# File: scripts/00_mkdocs_parse.py

import sys
import shutil
import logging
from pathlib import Path
from typing import Optional

import mkdocs_metadata
import mkdocs_images
import mkdocs_videos
import mkdocs_iframes
import mkdocs_tabs
import mkdocs_section_numbers
import mkdocs_reading_time
import mkdocs_section_ids
import mkdocs_section_split
import mkdocs_chapter_header
import mkdocs_section_header
import mkdocs_pages
import mkdocs_cleanup




# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MkDocsParser:
    def __init__(self, chapter_name: str):
        """Initialize parser with chapter name (e.g. 'ch1', 'ch2')"""
        # Get the script's directory
        script_dir = Path(__file__).parent

        # Set up paths
        self.base_dir = script_dir.parent
        self.processed_dir = self.base_dir / "processed"

        # Find chapter directory (e.g., "01" for "ch1")
        chapter_num = chapter_name[2:]  # Extract number from "ch1"
        chapter_dir_name = f"{int(chapter_num):02d}"
        self.chapter_dir = self.processed_dir / chapter_dir_name

        if not self.chapter_dir.exists():
            raise FileNotFoundError(f"Chapter directory not found: {self.chapter_dir}")

        # Set up input/output paths
        self.input_file = self.chapter_dir / "Output-clean.md"
        if not self.input_file.exists():
            raise FileNotFoundError(
                f"Input file not found: {self.input_file}\n"
                "Make sure to run preprocess_parse.py first"
            )

        # Setup mkdocs output directory within processed chapter dir
        self.mkdocs_dir = self.chapter_dir / "mkdocs"
        self.mkdocs_dir.mkdir(parents=True, exist_ok=True)

        # Images will be copied to mkdocs directory
        self.images_dir = self.chapter_dir / "Images"
        self.mkdocs_images_dir = self.mkdocs_dir / "Images"

    def read_content(self) -> str:
        """Read content from preprocessed markdown file."""
        try:
            with open(self.input_file, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            logger.error(f"Error reading {self.input_file}: {e}")
            raise

    def copy_images(self):
        """Copy Images directory to mkdocs directory."""
        if self.images_dir.exists():
            # Remove existing Images directory in mkdocs if it exists
            if self.mkdocs_images_dir.exists():
                shutil.rmtree(self.mkdocs_images_dir)
            # Copy the entire Images directory
            shutil.copytree(self.images_dir, self.mkdocs_images_dir)
            logger.info(f"Copied Images directory to {self.mkdocs_images_dir}")
        else:
            logger.warning(f"No Images directory found at {self.images_dir}")

    def parse(self):
        """Main parsing pipeline."""
        try:

            logger.info(f"Processing {self.input_file.name}...")

            # 1. Process metadata first
            mkdocs_metadata.process(self.chapter_dir)

            # 2. Read content for processing
            content = self.read_content()

            # 3. Copy Images directory first
            self.copy_images()

            # 4. Process images + image captions
            content = mkdocs_images.process(content, self.chapter_dir)

            # 5. Process videos + video captions
            content = mkdocs_videos.process(content, self.chapter_dir)

            # 6. Process iframes + iframe captions
            content = mkdocs_iframes.process(content, self.chapter_dir)

            # 7. Process tab sections for admonitions
            content = mkdocs_tabs.process(content)

            # 8. Add chapter and section numbers
            content = mkdocs_section_numbers.process(content, self.chapter_dir)

            # 9. Calculate reading time (moved after section numbering)
            content = mkdocs_reading_time.process(content, self.chapter_dir)

            # 10. Add URL/file IDs
            content = mkdocs_section_ids.process(content)

            # 11. Split content into sections and write files
            files_content = mkdocs_section_split.process(content, self.mkdocs_dir)

            # 12. Process chapter metadata template
            mkdocs_chapter_header.process(self.chapter_dir)

            # 13. Process section metadata template
            for filename, content in files_content.items():
                if filename != "README.md":  # Skip README since it has chapter header
                    mkdocs_section_header.process(self.chapter_dir, filename, files_content)

            # 14. Generate pages and write files
            mkdocs_pages.process(files_content, self.chapter_dir)

            # 15. Final cleanup steps so that you can just copy paste
            mkdocs_cleanup.process(self.chapter_dir)

            logger.info("Done!")

        except Exception as e:
            logger.error(f"Error during parsing: {e}")
            raise

def main():
    if len(sys.argv) != 2:
        print("Usage: python mkdocs.py <chapter_name>")
        print("Example: python mkdocs.py ch5")
        sys.exit(1)

    chapter_name = sys.argv[1]
    try:
        parser = MkDocsParser(chapter_name)
        parser.parse()
    except Exception as e:
        logger.error(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
