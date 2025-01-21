import re
from typing import Dict, List, Tuple

def is_in_latex_command(text: str, pos: int) -> bool:
    """Check if the position is inside a LaTeX command."""
    # Find last command before this position
    last_command = text.rfind('\\', 0, pos)
    if last_command == -1:
        return False
        
    # Find braces
    open_brace = text.find('{', last_command)
    if open_brace == -1 or open_brace > pos:
        return False
        
    # Count braces to this position
    opens = 0
    closes = 0
    for i in range(open_brace, pos):
        if text[i] == '{':
            opens += 1
        elif text[i] == '}':
            closes += 1
    
    # If we have more opens than closes, we're in a command
    return opens > closes

def escape_special_chars(text: str) -> str:
    """Escape special characters, but only in regular text."""
    result = ""
    i = 0
    while i < len(text):
        # Skip if in a LaTeX command
        if is_in_latex_command(text, i):
            result += text[i]
            i += 1
            continue
            
        # Handle special characters
        if text[i] == '&':
            result += r'\&'
        else:
            result += text[i]
        i += 1
    return result

def process_inline_formatting(content: str) -> str:
    """Process bold and italic text."""
    def replace_bold(match: re.Match) -> str:
        text = match.group(1)
        text = escape_special_chars(text)
        return f'\\textbf{{{text}}}'
    
    def replace_italic(match: re.Match) -> str:
        text = match.group(1)
        text = escape_special_chars(text)
        return f'\\textit{{{text}}}'
    
    # Process bold first
    content = re.sub(r'\*\*([^*]+)\*\*', replace_bold, content)
    # Then italic
    content = re.sub(r'(?<!\\)\*([^*]+)\*', replace_italic, content)
    return content

def fix_spacing(content: str) -> str:
    """Fix paragraph spacing and line breaks."""
    # Add blank line before sections
    content = re.sub(r'(\\(?:sub)*section{[^}]+})', r'\n\n\1', content)
    
    # Ensure blank line after sections
    content = re.sub(r'(\\(?:sub)*section{[^}]+})\n(?!\n)', r'\1\n\n', content)
    
    # Convert single newlines to spaces within paragraphs
    content = re.sub(r'([^\n])\n([^\n])', r'\1 \2', content)
    
    # Clean up multiple newlines
    content = re.sub(r'\n{3,}', r'\n\n', content)
    
    return content

def process(content: str) -> str:
    """Main processing function."""
    content = process_inline_formatting(content)
    content = fix_spacing(content)
    return content
