import re
from pathlib import Path
from typing import Optional, Tuple
import convert_hyperlinks  # Import hyperlinks processor

def sanitize_caption(caption_text: str) -> str:
    """Sanitize caption text for LaTeX."""
    # First process any hyperlinks in the caption
    caption_text = convert_hyperlinks.process(caption_text)
    
    # Special LaTeX characters to escape
    special_chars = {
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '~': r'\textasciitilde{}',
        '^': r'\textasciicircum{}'
    }
    
    result = caption_text
    
    # Skip escaping characters within already processed \href commands
    parts = re.split(r'(\\href{[^}]*}{[^}]*})', result)
    processed_parts = []
    
    for i, part in enumerate(parts):
        if i % 2 == 0:  # Not inside \href
            # Escape special characters
            for char, escape in special_chars.items():
                part = part.replace(char, escape)
        processed_parts.append(part)
    
    result = ''.join(processed_parts)
    
    # Convert markdown formatting to LaTeX
    result = re.sub(r'\*\*(.*?)\*\*', r'\\textbf{\1}', result)  # Bold
    result = re.sub(r'\*(.*?)\*', r'\\textit{\1}', result)      # Italic
    
    return result.strip()

def extract_image_info(image_block: str) -> Tuple[str, str]:
    """Extract image path and caption from an image block."""
    # Extract image path
    img_pattern = r'!\[.*?\]\((.*?)\)'
    img_match = re.search(img_pattern, image_block)
    image_path = img_match.group(1) if img_match else ""

    # Extract caption
    caption_pattern = r'<caption>\s*(.*?)\s*</caption>'
    caption_match = re.search(caption_pattern, image_block, re.DOTALL)
    caption = caption_match.group(1).strip() if caption_match else ""
    
    # Sanitize the caption
    caption = sanitize_caption(caption)
    
    return image_path, caption

def convert_to_figure(image_path: str, caption: str) -> str:
    """Convert to LaTeX figure environment."""
    latex_figure = [
        "\\begin{figure}[htbp]",
        "    \\centering",
        f"    \\includegraphics[width=0.8\\textwidth]{{{image_path}}}"
    ]
    
    if caption:
        latex_figure.append(f"    \\caption{{{caption}}}")
        
    latex_figure.extend([
        "\\end{figure}",
        ""
    ])
    
    return '\n'.join(latex_figure)

def process(content: str, images_dir: Optional[Path] = None) -> str:
    """Process all images in the content."""
    def replace_image(match: re.Match) -> str:
        block = match.group(0)
        image_path, caption = extract_image_info(block)
        return convert_to_figure(image_path, caption)
    
    # Match image + caption blocks
    pattern = r'!\[.*?\]\(.*?\)\s*<caption>.*?</caption>'
    content = re.sub(pattern, replace_image, content, flags=re.DOTALL)
    
    # Clean up extra newlines
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    return content

def test_processor():
    """Test function with sample content."""
    test_content = '''
![Test image](Images/test.png)
<caption>
A caption with special characters: & % $ # _ { }
And a URL: [Click here](https://example.com)
And some **bold** and *italic* text
</caption>

![Another image](Images/test2.png)
<caption>
Multi-line caption with citations:
([Author & Coauthor, 2024](https://example.com/paper))
</caption>
'''
    
    processed = process(test_content)
    print("Processed content:")
    print(processed)
