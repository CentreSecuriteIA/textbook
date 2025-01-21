# File: scripts/mkdocs_section_numbers.py

import re
import json
import logging
from pathlib import Path
from typing import Dict, List, Tuple, Optional

logger = logging.getLogger(__name__)

def get_chapter_number(chapter_dir: Path) -> int:
    """Get chapter number from metadata json."""
    json_files = list(chapter_dir.glob("chapter_*_metadata.json"))
    if not json_files:
        raise FileNotFoundError(f"No metadata JSON file found in {chapter_dir}")
    
    with open(json_files[0], 'r', encoding='utf-8') as f:
        metadata = json.load(f)
    
    return metadata.get('chapter_number', 0)

def is_appendix_section(header: str) -> bool:
    """
    Check if a header is an appendix section.
    Matches variations like "Appendix:", "Appendix -", etc.
    """
    return bool(re.search(r'appendix\s*[:|-]?', header, re.IGNORECASE))

def update_subsection_numbers(lines: List[str], start_idx: int, section_prefix: str) -> int:
    """
    Update subsection numbers starting from a given index.
    Returns the index where subsections end.
    """
    current = {
        'h2': 0,  # ##
        'h3': 0,  # ###
        'h4': 0   # ####
    }
    i = start_idx + 1
    
    while i < len(lines):
        line = lines[i].strip()
        
        # Break if we hit another h1 header
        if line.startswith('# '):
            break
            
        # Handle h2 headers (##)
        elif line.startswith('## '):
            current['h2'] += 1
            current['h3'] = 0  # Reset deeper levels
            current['h4'] = 0
            title = re.sub(r'^## +', '', line)  # Extract existing title
            # For appendix sections, include the full chapter.appendix number
            if 'A' in section_prefix:
                number = f"{section_prefix}.{current['h2']}"
            else:
                number = f"{section_prefix}.{current['h2']}"
            lines[i] = f"## {number} {title}"
            
        # Handle h3 headers (###)
        elif line.startswith('### '):
            current['h3'] += 1
            current['h4'] = 0  # Reset deeper level
            title = re.sub(r'^### +', '', line)
            number = f"{section_prefix}.{current['h2']}.{current['h3']}"
            lines[i] = f"### {number} {title}"
            
        # Handle h4 headers (####)
        elif line.startswith('#### '):
            current['h4'] += 1
            title = re.sub(r'^#### +', '', line)
            number = f"{section_prefix}.{current['h2']}.{current['h3']}.{current['h4']}"
            lines[i] = f"#### {number} {title}"
            
        i += 1
    
    return i - 1

def is_introduction_section(header: str, is_first: bool) -> bool:
    """
    Check if a section is the introduction.
    Returns True if it's both the first section and has 'Introduction' in title.
    """
    return is_first and ('introduction' in header.lower() or 
                        header.strip('# ').lower() == '')  # Empty title case

def process(content: str, chapter_dir: Path) -> str:
    """
    Add section numbers to all headers.
    - Introduction section is not numbered
    - Regular sections get numbers like 1.1, 1.2
    - Appendices get numbers like 1.A1, 1.A2
    - Subsections are numbered up to 4 levels deep (1.1.1.1)
    """
    chapter_num = get_chapter_number(chapter_dir)
    lines = content.split('\n')
    current_section = 0
    appendix_count = 0
    i = 0
    is_first_section = True
    
    while i < len(lines):
        line = lines[i].strip()
        
        if line.startswith('# '):  # h1 headers only
            if is_introduction_section(line, is_first_section):
                # Keep introduction as is, without numbering
                title = re.sub(r'^# +', '', line)  # Just clean up the header marker
                lines[i] = f"# {title}"
                # Process subsections (if any) without main section number
                i = update_subsection_numbers(lines, i, chapter_num)
            elif is_appendix_section(line):
                appendix_count += 1
                section_prefix = f"{chapter_num}.A{appendix_count}"
                # Clean up the header text while preserving title
                title = re.sub(r'^# *(?:Appendix\s*[:|-])?\s*', '', line, flags=re.IGNORECASE)
                lines[i] = f"# {section_prefix} {title}"
                # Process subsections
                i = update_subsection_numbers(lines, i, section_prefix)
            else:
                current_section += 1
                section_prefix = f"{chapter_num}.{current_section}"
                title = re.sub(r'^# +', '', line)  # Extract existing title
                lines[i] = f"# {section_prefix} {title}"
                # Process subsections
                i = update_subsection_numbers(lines, i, section_prefix)
            
            is_first_section = False
        
        i += 1
    
    logger.info(f"Processed {current_section} main sections and {appendix_count} appendices")
    return '\n'.join(lines)

