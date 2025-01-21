# File: scripts/mkdocs_images.py

import re
import json
import logging
from pathlib import Path
from typing import Optional, Match

logger = logging.getLogger(__name__)

def get_chapter_number(chapter_dir: Path) -> int:
    """Get chapter number from metadata json."""
    # Try to find metadata file
    json_files = list(chapter_dir.glob("chapter_*_metadata.json"))
    if not json_files:
        raise FileNotFoundError(f"No metadata JSON file found in {chapter_dir}")
    
    with open(json_files[0], 'r', encoding='utf-8') as f:
        metadata = json.load(f)
    
    return metadata.get('chapter_number', 0)

def process_image_caption(match: Match, chapter_number: int, figure_count: int) -> str:
    """Process a single image caption match."""
    image_markdown = match.group(1)
    caption = match.group(2).strip()
    
    # Create figure with chapter-prefixed numbered caption
    figure_html = f'''<figure markdown="span">
{image_markdown}{{ loading=lazy }}
  <figcaption markdown="1"><b>Figure {chapter_number}.{figure_count}:</b> {caption}</figcaption>
</figure>'''
    
    return figure_html

def process(content: str, chapter_dir: Path) -> str:
    """
    Convert image markdown with <caption> tags to figure format.
    
    Example:
    ![Alt text](image.png)
    <caption>A description of the image</caption>
    
    Becomes:
    <figure markdown="span">
    ![Alt text](image.png){ loading=lazy }
      <figcaption markdown="1"><b>Figure X.Y:</b> A description of the image</figcaption>
    </figure>
    """
    # Get chapter number from metadata
    chapter_number = get_chapter_number(chapter_dir)
    
    # Pattern matches image followed by caption
    pattern = r'(!\[.*?\]\(.*?\))\s*<caption>\s*(.*?)\s*</caption>'
    
    # Keep track of figure count
    figure_count = 1  # Starts at 1
    
    def replacement(match: Match) -> str:
        nonlocal figure_count
        result = process_image_caption(match, chapter_number, figure_count)
        figure_count += 1
        return result
    
    # Process all caption instances
    processed_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    logger.info(f"Processed {figure_count - 1} images with captions")
    return processed_content

def test_processor():
    """Test function with sample content."""
    # Create test directory and metadata
    test_dir = Path("test_chapter")
    test_dir.mkdir(exist_ok=True)
    
    metadata = {
        "chapter_number": 3,
        "chapter_title": "Test Chapter"
    }
    
    with open(test_dir / "chapter_3_metadata.json", 'w') as f:
        json.dump(metadata, f)
    
    test_content = """# Chapter 3 - Test Chapter

This is a test image:

![Test image](Images/test.png)
<caption>This is a test image caption</caption>

And another:

![Another test](Images/test2.png)
<caption>Another caption with *markdown* and **formatting**</caption>
"""
    
    processed = process(test_content, test_dir)
    print("\nProcessed content:")
    print(processed)
    print("\nNote: Check that figures are numbered 3.1, 3.2, etc.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    test_processor()
