import re
from typing import Dict, List, Tuple

def convert_citation_link(match: re.Match) -> str:
    """Convert citation-style links ([Author et al., 2024](url)) preserving parentheses."""
    text = match.group(1)  # Authors and year
    url = match.group(2)   # URL
    return f'(\\href{{{url}}}{{{text}}})'

def convert_inline_link(match: re.Match) -> str:
    """Convert regular markdown links [text](url)."""
    text = match.group(1)
    url = match.group(2)
    return f'\\href{{{url}}}{{{text}}}'

def process(content: str) -> str:
    """Convert markdown links to LaTeX href commands."""
    # Skip image markdown patterns
    content_parts = re.split(r'(!\[.*?\]\(.*?\))', content)
    processed_parts = []
    
    for i, part in enumerate(content_parts):
        # Skip image parts (odd indices)
        if i % 2 == 1:
            processed_parts.append(part)
            continue
            
        # Handle citation-style links: ([Author et al., 2024](url))
        citation_pattern = r'\(\[([^,\]]+(?:,\s*\d{4})?)\]\(([^)]+)\)\)'
        part = re.sub(citation_pattern, convert_citation_link, part)
        
        # Handle remaining markdown links: [text](url)
        inline_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
        part = re.sub(inline_pattern, convert_inline_link, part)
        
        processed_parts.append(part)
    
    return ''.join(processed_parts)

def test_processor():
    """Test function with sample content."""
    test_content = """
![Image](Images/test.png)
Regular link [Click here](https://example.com)
Citation ([Author et al., 2024](https://example.com/paper))
Another image ![Alt text](Images/test2.png)
"""
    
    processed = process(test_content)
    print("Processed content:")
    print(processed)

if __name__ == "__main__":
    test_processor()
