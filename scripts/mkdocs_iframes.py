# File: scripts/mkdocs_iframes.py

import re
import json
import logging
from pathlib import Path
from typing import Match

logger = logging.getLogger(__name__)

def get_chapter_number(chapter_dir: Path) -> int:
    """Get chapter number from metadata json."""
    json_files = list(chapter_dir.glob("chapter_*_metadata.json"))
    if not json_files:
        raise FileNotFoundError(f"No metadata JSON file found in {chapter_dir}")
    
    with open(json_files[0], 'r', encoding='utf-8') as f:
        metadata = json.load(f)
    
    return metadata.get('chapter_number', 0)

def process_iframe(match: Match, chapter_number: int, iframe_count: int) -> str:
    """Process a single iframe match."""
    iframe_content = match.group(1).strip()
    caption = match.group(2).strip()
    
    figure_html = f'''<figure class="iframe-figure" markdown="span">
{iframe_content}
  <figcaption markdown="1"><b>Interactive Figure {chapter_number}.{iframe_count}:</b> {caption}</figcaption>
</figure>'''
    
    return figure_html

def process(content: str, chapter_dir: Path) -> str:
    """
    Convert iframe with <caption-iframe> tags to figure format.
    
    Example:
    <iframe src="..."></iframe>
    <caption-iframe>A description of the interactive content</caption-iframe>
    """
    # Get chapter number from metadata
    chapter_number = get_chapter_number(chapter_dir)
    
    # Pattern matches iframe with caption
    pattern = r'(<iframe[^>]*>[^<]*</iframe>)\s*<caption-iframe>\s*(.*?)\s*</caption-iframe>'
    
    # Keep track of iframe count
    iframe_count = 1
    
    def replacement(match: Match) -> str:
        nonlocal iframe_count
        result = process_iframe(match, chapter_number, iframe_count)
        iframe_count += 1
        return result
    
    # Process all iframe instances
    processed_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    logger.info(f"Processed {iframe_count - 1} iframes")
    return processed_content

def test_processor():
    """Test function with sample content."""
    test_dir = Path("test_chapter")
    test_dir.mkdir(exist_ok=True)
    
    metadata = {
        "chapter_number": 4,
        "chapter_title": "Test Chapter"
    }
    
    with open(test_dir / "chapter_4_metadata.json", 'w') as f:
        json.dump(metadata, f)
    
    test_content = '''# Chapter 4 - Test Chapter

Here's an interactive figure:

<iframe src="https://example.com/interactive1" width="100%" height="400"></iframe>
<caption-iframe>First interactive figure</caption-iframe>

And another:

<iframe src="https://example.com/interactive2" width="100%" height="500"></iframe>
<caption-iframe>Second figure with *markdown* and **formatting**</caption-iframe>
'''
    
    processed = process(test_content, test_dir)
    print("\nProcessed content:")
    print(processed)
    print("\nNote: Check that iframes are numbered 4.1, 4.2, etc.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    test_processor()
