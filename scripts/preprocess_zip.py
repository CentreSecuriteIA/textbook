import os
import re
import shutil
import zipfile
from pathlib import Path
from typing import Optional, Tuple, NamedTuple

class ProcessedPaths(NamedTuple):
    """Store all relevant paths for processed chapter"""
    chapter_dir: Path
    input_file: Path
    output_file: Path
    latex_dir: Path

def extract_chapter_info(content: str) -> Tuple[str, str]:
    """Extract chapter number and title from content."""
    pattern = r'^#\s*Chapter\s*(\d+)\s*[-–—]\s*(.+?)(?:\s*{.*})?$'
    match = re.match(pattern, content.split('\n')[0].strip())
    if not match:
        raise ValueError("Could not extract chapter info from first line")
    return match.group(1), match.group(2).strip()

def create_chapter_dir(base_dir: Path, chapter_num: str) -> Path:
    """Create and return path to chapter directory with zero-padded number."""
    dir_name = f"{int(chapter_num):02d}"
    chapter_dir = base_dir / dir_name
    chapter_dir.mkdir(parents=True, exist_ok=True)
    return chapter_dir

def extract_zip(zip_path: Path, temp_dir: Path) -> None:
    """Extract zip file to temporary directory."""
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(temp_dir)

def setup_processing_dirs(script_path: Path, chapter_name: str) -> Tuple[Path, Path]:
    """Setup necessary directories and return paths to source zip and output dir."""
    base_dir = script_path.parent
    source_zips_dir = base_dir / "source_zips"
    processed_dir = base_dir / "processed"
    
    if not source_zips_dir.exists():
        raise FileNotFoundError(f"source_zips directory not found at {source_zips_dir}")
    
    zip_file = source_zips_dir / f"{chapter_name}.zip"
    if not zip_file.exists():
        raise FileNotFoundError(f"Zip file not found: {zip_file}")
        
    processed_dir.mkdir(parents=True, exist_ok=True)
    
    return zip_file, processed_dir

def process(chapter_name: str, script_path: Optional[Path] = None) -> ProcessedPaths:
    """
    Process zip file and setup directory structure.
    Returns tuple of paths needed for further processing.
    """
    if script_path is None:
        script_path = Path(__file__).parent
        
    # Setup directories and get paths
    zip_file, processed_dir = setup_processing_dirs(script_path, chapter_name)
    
    # Create temp directory for extraction
    temp_dir = processed_dir / "temp_extract"
    temp_dir.mkdir(parents=True, exist_ok=True)
    
    try:
        # Extract zip
        extract_zip(zip_file, temp_dir)
        
        # Read Output.md to get chapter info
        output_md = temp_dir / "Output.md"
        if not output_md.exists():
            raise FileNotFoundError("No Output.md found in zip file")
        
        content = output_md.read_text(encoding='utf-8')
        chapter_num, _ = extract_chapter_info(content)
        
        # Create chapter directory
        chapter_dir = create_chapter_dir(processed_dir, chapter_num)
        
        # Create subdirectories
        original_dir = chapter_dir / "original"
        original_dir.mkdir(exist_ok=True)
        latex_dir = chapter_dir / "latex_output"
        latex_dir.mkdir(exist_ok=True)
        
        # Move files to appropriate locations
        for item in temp_dir.iterdir():
            if item.name == "Output.md":
                shutil.move(str(item), str(original_dir / "Output.md"))
            else:
                dest = chapter_dir / item.name
                if dest.exists():
                    shutil.rmtree(dest) if item.is_dir() else dest.unlink()
                shutil.move(str(item), str(dest))
        
        # Define paths for preprocessor
        input_file = original_dir / "Output.md"
        output_file = chapter_dir / "Output-clean.md"
        
        return ProcessedPaths(
            chapter_dir=chapter_dir,
            input_file=input_file,
            output_file=output_file,
            latex_dir=latex_dir
        )
        
    finally:
        # Clean up temp directory
        if temp_dir.exists():
            shutil.rmtree(temp_dir)

def test_processor():
    """Test function."""
    paths = process("ch1")
    print(f"Created chapter directory: {paths.chapter_dir}")
    print(f"Input file: {paths.input_file}")
    print(f"Output file: {paths.output_file}")
    print(f"LaTeX directory: {paths.latex_dir}")

if __name__ == "__main__":
    test_processor()
