import re
import json
from pathlib import Path
from typing import Dict, List, Tuple, Optional

def remove_style_tags(content: str) -> str:
    """Remove userStyle tags and similar."""
    return re.sub(r'<userStyle>.*?</userStyle>\s*', '', content, flags=re.DOTALL)

def get_chapter_number(metadata_file: Optional[Path]) -> int:
    """Get chapter number from metadata file."""
    if not metadata_file:
        return 1
    try:
        metadata = json.loads(metadata_file.read_text(encoding='utf-8'))
        return metadata.get('chapter_number', 1)
    except (json.JSONDecodeError, FileNotFoundError):
        return 1

def convert_headers(content: str, chapter_num: int = 1) -> str:
    """Convert markdown headers to LaTeX sections.
    Promotes all headers up one level since chapter title is handled separately.
    Prefixes section numbers with chapter number."""
    def process_header_line(match: re.Match) -> str:
        level = len(match.group(1))  # Number of #
        title = match.group(2).strip()
        
        # Promote everything up one level since chapter title is handled separately
        if level == 1:  
            return f'\\section{{{title}}}'
        elif level == 2:
            return f'\\subsection{{{title}}}'
        elif level == 3:
            return f'\\subsubsection{{{title}}}'
        elif level == 4:
            return f'\\paragraph{{{title}}}'
        return match.group(0)

    # Configure section numbering to include chapter number
    content = f"""\\renewcommand\\thesection{{{chapter_num}.\\arabic{{section}}}}
\\renewcommand\\thefigure{{{chapter_num}.\\arabic{{figure}}}}
\\renewcommand\\thetable{{{chapter_num}.\\arabic{{table}}}}
\\renewcommand\\theequation{{{chapter_num}.\\arabic{{equation}}}}
\\setcounter{{section}}{{0}}
\\setcounter{{figure}}{{0}}
\\setcounter{{table}}{{0}}
\\setcounter{{equation}}{{0}}\n\n""" + content

    # Only match actual markdown headers
    pattern = r'^(#+)\s+(.+?)(?:\s*#*)?$'
    return re.sub(pattern, process_header_line, content, flags=re.MULTILINE)

def process(content: str, metadata_file: Optional[Path] = None) -> str:
    """Main processing function to convert headers."""
    content = remove_style_tags(content)
    chapter_num = get_chapter_number(metadata_file)
    content = convert_headers(content, chapter_num)
    content = re.sub(r'\n{3,}', '\n\n', content)
    return content
