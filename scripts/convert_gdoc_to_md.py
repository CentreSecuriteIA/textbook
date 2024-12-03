# File: scripts/convert_gdoc_to_md.py

import os
import re
import zipfile
from pathlib import Path
import shutil
import logging
import yaml
import generate_pages
from generate_meta import extract_metadata
from generate_readme import create_readme


# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def extract_zip(zip_path, output_dir):
    """Extract the zip file to a temporary directory within the specified output directory."""
    temp_dir = Path(output_dir) / "temp_extract"
    temp_dir.mkdir(parents=True, exist_ok=True)
    
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
        return temp_dir
    except Exception as e:
        logger.error(f"Error extracting zip file: {e}")
        shutil.rmtree(temp_dir)
        raise

def create_chapter_folder(temp_dir, output_dir):
    """Create chapter folder based on Output.md content, extract chapter info, and move files."""
    output_md_path = temp_dir / "Output.md"
    with open(output_md_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Extract chapter info
    match = re.match(r'#\s*Chapter\s*(\d+)\s*-\s*(.+)', content.split('\n', 1)[0])
    if not match:
        raise ValueError("Could not extract chapter info from the first line")
    
    chapter_number, chapter_title = match.group(1), match.group(2).strip()
    
    chapter_folder_name = chapter_number.zfill(2)
    chapter_path = Path(output_dir) / chapter_folder_name
    chapter_path.mkdir(parents=True, exist_ok=True)
    
    # Move Output.md and Images folder to chapter folder
    shutil.move(str(output_md_path), str(chapter_path / "Output.md"))
    images_folder = temp_dir / "Images"
    if images_folder.exists():
        # Remove existing Images directory if it exists
        images_dest = chapter_path / "Images"
        if images_dest.exists():
            shutil.rmtree(images_dest)
        shutil.move(str(images_folder), str(images_dest))
    
    return chapter_path, content, chapter_number, chapter_title

def add_snippets(content, snippets_dir):
    """Replace snippet placeholders with actual content."""
    logger.debug("Adding snippets")
    snippet_pattern = re.compile(r'\{\{(.+?)\}\}')
    def replace_snippet(match):
        snippet_name = match.group(1).strip()
        snippet_path = os.path.join(snippets_dir, snippet_name)
        if os.path.exists(snippet_path):
            with open(snippet_path, 'r') as snippet_file:
                return snippet_file.read()
        logger.warning(f"Snippet not found: {snippet_name}")
        return match.group(0)  # Return original if snippet not found
    return snippet_pattern.sub(replace_snippet, content)

def add_tabs(content):
    """Replace $$$ with spaces and apply tab sections."""
    logger.debug("Adding tabs")
    content = content.replace("$$$$", "    ")
    content = re.sub(r'<tab>(.*?)</tab>', lambda m: '\n'.join(['    ' + line for line in m.group(1).split('\n')]), content, flags=re.DOTALL)
    return content

def add_section_numbers(content, chapter_number, chapter_path):
    """Add section numbers to headers and write the numbered content to Output.md."""
    lines = content.split('\n')
    numbered_lines = []
    section_counters = [0, 0, 0]  # For h1, h2, h3
    for line in lines:
        if line.startswith('# '):
            section_counters[0] += 1
            section_counters[1] = 0
            section_counters[2] = 0
            numbered_lines.append(f"# {chapter_number}.{section_counters[0]} {line[2:]} {{: #{str(section_counters[0]).zfill(2)} }}")
        elif line.startswith('## '):
            section_counters[1] += 1
            section_counters[2] = 0
            numbered_lines.append(f"## {chapter_number}.{section_counters[0]}.{section_counters[1]} {line[3:]} {{: #{str(section_counters[1]).zfill(2)} }}")
        elif line.startswith('### '):
            section_counters[2] += 1
            numbered_lines.append(f"### {chapter_number}.{section_counters[0]}.{section_counters[1]}.{section_counters[2]} {line[4:]} {{: #{str(section_counters[2]).zfill(2)} }}")
        else:
            numbered_lines.append(line)

    numbered_content = '\n'.join(numbered_lines)

    # Write numbered content to Output.md
    with open(chapter_path / "Output.md", 'w', encoding='utf-8') as file:
        file.write(numbered_content)

    return numbered_content

def split_into_section_files(content, chapter_path, chapter_number):
    """Split the content into individual section files with simplified naming and add reading time."""
    sections = re.split(r'\n(?=# \d+\.\d+)', content)
    logger.info(f"Found {len(sections)} sections")
    for i, section in enumerate(sections, 1):
        if section.strip():
            # Extract section number and title
            match = re.match(r'# (\d+)\.(\d+)\s+(.+?)(?:\s+\{.*\})?$', section.split('\n', 1)[0])
            if match:
                _, section_num, _ = match.groups()
                section_num_padded = f"{int(section_num):02d}"
                filename = f"{section_num_padded}.md"
                filepath = chapter_path / filename

                # Add reading time
                section_with_reading_time = add_reading_time(section.strip())

                filepath.write_text(section_with_reading_time, encoding='utf-8')
                logger.info(f"Created file: {filename}")
            else:
                logger.warning(f"Could not extract section number and title for section {i}")
        else:
            logger.warning(f"Empty section found at position {i}")

def add_reading_time(content):
    """Calculate reading time and add it after the main title/header using an MkDocs note admonition."""
    word_count = len(content.split())
    minutes = max(1, round(word_count / 200))

    admonition = f"""!!! note "Reading Time: {minutes} minutes" """

    header_end = content.find('\n', content.find('#'))
    if header_end == -1:
        return f"{admonition}\n{content}"
    else:
        return f"{content[:header_end]}\n{admonition}{content[header_end:]}"

def finalize_chapter(chapter_path, content, chapter_title):
    """Add chapter name as title, rename output file, and move it to ../Full Chapters/."""
    # Add chapter name as title element
    title_element = f"# Chapter {chapter_path.name} - {chapter_title}\n\n"
    final_content = title_element + content

    # Create the "Full Chapters" directory if it doesn't exist
    full_chapters_dir = chapter_path.parent / "Full Chapters"
    full_chapters_dir.mkdir(exist_ok=True)

    # Rename and move the file
    new_filename = f"Chapter {chapter_path.name} - {chapter_title}.md"
    new_file_path = full_chapters_dir / new_filename

    with open(new_file_path, 'w', encoding='utf-8') as file:
        file.write(final_content)

    # Remove the original Output.md
    (chapter_path / "Output.md").unlink()

    logger.info(f"Finalized chapter: {new_file_path}")

def process_markdown(input_zip, output_dir, snippets_dir):
    """Process markdown from zip file and create chapter folder with processed content and section files."""
    try:
        # Extract zip
        temp_dir = extract_zip(input_zip, output_dir)

        # Create chapter folder and get content
        chapter_path, content, chapter_number, chapter_title = create_chapter_folder(temp_dir, output_dir)

        # Process content in memory
        content = add_snippets(content, snippets_dir)
        content = add_tabs(content)
        
        # Extract metadata and create .meta.yml
        content = extract_metadata(content, chapter_path)

        # Create README and update main content
        content = create_readme(content, chapter_path)
        
        # Add section numbers and write to Output.md
        content = add_section_numbers(content, chapter_number, chapter_path)
        
        # Split content into section files
        split_into_section_files(content, chapter_path, chapter_number)
        
        # Finalize chapter
        finalize_chapter(chapter_path, content, chapter_title)

    except Exception as e:
        logger.error(f"Error processing markdown: {e}")
        raise
    finally:
        if 'temp_dir' in locals():
            shutil.rmtree(temp_dir)

if __name__ == "__main__":
    snippets_dir = "path/to/snippets/directory"
    output_dir = "docs"  # This should be the path to your docs directory
    # for chapter in ["ch1", "ch2", "ch3", "ch4", "ch5", "ch6", "ch7", "ch8", "ch9"]:
    for chapter in ["ch1"]:
        process_markdown(f"source_zips/{chapter}.zip", os.path.join(output_dir, "chapters"), snippets_dir)
    generate_pages.generate_all_pages_yml(output_dir)
