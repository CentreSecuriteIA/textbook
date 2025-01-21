# preprocess_comments.py
import re
from typing import List, Tuple

def remove_html_comments(content: str) -> str:
    """Remove HTML-style comments <!-- comment -->."""
    pattern = r'<!--.*?-->'
    return re.sub(pattern, '', content, flags=re.DOTALL)

def remove_style_tags(content: str) -> str:
    """Remove style tags and related metadata."""
    patterns = [
        r'<userStyle>.*?</userStyle>\s*\n?',
        r'<style>.*?</style>\s*\n?',
        r'<customStyle>.*?</customStyle>\s*\n?'
    ]
    
    for pattern in patterns:
        content = re.sub(pattern, '', content, flags=re.DOTALL)
    return content

def remove_markdown_comments(content: str) -> str:
    """Remove markdown-style comments."""
    patterns = [
        r'\[comment\]: ?#.*?\n',
        r'\[//\]: ?#.*?\n',
        r'\[//\]: <> \(.*?\)',
        r'\[//\]: # ".*?"'
    ]
    
    for pattern in patterns:
        content = re.sub(pattern, '', content, flags=re.DOTALL)
    return content

def remove_todo_comments(content: str) -> str:
    """Remove TODO-style comments."""
    patterns = [
        r'^TODO:.*$\n?',
        r'^FIXME:.*$\n?',
        r'^NOTE:.*$\n?',
        r'^XXX:.*$\n?'
    ]
    
    for pattern in patterns:
        content = re.sub(pattern, '', content, flags=re.MULTILINE)
    return content

def process(content: str) -> str:
    """Main processing function to remove all types of comments."""
    content = remove_html_comments(content)
    content = remove_style_tags(content)
    content = remove_markdown_comments(content)
    content = remove_todo_comments(content)
    
    # Clean up any leftover empty lines
    content = re.sub(r'\n{3,}', '\n\n', content)
    return content

def test_processor():
    """Test function with sample content."""
    test_content = """
# Test content

<!-- HTML comment -->
[comment]: # (Markdown comment)
TODO: Something to do
<userStyle>Normal</userStyle>

Regular content.
    """
    
    processed = process(test_content)
    print("Processed content:")
    print(processed)

if __name__ == "__main__":
    test_processor()
