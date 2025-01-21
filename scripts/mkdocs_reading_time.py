# File: scripts/mkdocs_reading_time.py

import re
import logging
from pathlib import Path
from typing import Dict
import yaml

logger = logging.getLogger(__name__)

def calculate_word_count(content: str) -> int:
    """Calculate word count from content after cleaning formatting."""
    # Remove metadata and style tags
    content = re.sub(r'<userStyle>.*?</userStyle>\s*', '', content, flags=re.DOTALL)
    content = re.sub(r'<metadata>.*?</metadata>\s*', '', content, flags=re.DOTALL)
    content = re.sub(r'<links>.*?</links>\s*', '', content, flags=re.DOTALL)
    
    # Remove markdown formatting
    content = re.sub(r'#.*$', '', content, flags=re.MULTILINE)  # Remove headers
    content = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', content)  # Remove links but keep text
    content = re.sub(r'[*_`~]', '', content)  # Remove formatting characters
    
    # Clean whitespace and count words
    return len(re.sub(r'\s+', ' ', content).strip().split())

def calculate_section_times(content: str) -> Dict[str, int]:
    """Calculate reading times for core content and appendices."""
    # Look for numbered appendix headers (e.g. "# 1.A1")
    appendix_match = re.search(r'^#\s+\d+\.A\d+', content, re.MULTILINE)
    
    if appendix_match:
        # Split content at appendix
        main_content = content[:appendix_match.start()]
        appendix_content = content[appendix_match.start():]
        
        # Calculate word counts
        main_words = calculate_word_count(main_content)
        appendix_words = calculate_word_count(appendix_content)
        
        # Convert to reading times (200 words per minute)
        return {
            'core': max(1, round(main_words / 200)),
            'appendix': max(1, round(appendix_words / 200))
        }
    else:
        # Just calculate total time if no appendices
        word_count = calculate_word_count(content)
        return {
            'core': max(1, round(word_count / 200)),
            'appendix': 0
        }

def process(content: str, chapter_dir: Path) -> str:
    """
    Process content to calculate and store reading times.
    Returns the content unchanged.
    """
    try:
        # Calculate reading times
        reading_times = calculate_section_times(content)
        
        # Create mkdocs directory if it doesn't exist
        mkdocs_dir = chapter_dir / "mkdocs"
        mkdocs_dir.mkdir(parents=True, exist_ok=True)
        
        # Write reading times to YAML file
        reading_times_path = mkdocs_dir / ".reading_times.yml"
        with open(reading_times_path, 'w', encoding='utf-8') as f:
            yaml.dump(reading_times, f)
        
        logger.info(
            f"Calculated reading times - Core: {reading_times['core']} min, "
            f"Appendix: {reading_times['appendix']} min"
        )
        
        # Return content unchanged
        return content
        
    except Exception as e:
        logger.error(f"Error calculating reading times: {e}")
        raise

def test_processor():
    """Test function with sample content."""
    test_content = """# Main Content
This is the main content.
It has multiple paragraphs.

# 1.A1 First Appendix
This is appendix content.

# 1.A2 Second Appendix
More appendix content."""
    
    test_dir = Path("test_chapter")
    test_dir.mkdir(exist_ok=True)
    
    process(test_content, test_dir)
    
    # Read and print the results
    with open(test_dir / "mkdocs" / ".reading_times.yml", 'r') as f:
        print("\nCalculated reading times:")
        print(yaml.safe_load(f))

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    test_processor()
