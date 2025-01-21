# convert_lists.py
import re
from typing import List, Tuple

def convert_list_items(content: str) -> str:
    """Convert markdown list items to LaTeX itemize environment."""
    # Find paragraphs that begin with bullet points
    paragraph_pattern = r'(?:^|\n\n)((?:- (?:[^\n]+)\n?)+)'
    
    def convert_list(match: re.Match) -> str:
        list_content = match.group(1).strip()
        items = list_content.split('\n')
        
        # Convert items to LaTeX format
        latex_items = []
        for item in items:
            if item.strip().startswith('- '):
                item_content = item.strip()[2:]  # Remove '- ' marker
                latex_items.append(f'    \\item {item_content}')
        
        # Build LaTeX list
        latex_list = [
            '\\begin{itemize}',
            *latex_items,
            '\\end{itemize}'
        ]
        
        return '\n'.join(latex_list)
    
    content = re.sub(
        paragraph_pattern,
        convert_list,
        content,
        flags=re.MULTILINE
    )
    return content

def process(content: str) -> str:
    """Process both bullet points and numbered lists."""
    return convert_list_items(content)

def test_processor():
    """Test function with sample content."""
    test_content = """
These capabilities fall into several categories:

- **Cyber-offense**: The model can discover vulnerabilities.
- **Deception**: The model can deceive.
- **Example**: Another test.

Regular paragraph here.
"""
    processed = process(test_content)
    print("Processed content:")
    print(processed)

if __name__ == "__main__":
    test_processor()
