# preprocess_main.py
import sys
from pathlib import Path
import preprocess_zip
import preprocess_formatting
import preprocess_toc
import preprocess_comments
import preprocess_metadata
import preprocess_bibliography

class MarkdownPreprocessor:
    def __init__(self, chapter_name: str):
        """Initialize preprocessor with chapter name (e.g. 'ch1', 'ch2')"""
        # Process zip and get all necessary paths
        paths = preprocess_zip.process(chapter_name, Path(__file__).parent)
        self.chapter_dir = paths.chapter_dir
        self.input_file = paths.input_file
        self.output_file = paths.output_file
        self.latex_dir = paths.latex_dir
        
    def read_content(self) -> str:
        """Read markdown content from file."""
        try:
            with open(self.input_file, 'r', encoding='utf-8') as f:
                content = f.read()
                return content.replace('\r\n', '\n')
        except UnicodeDecodeError:
            print(f"Warning: UTF-8 decode error. Trying with 'latin-1' encoding...")
            with open(self.input_file, 'r', encoding='latin-1') as f:
                return f.read().replace('\r\n', '\n')

    def write_output(self, content: str):
        """Write cleaned markdown to output file."""
        with open(self.output_file, 'w', encoding='utf-8') as f:
            f.write(content)

    def preprocess(self):
        """Main preprocessing pipeline."""
        try:
            print(f"Processing {self.input_file.name}...")
            
            # Read content
            content = self.read_content()
            
            # Process in stages
            content = preprocess_metadata.process(content, self.latex_dir)
            content = preprocess_comments.process(content)
            content = preprocess_toc.process(content)
            content = preprocess_formatting.process(content)
            # content = preprocess_bibliography.process(content, self.latex_dir)
            
            print(f"Writing output to {self.output_file.name}")
            self.write_output(content)
            print("Done!")
            
        except Exception as e:
            print(f"Error during preprocessing: {e}")
            raise

def main():
    if len(sys.argv) != 2:
        print("Usage: python preprocess_main.py <chapter_name>")
        print("Example: python preprocess_main.py ch5")
        sys.exit(1)

    chapter_name = sys.argv[1]
    try:
        preprocessor = MarkdownPreprocessor(chapter_name)
        preprocessor.preprocess()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
