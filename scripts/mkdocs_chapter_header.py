# File: scripts/mkdocs_chapter_header.py

import re
import json
import yaml  # Add this import
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def calculate_reading_time(chapter_dir: Path) -> str:
    """Get reading time from .reading_times.yml file."""
    reading_times_path = chapter_dir / "mkdocs" / ".reading_times.yml"
    logger.info(f"Looking for reading times at: {reading_times_path}")
    
    try:
        with open(reading_times_path, 'r', encoding='utf-8') as f:
            times = yaml.safe_load(f)
            logger.info(f"Found reading times: {times}")
            
        core_time = times.get('core', 1)
        appendix_time = times.get('appendix', 0)
        
        if appendix_time > 0:
            return f"{core_time} min (core), {appendix_time} min (appendix)"
        return f"{core_time} min (core)"
    except Exception as e:
        logger.warning(f"Could not read reading times: {e}")
        return "1 min (core)"  # Fallback

def process(chapter_dir: Path) -> None:
    """Process README.md to add chapter metadata header and action buttons."""
    # Read README.md
    readme_path = chapter_dir / "mkdocs" / "README.md"
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Get reading time
    reading_time = calculate_reading_time(chapter_dir)
    logger.info(f"Using reading time: {reading_time}")
    
    # Get metadata
    json_files = list(chapter_dir.glob("chapter_*_metadata.json"))
    if not json_files:
        raise FileNotFoundError(f"No metadata JSON file found in {chapter_dir}")
    
    with open(json_files[0], 'r', encoding='utf-8') as f:
        metadata = json.load(f)

    # Format chapter title
    chapter_number = metadata['chapter_number']
    chapter_title = metadata['chapter_title']
    chapter_header = f"# Chapter {chapter_number:02d} - {chapter_title}\n\n"
    
    # Read template
    script_dir = Path(__file__).parent
    template_path = script_dir / "templates" / "chapter_meta.html"
    
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()

    # Format values
    authors = [a.strip() for a in metadata['Authors'].split(',')]
    authors_html = " & ".join(authors)
    
    affiliations = metadata['Affiliations'].split(',')
    affiliations_html = "".join(f'<div>{aff.strip()}</div>' for aff in affiliations)
    
    acknowledgements = [a.strip() for a in metadata['Acknowledgements'].split(',')]  
    acknowledgements_html = ", ".join(acknowledgements)
    
    # Format links
    links = []
    for link in metadata.get('Also available on', []):
        if link['name'] in ['Alignment Forum', 'Google Docs']:
            links.append(
                f'<a href="{link["url"]}" class="meta-link">{link["name"]}</a>'
            )
    links_html = " · ".join(links)

    # Replace placeholders in template
    header = template.format(
        authors=authors_html,
        affiliations=affiliations_html,
        acknowledgements=acknowledgements_html,
        date=metadata.get('Last Edited', ''),
        reading_time=reading_time,
        links=links_html
    )

    # Add action buttons section with all buttons, disabled when no link
    action_buttons = """<div class="action-buttons">"""

    # Watch button
    if 'Watch' in metadata:
        action_buttons += f"""
    <a href="{metadata['Watch']}" class="action-button">
        <i class="fas fa-video"></i>
        <span>Watch</span>
    </a>"""
    else:
        action_buttons += """
    <div class="action-button disabled" data-tippy-content="Video coming soon">
        <i class="fas fa-video"></i>
        <span>Watch</span>
    </div>"""

    # Listen button (always disabled for now)
    action_buttons += """
    <div class="action-button disabled" data-tippy-content="Audio coming soon">
        <i class="fas fa-headphones"></i>
        <span>Listen</span>
    </div>"""

    # Download button (always disabled for now)
    action_buttons += """
    <div class="action-button disabled" data-tippy-content="PDF coming soon">
        <i class="fas fa-file-pdf"></i>
        <span>Download</span>
    </div>"""

    # Feedback button
    if 'Feedback' in metadata:
        action_buttons += f"""
    <a href="{metadata['Feedback']}" class="action-button">
        <i class="fas fa-comment"></i>
        <span>Feedback</span>
    </a>"""
    else:
        action_buttons += """
    <div class="action-button disabled" data-tippy-content="Feedback form coming soon">
        <i class="fas fa-comment"></i>
        <span>Feedback</span>
    </div>"""

    # Facilitate button
    if 'Facilitate' in metadata:
        action_buttons += f"""
    <a href="{metadata['Facilitate']}" class="action-button">
        <i class="fas fa-users"></i>
        <span>Facilitate</span>
    </a>"""
    else:
        action_buttons += """
    <div class="action-button disabled" data-tippy-content="Facilitation guide coming soon">
        <i class="fas fa-users"></i>
        <span>Facilitate</span>
    </div>"""

    action_buttons += "\n</div>"

    # Combine all components and ensure userStyle tag is removed
    content = re.sub(r'<userStyle>.*?</userStyle>\s*\n?', '', content, flags=re.DOTALL)
    full_content = chapter_header + header + '\n' + action_buttons + '\n\n' + content

    # Write back to README.md
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(full_content)

    logger.info(f"Added chapter header and action buttons to {readme_path}")
