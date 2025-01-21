import re
from typing import Dict, List, Tuple

def replace_unicode_chars(content: str) -> str:
    """Replace problematic Unicode characters with LaTeX equivalents."""
    replacements = {
        '\u2009': ' ',     # Thin space
        '\u2013': '--',    # En dash
        '\u2014': '---',   # Em dash
        '\u2018': '`',     # Left single quote
        '\u2019': "'",     # Right single quote
        '\u201C': "``",    # Left double quote
        '\u201D': "''",    # Right double quote
        '\u2026': r'\ldots', # Ellipsis
        '\u00A0': '~',     # Non-breaking space
        '\u2212': '-',     # Minus sign
        '\u2022': r'$\bullet$',  # Bullet
        '\u2011': '-',     # Non-breaking hyphen
        '\u2003': ' ',     # Em space
        '\u200B': '',      # Zero width space
    }
    
    for char, replacement in replacements.items():
        content = content.replace(char, replacement)
    
    return content

def should_escape_in_section(text: str) -> bool:
    """Check if we're in a LaTeX section command."""
    section_commands = ['chapter', 'section', 'subsection', 'subsubsection', 'paragraph']
    for cmd in section_commands:
        if f'\\{cmd}{{' in text:
            return True
    return False

def escape_special_chars(content: str) -> str:
    """Escape LaTeX special characters while preserving URLs and paths."""
    replacements = {
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '~': r'\textasciitilde{}',
        '^': r'\textasciicircum{}'
    }
    
    def process_part(text: str, in_url: bool = False, in_section: bool = False) -> str:
        if in_url:
            return text
        if in_section:
            # Only escape & in section titles
            return text.replace('&', r'\&')
        for char, repl in replacements.items():
            text = text.replace(char, repl)
        return text
    
    # Split content to handle different contexts
    result = []
    i = 0
    while i < len(content):
        # Check for LaTeX commands
        if content[i] == '\\':
            # Find end of command
            cmd_end = content.find('}', i)
            if cmd_end != -1:
                cmd_part = content[i:cmd_end+1]
                if should_escape_in_section(cmd_part):
                    # Process section title specially
                    brace_start = cmd_part.find('{')
                    result.append(cmd_part[:brace_start+1])
                    result.append(process_part(cmd_part[brace_start+1:-1], in_section=True))
                    result.append('}')
                else:
                    result.append(cmd_part)
                i = cmd_end + 1
                continue
        
        # Check for markdown links
        if content[i:].startswith(']('):
            # Find end of URL
            url_end = content.find(')', i)
            if url_end != -1:
                result.append('](')
                result.append(process_part(content[i+2:url_end], in_url=True))
                result.append(')')
                i = url_end + 1
                continue
        
        # Check for image paths
        if content[i:].startswith('Images/'):
            # Find end of path
            path_end = content.find('.png', i)
            if path_end != -1:
                result.append(process_part(content[i:path_end+4], in_url=True))
                i = path_end + 4
                continue
        
        # Regular text
        result.append(process_part(content[i]))
        i += 1
    
    return ''.join(result)

def process(content: str) -> str:
    """Main processing function."""
    # Remove metadata and links sections
    content = re.sub(r'<metadata>.*?</metadata>\s*', '', content, flags=re.DOTALL)
    content = re.sub(r'<links>.*?</links>\s*', '', content, flags=re.DOTALL)
    content = re.sub(r'<userStyle>.*?</userStyle>\s*', '', content, flags=re.DOTALL)
    
    # Replace Unicode characters
    content = replace_unicode_chars(content)
    
    # Escape special LaTeX characters
    content = escape_special_chars(content)
    
    return content

def test_processor():
    """Test function with sample content."""
    test_content = r"""
\section{History & Evolution}
Regular text with & symbol
![Test](Images/test_image_1.png)
([Source, 2024](https://example.com/test_url&param=1))
"""
    processed = process(test_content)
    print(processed)

if __name__ == "__main__":
    test_processor()
