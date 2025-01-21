import json
from pathlib import Path
from typing import Dict, Optional

def sanitize_latex(text: str) -> str:
    """Escape special LaTeX characters in text."""
    replacements = {
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
    
    for char, replacement in replacements.items():
        text = text.replace(char, replacement)
    return text

def format_authors(authors: str) -> str:
    """Format author list for LaTeX, assuming comma-separated authors."""
    authors = sanitize_latex(authors)
    # Split on commas and join with \and
    return ' \\and '.join(author.strip() for author in authors.split(','))

def format_affiliations(affiliations: str) -> str:
    """Format affiliations for LaTeX, assuming comma-separated affiliations."""
    affiliations = sanitize_latex(affiliations)
    # Split on commas and create a new line for each affiliation
    return ' \\\\\n'.join(affil.strip() for affil in affiliations.split(','))

def generate_title_tex(metadata: Dict, output_dir: Path) -> None:
    """Generate title.tex file from metadata dictionary."""
    # Extract required fields
    chapter_number = metadata.get('chapter_number', '')
    chapter_title = sanitize_latex(metadata.get('chapter_title', ''))
    authors = format_authors(metadata.get('Authors', ''))
    affiliations = format_affiliations(metadata.get('Affiliations', ''))
    
    # Create LaTeX content
    title_content = [
        r'\begin{titlepage}',
        r'    \centering',
        r'    {\huge\bfseries Chapter ' + str(chapter_number) + r'\\[0.4cm]}',
        r'    {\huge\bfseries ' + chapter_title + r'\\[2cm]}',
        r'    {\Large\lineskip 0.75em',
        r'    \begin{tabular}[t]{c}',
        f'    {authors}',
        r'    \end{tabular}\par}',
        r'    \vspace{1cm}',
        r'    {\large ' + affiliations + r'\\[2cm]}',
        r'    \vfill',
        r'    {\large \@date}',
        r'\end{titlepage}',
        r'',
        r'\newpage'
    ]
    
    # Write to file
    output_file = output_dir / 'title.tex'
    output_file.write_text('\n'.join(title_content), encoding='utf-8')

def process(metadata_file: Path, output_dir: Optional[Path] = None) -> None:
    """Main processing function to create title.tex from metadata.json."""
    # Read metadata
    metadata = json.loads(metadata_file.read_text(encoding='utf-8'))
    
    # Use parent directory of metadata file if no output_dir specified
    if output_dir is None:
        output_dir = metadata_file.parent
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Generate title.tex
    generate_title_tex(metadata, output_dir)

if __name__ == "__main__":
    test_processor()
