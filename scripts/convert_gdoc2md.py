import os
import re
from pathlib import Path
import shutil
import zipfile
import math
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def extract_zip(zip_path, extract_to):
    """Extract the zip file to the specified directory."""
    logger.info(f"Extracting {zip_path} to {extract_to}")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def read_markdown_content(file_path):
    """Read the contents of the markdown file."""
    logger.debug(f"Reading content from {file_path}")
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    if not content:
        logger.warning(f"File {file_path} is empty")
    return content

def get_chapter_info(content):
    """Extract the chapter number and title from the first line of the content."""
    if not content:
        logger.error("Content is empty")
        raise ValueError("The content is empty")
    
    first_line = content.split('\n', 1)[0]
    logger.debug(f"First line: {first_line}")
    
    chapter_info = re.match(r'#\s*Chapter\s*(\d+)\s*-\s*(.+)', first_line)
    if chapter_info:
        chapter_number = chapter_info.group(1)
        chapter_title = chapter_info.group(2).strip()
        logger.debug(f"Extracted chapter number: {chapter_number}, title: {chapter_title}")
        return chapter_number, chapter_title
    else:
        logger.error(f"Could not extract chapter info from: {first_line}")
        raise ValueError("The first line of the document does not match the expected format '# Chapter X - Title'")

def remove_table_of_contents(content):
    """Remove the table of contents from the markdown content."""
    logger.debug("Removing table of contents")
    # Find the start of the table of contents
    toc_start = content.find('[')
    if toc_start == -1:
        logger.debug("No table of contents found")
        return content  # No table of contents found

    # Find the end of the table of contents
    toc_end = content.find('\n# ', toc_start)
    if toc_end == -1:
        toc_end = content.find('\n## ', toc_start)
    if toc_end == -1:
        logger.warning("Couldn't find the end of the table of contents")
        return content  # Couldn't find the end of the table of contents

    # Remove the table of contents
    logger.debug(f"Removing TOC from index {toc_start} to {toc_end}")
    return content[:toc_start] + content[toc_end:]

def get_overview(content):
    """Extract the overview section."""
    logger.debug("Extracting overview section")
    overview_pattern = re.compile(r'#\s*Overview(.*?)(?=\n#\s|$)', re.DOTALL)
    match = overview_pattern.search(content)
    if match:
        return match.group(1).strip()
    logger.warning("No overview section found")
    return ""

def remove_overview(content):
    """Remove the overview section from the content."""
    logger.debug("Removing overview section")
    return re.sub(r'(?s)#\s*Overview.*?(?=\n#\s|$)', '', content, count=1)

def add_section_numbers(content, chapter_number):
    """Add section numbers to headers."""
    logger.debug("Adding section numbers")
    lines = content.split('\n')
    numbered_lines = []
    section_counters = [0, 0, 0]  # For h1, h2, h3

    for line in lines:
        if line.startswith('# Chapter'):
            numbered_lines.append(f"# Chapter {chapter_number} {line[9:]}")
        elif line.startswith('# '):
            section_counters[0] += 1
            section_counters[1] = 0
            section_counters[2] = 0
            numbered_lines.append(f"# {chapter_number}.{section_counters[0]} {line[2:]}")
        elif line.startswith('## '):
            section_counters[1] += 1
            section_counters[2] = 0
            numbered_lines.append(f"## {chapter_number}.{section_counters[0]}.{section_counters[1]} {line[3:]}")
        elif line.startswith('### '):
            section_counters[2] += 1
            numbered_lines.append(f"### {chapter_number}.{section_counters[0]}.{section_counters[1]}.{section_counters[2]} {line[4:]}")
        else:
            numbered_lines.append(line)

    return '\n'.join(numbered_lines)

def get_sections(content):
    """Split content into sections."""
    logger.debug("Splitting content into sections")
    section_pattern = re.compile(r'(?m)^(#\s+.+)$')
    sections = section_pattern.split(content)[1:]  # Skip the first empty part
    return list(zip(sections[::2], sections[1::2]))

def add_time_to_read(section):
    """Calculate and add reading time to the section, preserving subsections and admonitions."""
    words = len(section.split())
    reading_time = math.ceil(words / 200)  # Assuming 200 words per minute
    reading_time_text = f"\n⌛ Estimated Reading Time: {reading_time} minutes. ({words} words)\n\n"
    
    # Split the section into lines
    lines = section.split('\n')
    
    # Find the main header (first line starting with single #)
    header_index = next((i for i, line in enumerate(lines) if line.strip().startswith('# ')), -1)
    
    if header_index != -1:
        # Insert reading time after the main header and before any content or subsections
        return '\n'.join(lines[:header_index+1] + [reading_time_text] + lines[header_index+1:])
    else:
        # If no header found, prepend reading time to the entire section
        return reading_time_text + section

def sanitize_filename(filename):
    """Sanitize the filename by removing invalid characters and replacing spaces with hyphens."""
    return re.sub(r'[^\w\s-]', '', filename).replace(" ", '-')

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
    content = re.sub(r'<tab>(.*?)</tab>', lambda m: '\n'.join(['\t' + line for line in m.group(1).split('\n')]), content, flags=re.DOTALL)
    return content

def create_full_page(content, output_dir, chapter_number, chapter_title, snippets_dir):
    """Create a full page with the entire content of the chapter."""
    logger.info("Creating full page")
    # Add section numbers
    full_content = add_section_numbers(content, chapter_number)
    
    # Additional processing
    full_content = add_tabs(full_content)
    full_content = add_snippets(full_content, snippets_dir)
    
    # Create the full page file
    full_page_filename = f"{chapter_number}-{sanitize_filename(chapter_title)}-full.md"
    full_page_path = output_dir / full_page_filename
    
    with open(full_page_path, 'w', encoding='utf-8') as full_page_file:
        full_page_file.write(full_content)
    
    logger.info(f"Created full page file: {full_page_filename}")
    return full_page_path

def process_markdown(input_path, output_dir, snippets_dir):
    """Process the markdown file following the specified flow."""
    try:
        logger.info(f"Processing markdown from {input_path}")
        
        # Step 1: Read the full markdown content
        file_path = input_path / "Output.md"
        full_markdown = read_markdown_content(file_path)
        
        if not full_markdown:
            logger.error("The markdown content is empty")
            raise ValueError("The markdown content is empty")

        # Step 2: Get chapter info and create folder
        chapter_number, chapter_title = get_chapter_info(full_markdown)
        chapter_folder_name = f"{chapter_number} - {chapter_title}"
        chapter_path = output_dir / chapter_folder_name
        chapter_path.mkdir(parents=True, exist_ok=True)
        logger.info(f"Created chapter folder: {chapter_path}")

        # Step 3: Remove table of contents
        full_markdown = remove_table_of_contents(full_markdown)
        logger.debug("Removed table of contents")

        # Step 4: Create full page
        full_page_path = create_full_page(full_markdown, chapter_path, chapter_number, chapter_title, snippets_dir)
        logger.info(f"Created full page at {full_page_path}")

        # Step 5: Get overview and write to README.md
        overview = get_overview(full_markdown)
        with open(chapter_path / "README.md", 'w', encoding='utf-8') as readme_file:
            readme_file.write(f"# Chapter {chapter_number} - {chapter_title}\n\n{overview}")
        logger.info("Created README.md with overview")

        # Step 6: Remove overview from full_markdown
        full_markdown = remove_overview(full_markdown)

        # Step 7: Add section numbers
        full_markdown = add_section_numbers(full_markdown, chapter_number)

        # Additional processing steps
        full_markdown = add_tabs(full_markdown)
        full_markdown = add_snippets(full_markdown, snippets_dir)

        # Step 8: Get sections and create files
        sections = get_sections(full_markdown)
        for i, (header, content) in enumerate(sections, start=1):
            section_content = f"{header}\n{add_time_to_read(content.strip())}"
            sanitized_title = sanitize_filename(header.lstrip('#').strip())
            output_filename = f"{chapter_number}.{i}-{sanitized_title}.md"
            
            with open(chapter_path / output_filename, 'w', encoding='utf-8') as output_file:
                output_file.write(section_content)
            logger.info(f"Created {output_filename}")

        # Step 9: Handle images (if needed)
        images_source = input_path / "Images"
        if images_source.exists() and images_source.is_dir():
            shutil.copytree(images_source, chapter_path / "Images", dirs_exist_ok=True)
            logger.info("Copied Images folder")

        logger.info(f"Processing complete. Output files are in: {chapter_path}")
        logger.info(f"Full page file created at: {full_page_path}")

    except Exception as e:
        logger.exception(f"An error occurred: {str(e)}")
        raise

if __name__ == "__main__":
    input_path = Path("source_zips/ch8.zip")
    output_dir = Path("docs/Chapters")
    snippets_dir = Path("snippets")

    extract_to = None
    try:
        if input_path.is_file() and input_path.suffix == '.zip':
            logger.info("Extracting zip file...")
            extract_to = input_path.parent / "extracted"
            extract_zip(input_path, extract_to)
            input_path = extract_to

        process_markdown(input_path, output_dir, snippets_dir)
    except Exception as e:
        logger.error(f"An error occurred during processing: {str(e)}")
    finally:
        if extract_to and extract_to.exists():
            shutil.rmtree(extract_to)

logger.info("Don't forget to check the result of the formatting and then commit")
