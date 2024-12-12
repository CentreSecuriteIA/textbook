import logging
import re
from pathlib import Path
from process_metadata import process_metadata, write_metadata_yaml
from process_links import process_links, format_links_for_readme

logger = logging.getLogger(__name__)

def format_metadata_values(metadata, reading_time):
    """Prepare metadata values for template injection."""
    # Format authors and affiliations as HTML divs
    authors_html = "".join(f'<div>{author}</div>' for author in metadata.get('authors', []))
    affiliations_html = "".join(f'<div>{aff}</div>' for aff in metadata.get('affiliations', []))
    
    # Format acknowledgements as comma-separated string
    acknowledgements_html = ", ".join(metadata.get('acknowledgements', []))
    
    # Filter and format links
    links = [link for link in metadata.get('links', []) 
            if link['type'] in ['alignment_forum', 'google_docs']]
    links_html = " · ".join(f'<a href="{link["url"]}" class="meta-link">{link["name"]}</a>' 
                           for link in links) if links else ""

    return {
        "authors": authors_html,
        "affiliations": affiliations_html,
        "acknowledgements": acknowledgements_html,
        "date": metadata.get('date', ''),
        "reading_time": reading_time,
        "links": links_html
    }

def inject_values_into_template(template, values):
    """Inject values into template by replacing placeholders."""
    content = template
    for key, value in values.items():
        placeholder = "{" + key + "}"
        content = content.replace(placeholder, str(value))
    return content

def create_chapter_readme(content, chapter_path):
    """Create README.md in a systematic, step-by-step manner."""
    try:
        logger.debug("Starting README creation")
        readme_parts = []
        remaining_content = content

        # 1. Extract and add chapter title
        title_match = re.match(r'#\s*Chapter\s*(\d+)\s*-\s*(.+)', remaining_content)
        if title_match:
            chapter_num, title = title_match.groups()
            readme_parts.append(f"# {title.strip()}")
            remaining_content = re.sub(r'^#.*\n', '', remaining_content, 1)
            logger.debug(f"Found chapter title: Chapter {chapter_num} - {title}")
        
        # 2. Handle metadata if present
        metadata, remaining_content = process_metadata(remaining_content)
        if metadata:
            # Write .meta.yml file
            write_metadata_yaml(metadata, chapter_path / ".meta.yml")
            logger.debug("Processed metadata")
            
            try:
                # Read template
                template_path = Path("templates/chapter_meta.html")
                with open(template_path, 'r', encoding='utf-8') as f:
                    template_content = f.read()
                
                # Calculate reading time
                word_count = len(remaining_content.split())
                reading_time = max(1, round(word_count / 200))
                
                # Format values and inject into template
                meta_values = format_metadata_values(metadata, reading_time)
                meta_html = inject_values_into_template(template_content, meta_values)
                
                readme_parts.append('<div class="chapter-meta">')
                readme_parts.append(meta_html)
                readme_parts.append('</div>')
                
            except FileNotFoundError:
                logger.warning("Template file not found: templates/chapter_meta.html")
            except Exception as e:
                logger.error(f"Error processing template: {e}")
                raise

        # 3. Handle links if present
        links, remaining_content = process_links(remaining_content)
        if links:
            formatted_links = format_links_for_readme(links)
            if formatted_links:
                readme_parts.append(formatted_links)
            logger.debug("Processed links")

        # 4. Remove table of contents
        parts = re.split(r'#\s*Table of Contents.*?\n(?=# )', remaining_content, flags=re.DOTALL, maxsplit=1)
        if len(parts) > 1:
            logger.debug("Found and removed table of contents")
            remaining_content = parts[1]
        else:
            logger.warning("No table of contents found")
            
        # 5. Find and extract the first section
        first_section_match = re.match(r'(# [^\n]+\n.*?)(?=\n# |$)', remaining_content, re.DOTALL)
        if first_section_match:
            first_section = first_section_match.group(1).strip()
            logger.debug(f"Found first section: {first_section[:50]}...")
            readme_parts.append(first_section)
            
            # Remove the first section from remaining content
            remaining_content = re.sub(re.escape(first_section), '', remaining_content, 1).strip()
            logger.debug("Removed first section from remaining content")
        else:
            logger.warning("No first section found")

        # 6. Write complete README
        readme_content = '\n\n'.join(part.strip() for part in readme_parts if part.strip())
        with open(chapter_path / "README.md", 'w', encoding='utf-8') as f:
            f.write(readme_content)

        logger.info(f"Created README.md in {chapter_path}")
        return remaining_content.strip()

    except Exception as e:
        logger.error(f"Error creating README: {e}")
        return content
