# File: scripts/mkdocs_cleanup.py

import shutil
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def process(chapter_dir: Path) -> None:
    """
    Move all content from chapter_dir/mkdocs/* to chapter_dir/mkdocs/XX/*
    where XX is the chapter number directory.
    """
    try:
        # Get chapter number from the chapter directory name
        chapter_num = chapter_dir.name
        mkdocs_dir = chapter_dir / "mkdocs"
        target_dir = mkdocs_dir / chapter_num
        
        # Create temporary directory to store files during move
        temp_dir = mkdocs_dir / "temp"
        temp_dir.mkdir(exist_ok=True)
        
        # Move all files to temporary directory first
        for item in mkdocs_dir.iterdir():
            if item != temp_dir:  # Skip the temp directory itself
                if item.is_file() or item.is_dir():
                    shutil.move(str(item), str(temp_dir / item.name))
        
        # Create the final target directory
        target_dir.mkdir(parents=True, exist_ok=True)
        
        # Move everything from temp to target
        for item in temp_dir.iterdir():
            shutil.move(str(item), str(target_dir / item.name))
            
        # Remove temporary directory
        temp_dir.rmdir()
        
        logger.info(f"Moved all content to {target_dir}")
        
    except Exception as e:
        logger.error(f"Error during cleanup: {e}")
        raise

def test_processor():
    """Test function."""
    test_dir = Path("test_chapter")
    test_dir.name = "01"  # Simulate chapter directory
    test_dir.mkdir(parents=True, exist_ok=True)
    
    # Create test files
    mkdocs_dir = test_dir / "mkdocs"
    mkdocs_dir.mkdir(parents=True, exist_ok=True)
    
    (mkdocs_dir / "test.md").touch()
    (mkdocs_dir / "Images").mkdir()
    
    process(test_dir)
    
    print(f"Contents moved to {mkdocs_dir / '01'}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    test_processor()
