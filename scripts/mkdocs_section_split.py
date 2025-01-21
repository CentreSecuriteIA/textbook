# File: scripts/mkdocs_section_split.py

import re
import logging
from pathlib import Path
from typing import Dict, List, Tuple, Optional

logger = logging.getLogger(__name__)

def get_section_boundaries(content: str) -> List[Tuple[int, int, str, str]]:
    """
    Find the start and end positions of each section.
    Returns list of tuples (start_pos, end_pos, section_title, section_id).
    """
    sections = []
    current_start = 0
    
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if line.strip().startswith('# '):  # Any h1 header
            if current_start != i:  # If not the first line
                # Get previous section content
                prev_header = lines[current_start].strip()
                # Extract section number
                number_match = re.search(r'^#\s+\d+\.([A\d]+)\s+', prev_header)
                section_num = number_match.group(1) if number_match else ""
                
                sections.append((
                    current_start,
                    i,
                    prev_header,  # Keep full header
                    section_num
                ))
            current_start = i
    
    # Don't forget the last section
    if current_start < len(lines):
        last_header = lines[current_start].strip()
        number_match = re.search(r'^#\s+\d+\.([A\d]+)\s+', last_header)
        section_num = number_match.group(1) if number_match else ""
        
        sections.append((
            current_start,
            len(lines),
            last_header,  # Keep full header
            section_num
        ))
    
    return sections

def process(content: str, mkdocs_dir: Path) -> Dict[str, str]:
    """
    Split content into files and write them to mkdocs directory.
    Returns dict mapping filenames to content for use by subsequent processors.
    """
    try:
        sections = get_section_boundaries(content)
        files_content = {}
        lines = content.split('\n')
        
        # Create mkdocs directory if it doesn't exist
        mkdocs_dir.mkdir(parents=True, exist_ok=True)
        
        for i, (start, end, header, section_num) in enumerate(sections):
            section_content = '\n'.join(lines[start:end]).strip()
            
            if i == 0:  # First section is Introduction
                filename = "README.md"
            else:
                # Add zero padding for regular section numbers
                if section_num.startswith('A'):
                    filename = f"{section_num}.md"  # Keep A1, A2 as is
                else:
                    filename = f"{int(section_num):02d}.md"  # Pad with zeros: 01, 02, etc.

            # Write file
            output_path = mkdocs_dir / filename
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(section_content)
            
            # Store content in dictionary for return
            files_content[filename] = section_content
            logger.info(f"Created section file: {filename}")
        
        logger.info(f"Split content into {len(files_content)} files")
        return files_content
        
    except Exception as e:
        logger.error(f"Error splitting sections: {e}")
        raise
