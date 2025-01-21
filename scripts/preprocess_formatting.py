# preprocess_formatting.py
import re
from typing import List, Tuple

def fix_multiple_bold_sections(content: str) -> str:
    """Fix cases where multiple bold sections appear consecutively."""
    # Pattern matches consecutive bold sections
    pattern = r'\*\*([^*]+?)\*\*\s*\*\*([^*]+?)\*\*'
    
    def combine_bold_sections(match):
        """Combine consecutive bold sections into one."""
        parts = [match.group(1), match.group(2)]
        # Clean up any extra spaces between parts
        combined = ' '.join(part.strip() for part in parts)
        return f'**{combined}**'
    
    # Keep applying the fix until no more changes are made
    while True:
        new_content = re.sub(pattern, combine_bold_sections, content)
        if new_content == content:
            break
        content = new_content
    
    return content

def fix_bold_punctuation(content: str) -> str:
    """Fix punctuation placement in bold text headers."""
    def fix_punct(match):
        # Get the bold text and the punctuation
        text = match.group(1).strip()
        punct = match.group(2)
        return f'**{text}{punct}**'
    
    # Pattern matches bold text followed by punctuation
    pattern = r'\*\*([^*]+?)\*\*(\s*[.:])'
    return re.sub(pattern, fix_punct, content)

def fix_paragraph_bold_headers(content: str) -> str:
    """Fix paragraphs that start with bold text."""
    def fix_paragraph(match):
        # Get the bold header and the rest of the paragraph
        header = match.group(1).strip()
        rest = match.group(2).strip() if match.group(2) else ''
        
        # Handle cases where there might be extra bold markers
        header = re.sub(r'\*\*\s*\*\*', ' ', header)
        
        # Clean up any duplicate spaces
        header = ' '.join(header.split())
        
        if rest:
            return f'**{header}** {rest}'
        return f'**{header}**'
    
    # Pattern matches paragraphs that start with bold text
    pattern = r'\*\*([^*]+?)\*\*(\s*[^\n]+)?'
    return re.sub(pattern, fix_paragraph, content)

def normalize_whitespace(content: str) -> str:
    """Normalize whitespace while preserving paragraph breaks."""
    # Replace multiple spaces with single space
    content = re.sub(r' +', ' ', content)
    
    # Normalize paragraph breaks
    content = re.sub(r'\n\s*\n\s*\n+', '\n\n', content)
    
    return content.strip()

def process(content: str) -> str:
    """Main processing function to fix formatting issues."""
    # First fix multiple consecutive bold sections
    content = fix_multiple_bold_sections(content)
    
    # Fix paragraph headers
    content = fix_paragraph_bold_headers(content)
    
    # Clean up any remaining formatting artifacts
    content = re.sub(r'\*\*\s+\*\*', ' ', content)  # Remove empty bold sections
    
    # Normalize whitespace
    content = normalize_whitespace(content)
    
    return content

def test_processor():
    """Test function with sample input."""
    test_content = """
**How do benchmarks influence**** AI Safety****?** Without standardized measurements...

**Benchmarking ****Ethics**** & Bias**. The ETHICS benchmark...

Regular paragraph without bold.

**What makes ****evaluations ****different from benchmarks?** Evaluations are...
    """
    
    processed = process(test_content)
    print("Processed content:")
    print(processed)

if __name__ == "__main__":
    test_processor()
