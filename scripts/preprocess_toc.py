# preprocess_toc.py
import re
from typing import List, Tuple, Optional

def find_metadata_and_links_section(content: str) -> Tuple[int, int]:
    """Find the metadata and links sections at the start of the file."""
    patterns = [
        r'<metadata>.*?</metadata>\s*<links>.*?</links>',
        r'<metadata>.*?</metadata>',
        r'<links>.*?</links>'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, content, re.DOTALL)
        if match:
            return match.start(), match.end()
    return -1, -1

def is_toc_link(line: str) -> bool:
    """Check if a line is a TOC link."""
    # Matches markdown links that start with [ and point to internal references (#)
    return bool(re.match(r'^\s*\[.*?\]\(#.*?\)\s*$', line))

def find_toc_section(content: str) -> Optional[Tuple[int, int]]:
    """
    Find the table of contents section.
    Returns tuple of (start_pos, end_pos), or None if not found.
    """
    # Skip metadata/links section if present
    meta_start, meta_end = find_metadata_and_links_section(content)
    if meta_start != -1:
        content = content[meta_end:]
    
    # Split content into lines
    lines = content.split('\n')
    
    # Find start of TOC
    toc_start = -1
    for i, line in enumerate(lines):
        if i > 0 and lines[i-1].strip() == '' and is_toc_link(line):
            toc_start = i
            break
            
    if toc_start == -1:
        return None
        
    # Find end of TOC
    toc_end = toc_start
    for i in range(toc_start, len(lines)):
        if not is_toc_link(lines[i]) and lines[i].strip() != '':
            toc_end = i
            break
    
    # Convert line numbers back to character positions
    start_pos = sum(len(line) + 1 for line in lines[:toc_start])
    end_pos = sum(len(line) + 1 for line in lines[:toc_end])
    
    # Adjust positions if we skipped metadata
    if meta_end != -1:
        start_pos += meta_end
        end_pos += meta_end
        
    return start_pos, end_pos

def process(content: str) -> str:
    """Main processing function to remove table of contents."""
    # Find and remove the TOC header first
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if line.strip() == "# Table of Contents":
            lines.pop(i)
            content = '\n'.join(lines)
            break
    
    # Then find and remove TOC section
    toc_pos = find_toc_section(content)
    if toc_pos is not None:
        start, end = toc_pos
        content = content[:start] + content[end:]
    
    # Clean up extra newlines
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    return content

def test_processor():
    """Test function with sample content."""
    test_content = """
<metadata>
Authors: Test Author
</metadata>
<links>
[Link 1](#link1)
</links>

# Table of Contents
[Introduction](#introduction)
[Methods](#methods)
[Results](#results)

# Introduction
Content starts here...
    """
    
    processed = process(test_content)
    print("Processed content:")
    print(processed)

if __name__ == "__main__":
    test_processor()
