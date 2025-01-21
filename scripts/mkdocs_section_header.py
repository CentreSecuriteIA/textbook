# File: scripts/mkdocs_section_header.py

import re
import logging
from pathlib import Path
from typing import Dict

logger = logging.getLogger(__name__)

# File: scripts/mkdocs_section_header.py

def calculate_reading_time(section_content: str) -> str:
    """Calculate reading time for individual section."""
    # Remove metadata and style tags
    content = re.sub(r'<userStyle>.*?</userStyle>\s*', '', section_content, flags=re.DOTALL)
    content = re.sub(r'<metadata>.*?</metadata>\s*', '', content, flags=re.DOTALL)
    content = re.sub(r'<links>.*?</links>\s*', '', content, flags=re.DOTALL)
    
    # Remove markdown formatting
    content = re.sub(r'#.*$', '', content, flags=re.MULTILINE)  # Remove headers
    content = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', content)  # Remove links but keep text
    content = re.sub(r'[*_`~]', '', content)  # Remove formatting characters
    
    # Calculate words and reading time
    word_count = len(re.sub(r'\s+', ' ', content).strip().split())
    reading_time = max(1, round(word_count / 200))
    
    return f"{reading_time} min"

def process(chapter_dir: Path, current_file: str, section_files: Dict[str, str]) -> None:
    """Add section header with reading time to a section file."""
    try:
        # Get current section content and calculate reading time
        content = section_files[current_file]
        reading_time = calculate_reading_time(content)

        # Generate minimal header with just reading time
        header = f'''<div class="section-meta">
    <div class="meta-item">
        <span class="meta-icon">
            <i class="fas fa-clock"></i>
        </span>
        <div class="meta-content">
            <div class="meta-label">Reading Time</div>
            <div class="meta-value">{reading_time}</div>
        </div>
    </div>
</div>'''
        
        # Add header after title in file
        section_path = chapter_dir / "mkdocs" / current_file
        with open(section_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        lines = content.split('\n')
        output = [lines[0], header] + lines[1:]
        
        with open(section_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(output))
            
        logger.info(f"Added reading time to {current_file}")
        
    except Exception as e:
        logger.error(f"Error processing section header for {current_file}: {e}")
        raise
