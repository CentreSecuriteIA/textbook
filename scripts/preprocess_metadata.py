# preprocess_metadata.py
import re
import json
from pathlib import Path
from typing import Dict, Tuple, Optional

def extract_chapter_info(content: str) -> Tuple[Optional[str], Optional[str]]:
    """Extract chapter number and title, returns (number, title)."""
    chapter_pattern = r'^#\s*Chapter\s+(\d+)\s*[-–—]\s*(.+?)$'
    
    for line in content.split('\n'):
        match = re.match(chapter_pattern, line.strip())
        if match:
            return match.group(1), match.group(2).strip()
    return None, None

def extract_metadata(content: str) -> Dict:
    """Extract metadata from <metadata> tags."""
    metadata = {}
    pattern = r'<metadata>\s*(.*?)\s*</metadata>'
    match = re.search(pattern, content, re.DOTALL)
    
    if match:
        metadata_text = match.group(1)
        for line in metadata_text.strip().split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                key = key.strip()
                value = value.strip()
                
                # Special handling for "Also available on"
                if key == "Also available on":
                    # Extract links from format [text](url)
                    links = []
                    for text, url in re.findall(r'\[([^\]]+)\]\(([^)]+)\)', value):
                        links.append({
                            "name": text.strip(),
                            "url": url.strip()
                        })
                    metadata[key] = links
                else:
                    metadata[key] = value

    # Extract links section
    links_pattern = r'<links>\s*(.*?)\s*</links>'
    links_match = re.search(links_pattern, content, re.DOTALL)
    if links_match:
        links_text = links_match.group(1)
        # Process each link [text](url)
        for text, url in re.findall(r'\[([^\]]+)\]\(([^)]+)\)', links_text):
            metadata[text.strip()] = url.strip()
                
    return metadata

def remove_chapter_title(content: str) -> str:
    """Remove the chapter title line from content."""
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if re.match(r'^#\s*Chapter\s+\d+\s*[-–—]', line.strip()):
            lines.pop(i)
            break
    return '\n'.join(lines)

def remove_metadata_section(content: str) -> str:
    """Remove the metadata section from content."""
    content = re.sub(r'<metadata>.*?</metadata>\s*', '', content, flags=re.DOTALL)
    content = re.sub(r'<links>.*?</links>\s*', '', content, flags=re.DOTALL)
    return content

def process(content: str, output_dir: Path) -> str:
    """Process metadata and return modified content."""
    # Extract chapter info
    chapter_num, chapter_title = extract_chapter_info(content)
    if not chapter_num:
        raise ValueError("Could not find chapter number and title")
        
    # Create metadata dictionary
    metadata = {
        "chapter_number": int(chapter_num),
        "chapter_title": chapter_title,
    }
    
    # Extract additional metadata
    metadata.update(extract_metadata(content))
    
    # Write metadata to JSON file in parent directory of output_dir
    json_path = output_dir.parent / f"chapter_{chapter_num}_metadata.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
        
    # Remove chapter title and metadata section from content
    content = remove_chapter_title(content)
    content = remove_metadata_section(content)
    
    # Clean up extra newlines
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    return content

def test_processor():
    """Test function with sample content."""
    test_content = """# Chapter 5 - Test Chapter

<metadata>
Authors: Test Author
Affiliation: Test University
</metadata>

Content starts here..."""
    
    test_dir = Path("test_output")
    processed = process(test_content, test_dir)
    print("Original content:")
    print(test_content)
    print("\nProcessed content:")
    print(processed)
    print("\nGenerated metadata file in:", test_dir)

if __name__ == "__main__":
    test_processor()
