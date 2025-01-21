# File: scripts/mkdocs_section_ids.py

import re
import logging
from pathlib import Path
from typing import Dict, List, Optional

logger = logging.getLogger(__name__)

def is_introduction_section(header: str, is_first: bool) -> bool:
    """Check if a section is the introduction."""
    return is_first and ('introduction' in header.lower() or 
                        header.strip('# ').lower() == '')

def add_id_to_header(header: str, section_id: str) -> str:
    """Add an ID to a header line if section_id is provided."""
    if not section_id:  # Skip if no ID needed
        return header
        
    # Check if header already has an ID
    if '{:' in header:
        # Update existing ID
        return re.sub(r'{:.*?}', f'{{: #{section_id}}}', header)
    else:
        # Add new ID
        return f'{header} {{: #{section_id}}}'

def is_appendix_section(header: str) -> bool:
    """Check if a header contains appendix marker."""
    return bool(re.search(r'\.A\d+', header))


def extract_section_id(header: str) -> str:
    """
    Extract and format section numbers for ID, skipping the main section number.
    Examples:
    Regular sections:
    "# 1.2 Title" -> ""  (no ID needed, handled by file name)
    "## 1.2.1 Title" -> "01"
    "### 1.2.1.1 Title" -> "01-01"
    
    Appendix sections:
    "# 1.A1 Title" -> ""  (no ID needed, handled by file name)
    "## 1.A1.2 Title" -> "02"
    "### 1.A1.2.1 Title" -> "02-01" (parent section number - subsection number)
    """
    # Skip IDs for h1 headers
    if header.startswith('# '):
        return ""

    # Count header level
    level = len(re.match(r'^#+', header).group())
    
    if is_appendix_section(header):
        # Extract the structure: A1.2.1 -> [A1, 2, 1]
        numbers = re.findall(r'\.A\d+|\.(\d+)', header)
        # Filter out None values and get only the numeric parts
        numbers = [n for n in numbers if n]
        
        if level == 2:  # h2 header
            if numbers:
                return f"{int(numbers[0]):02d}"
        elif level == 3:  # h3 header
            if len(numbers) >= 2:
                return f"{int(numbers[0]):02d}-{int(numbers[1]):02d}"
        elif level == 4:  # h4 header
            if len(numbers) >= 3:
                return f"{int(numbers[0]):02d}-{int(numbers[1]):02d}-{int(numbers[2]):02d}"
    else:
        # Regular sections - keep existing logic
        numbers = re.findall(r'\.(\d+)', header)
        if len(numbers) > 1:
            # Skip main section number, format remaining as hierarchy
            subsection_numbers = [f"{int(num):02d}" for num in numbers[1:]]
            return "-".join(subsection_numbers)
        elif len(numbers) == 1:
            return f"{int(numbers[0]):02d}"
    
    return ""




def process(content: str) -> str:
    """
    Add section IDs for URLs to headers.
    - h1 headers get no ID (handled by file name)
    - h2 headers get simple numbers {: #01}
    - h3+ headers get hierarchical numbers {: #01-01}
    """
    lines = content.split('\n')
    is_first_section = True
    
    for i, line in enumerate(lines):
        # Skip non-header lines including style tags
        if not line.strip().startswith('#'):
            continue
            
        # Skip introduction section entirely
        if is_introduction_section(line, is_first_section):
            if line.startswith('# '):
                is_first_section = False
            continue
            
        # Extract and format section ID
        section_id = extract_section_id(line)
        if section_id:  # Only add ID if we got one
            lines[i] = add_id_to_header(line, section_id)
            
        # Mark that we're past the first section
        if line.startswith('# '):
            is_first_section = False
    
    logger.info("Added section IDs for URLs and table of contents navigation")
    return '\n'.join(lines)

def test_processor():
    """Test function with sample content."""
    test_content = """# Introduction
## Some Intro Section

# 1.1 First Section
## 1.1.1 Subsection One
### 1.1.1.1 Deep Section
#### 1.1.1.1.1 Very Deep

# 1.2 Second Section {: #old-id}
## 1.2.1 Another Subsection
### 1.2.1.1 Sub-sub Section

# 1.A1 Appendix: Extra Info
## 1.A1.1 Appendix Subsection
### 1.A1.1.1 Deep Appendix"""

    processed = process(test_content)
    print("\nProcessed content:")
    print(processed)
    print("\nVerify that:")
    print("1. h1 headers have no IDs")
    print("2. h2 headers have simple IDs like {: #01}")
    print("3. h3+ headers have hierarchical IDs like {: #01-01}")
    print("4. Existing IDs are updated, not duplicated")
    print("5. Introduction sections have no IDs")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    test_processor()
