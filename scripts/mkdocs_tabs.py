# File: scripts/mkdocs_tabs.py

import re
import logging
from pathlib import Path
from typing import Match

logger = logging.getLogger(__name__)

def process_tab_content(tab_content: str) -> str:
    """
    Process content within a tab section.
    - Indents all non-empty lines with 4 spaces
    """
    lines = tab_content.split('\n')
    indented_lines = []
    
    for line in lines:
        # Skip indenting empty lines to preserve spacing
        if line.strip():
            indented_lines.append('    ' + line)
        else:
            indented_lines.append(line)
            
    return '\n'.join(indented_lines)

def process(content: str) -> str:
    """
    Process tab sections in content.
    
    Handles:
    1. Converting $$$$ markers to spaces
    2. Processing <tab> sections by indenting their content
    
    Example:
    <tab>
    This content will be indented
    Multiple lines are handled
    
    Empty lines preserved
    </tab>
    """
    logger.debug("Processing tab sections...")
    
    # First replace any $$$$ markers with spaces
    content = content.replace("$$$$", "    ")
    
    # Count tabs before processing to report in logging
    tab_count = len(re.findall(r'<tab>', content))
    
    # Process <tab> sections
    pattern = r'<tab>(.*?)</tab>'
    processed_content = re.sub(
        pattern,
        lambda m: process_tab_content(m.group(1)),
        content,
        flags=re.DOTALL
    )
    
    logger.info(f"Processed {tab_count} tab sections")
    return processed_content

def test_processor():
    """Test function with sample content."""
    test_content = """Here's some normal content.

<tab>
This is tabbed content
It should be indented
  This line has extra indentation
</tab>

Here's more normal content.

<tab>
Another tabbed section
With $$$$special markers
That should become spaces
</tab>"""

    processed = process(test_content)
    print("\nProcessed content:")
    print(processed)
    print("\nNote: Check that tab sections are properly indented")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    test_processor()
