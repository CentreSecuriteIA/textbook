import os
from pathlib import Path
import latex_iframes
import latex_headers    # Headers first to avoid escaping commands
import latex_unicode    # Unicode after headers
import latex_lists     # Process lists before typography
import latex_images
import latex_admonitions
import latex_typography
import latex_hyperlinks
# import latex_citations
import latex_title_page

class LatexConverter:
    def __init__(self, chapter_dir: str):
        """Initialize converter with chapter directory path."""
        self.chapter_dir = Path(chapter_dir)
        self.md_file = None
        self.metadata_file = None
        self.images_dir = None
        self.setup_paths()

    def setup_paths(self):
        """Find markdown file, metadata file and images directory."""
        md_files = list(self.chapter_dir.glob("*.md"))
        if not md_files:
            raise FileNotFoundError("No markdown file found in directory")
        self.md_file = md_files[0]

        # Find metadata file
        metadata_files = list(self.chapter_dir.glob("chapter_*_metadata.json"))
        if not metadata_files:
            raise FileNotFoundError("No metadata file found in directory")
        self.metadata_file = metadata_files[0]

        self.images_dir = self.chapter_dir / "Images"
        if not self.images_dir.exists():
            raise FileNotFoundError("Images directory not found")

    def read_content(self):
        """Read markdown content from file."""
        with open(self.md_file, 'r', encoding='utf-8') as f:
            return f.read()

    def convert(self):
        """Main conversion pipeline."""
        content = self.read_content()
        output_dir = self.chapter_dir / "latex_output"
        output_dir.mkdir(exist_ok=True)

        # Generate title page first
        convert_title.process(self.metadata_file, output_dir)

        # Content processing pipeline
        # content = convert_citations.process(content, output_dir)
        content = convert_iframes.process(content)
        content = convert_headers.process(content, self.metadata_file)    # Headers before Unicode
        content = convert_unicode.process(content)    # Unicode after headers
        content = convert_lists.process(content)     # Process lists
        content = convert_images.process(content, self.images_dir)
        content = convert_admonitions.process(content)
        content = convert_typography.process(content)
        content = convert_hyperlinks.process(content)

        self.write_output(content)

    def write_output(self, content: str):
        """Write LaTeX output file."""
        output_dir = self.chapter_dir / "latex_output"
        output_dir.mkdir(exist_ok=True)
        with open(output_dir / "chapter.tex", 'w', encoding='utf-8') as f:
            f.write(content)

def main():
    converter = LatexConverter("ch4")
    converter.convert()

if __name__ == "__main__":
    main()
