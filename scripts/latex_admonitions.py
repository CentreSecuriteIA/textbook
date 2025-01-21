import re
from typing import Dict, List, Tuple, Optional

def convert_figure_to_includegraphics(content: str) -> str:
    """Convert figure environments to simple includegraphics when inside tcolorbox."""
    pattern = (
        r'\\begin{figure}\[htbp\]\s*'
        r'\\centering\s*'
        r'\\includegraphics\[width=0\.8\\textwidth\]{(.*?)}\s*'
        r'\\caption{(.*?)}\s*'
        r'\\end{figure}'
    )
    
    replacement = (
        r'\\centering\n'
        r'\\includegraphics[width=0.8\\textwidth]{\1}\n'
        r'\\captionof{figure}{\2} \\justifying\n\n'
    )
    
    return re.sub(pattern, replacement, content, flags=re.DOTALL)

def extract_admonition_info(block: str) -> Tuple[str, Optional[str], str]:
    """Extract type, title, and content from admonition block."""
    header_pattern = r'(?:[!?]\s*){3}[-+]?\s*(\w+)(?:\s*"([^"]*)")?\s*\n'
    match = re.match(header_pattern, block)
    
    if not match:
        return "", None, block
        
    adm_type = match.group(1)
    title = match.group(2)  # May be None
    
    # Find content between <tab> tags if they exist
    tab_pattern = r'<tab>\s*(.*?)\s*</tab>'
    content_match = re.search(tab_pattern, block, re.DOTALL)
    
    if content_match:
        content = content_match.group(1).strip()
    else:
        # If no <tab> tags, take everything after the header
        content = block[match.end():].strip()
    
    return adm_type, title, content

def format_paragraphs(content: str) -> str:
    """Format paragraph breaks in content."""
    # Split content into paragraphs
    paragraphs = [p.strip() for p in content.split('\n\n') if p.strip()]
    
    # Join paragraphs with proper spacing
    return '\n\n'.join(paragraphs)

def convert_to_tcolorbox(adm_type: str, title: Optional[str], content: str) -> str:
    """Convert to LaTeX tcolorbox."""
    # If no title provided, use capitalized type
    box_title = title if title else adm_type.capitalize()
    
    # Convert any figures to includegraphics with proper justification reset
    content = convert_figure_to_includegraphics(content)
    
    # Format paragraphs
    content = format_paragraphs(content)
    
    latex_box = [
        f"\\begin{{tcolorbox}}[breakable,title={{{box_title}}}]",
        content.strip(),
        "\\end{tcolorbox}",
        ""  # Empty line after box
    ]
    
    return '\n'.join(latex_box)

def process(content: str) -> str:
    """Convert admonitions to tcolorboxes."""
    def replace_admonition(match: re.Match) -> str:
        block = match.group(0)
        adm_type, title, content = extract_admonition_info(block)
        if not adm_type:  # Not a valid admonition
            return block
        return convert_to_tcolorbox(adm_type, title, content)
    
    # Match admonition blocks with or without <tab> tags
    pattern = (
        r'(?:[!?]\s*){3}[-+]?\s*\w+(?:\s*"[^"]*")?\s*\n'  # Header
        r'(?:'  # Start of content alternatives
        r'(?:<tab>.*?</tab>)|'  # Either <tab> content
        r'(?:(?!(?:[!?]\s*){3}[-+]?\s*\w+)(?:(?!\n\n).)*(?:\n(?!\n).*)*)'  # Or regular content
        r')'
    )
    
    content = re.sub(pattern, replace_admonition, content, flags=re.DOTALL)
    
    # Clean up extra newlines
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    return content

def test_processor():
    """Test function with sample content."""
    test_content = '''
!!! note "Test Note with Image"
<tab>
This is a test note with an image:

\\begin{figure}[htbp]
    \\centering
    \\includegraphics[width=0.8\\textwidth]{Images/test.png}
    \\caption{This is a test image}
\\end{figure}

And some text after.
</tab>

??? warning "Another Test"
<tab>
Regular text here.
</tab>
'''
    
    processed = process(test_content)
    print("Processed content:")
    print(processed)
