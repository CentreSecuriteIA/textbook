# File: scripts/mkdocs_pages.py

import re
import json
import yaml
import logging
from pathlib import Path
from typing import Dict, List, Tuple

logger = logging.getLogger(__name__)

def get_chapter_info(chapter_dir: Path) -> tuple[int, str]:
    """Get chapter number and title from metadata JSON."""
    json_files = list(chapter_dir.glob("chapter_*_metadata.json"))
    if not json_files:
        raise FileNotFoundError(f"No metadata JSON file found in {chapter_dir}")
    
    with open(json_files[0], 'r', encoding='utf-8') as f:
        metadata = json.load(f)
    
    return metadata.get('chapter_number', 0), metadata.get('chapter_title', '')

def get_section_info(content: str) -> tuple[str, str]:
    """
    Extract section number and title from content.
    Returns tuple of (section_number, title).
    """
    first_line = content.split('\n')[0].strip()
    # Extract section number and title, now including full chapter number
    match = re.match(r'^#\s+(\d+\.(?:A?\d+)?(?:\.\d+)*)\s+(.+?)(?:\s+{:.*})?$', first_line)
    if match:
        section_num = match.group(1)
        title = match.group(2).strip()
        return section_num, title
    return "", first_line.replace('# ', '').strip()

def process(files_content: Dict[str, str], chapter_dir: Path) -> None:
    """
    Generate .pages.yml file for MkDocs navigation.
    """
    try:
        # Get chapter info from metadata
        chapter_num, chapter_title = get_chapter_info(chapter_dir)
        
        # Build navigation list
        nav = []
        appendix_sections = []
        
        # Add introduction first with chapter number
        if "README.md" in files_content:
            nav.append({f"Chapter {chapter_num:02d}": "README.md"})
        
        # Process regular sections first
        numbered_files = sorted([f for f in files_content.keys() 
                               if f != "README.md" and not f.startswith('A')])
        
        for filename in numbered_files:
            content = files_content[filename]
            section_num, title = get_section_info(content)
            # Format as "1.1 - Title" (including chapter number)
            nav_title = f"{section_num} - {title}"
            nav.append({nav_title: filename})
        
        # Process appendix sections
        appendix_files = sorted([f for f in files_content.keys() 
                               if f.startswith('A')])
        
        for filename in appendix_files:
            content = files_content[filename]
            section_num, title = get_section_info(content)
            # Format as "1.A1 - Title" (including chapter number)
            if section_num:
                appendix_title = f"{section_num} - {title}"
            else:
                # Fallback if section number not found
                appendix_num = re.search(r'A(\d+)', filename).group(1)
                appendix_title = f"{chapter_num}.A{appendix_num} - {title}"
            appendix_sections.append({appendix_title: filename})
        
        # Add appendices if any exist
        if appendix_sections:
            nav.append({"Appendix": appendix_sections})
        
        # Create pages config
        pages_config = {
            "nav": nav,
            "title": f"{chapter_num:02d} - {chapter_title}"
        }
        
        # Write .pages.yml
        mkdocs_dir = chapter_dir / "mkdocs"
        mkdocs_dir.mkdir(exist_ok=True)
        
        with open(mkdocs_dir / ".pages.yml", 'w', encoding='utf-8') as f:
            yaml.dump(pages_config, f, default_flow_style=False, allow_unicode=True)
        
        logger.info("Generated .pages.yml for MkDocs navigation")
        
    except Exception as e:
        logger.error(f"Error generating pages config: {e}")
        raise

def test_processor():
    """Test function with sample content."""
    test_dir = Path("test_chapter")
    test_dir.mkdir(exist_ok=True)
    
    # Create test metadata
    metadata = {
        "chapter_number": 1,
        "chapter_title": "Capabilities"
    }
    
    with open(test_dir / "chapter_1_metadata.json", 'w', encoding='utf-8') as f:
        json.dump(metadata, f)
    
    # Sample content
    files_content = {
        "README.md": "# Introduction\nThis is the introduction.",
        "01.md": "# 1.1 State-of-the-Art AI\nThis is the first section.",
        "02.md": "# 1.2 Foundation Models\nThis is the second section.",
        "A1.md": "# 1.A1 Expert Opinions\nThis is an appendix.",
        "A2.md": "# 1.A2 Discussion on LLMs\nThis is another appendix."
    }
    
    process(files_content, test_dir)
    
    # Print the generated .pages.yml
    with open(test_dir / "mkdocs" / ".pages.yml", 'r') as f:
        print("\nGenerated .pages.yml:")
        print(f.read())

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    test_processor()
