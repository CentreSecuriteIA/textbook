# File: scripts/generate_readme.py

import yaml
import logging
import re
from pathlib import Path

logger = logging.getLogger(__name__)

def create_button_links(links):
    """Create button-style links for specific types of links."""
    button_config = {
        'pdf_download': ('download', 'Download'),
        'audio_version': ('headphones', 'Listen'),
        'video_version': ('video', 'Watch'),
        'facilitation_guide': ('users', 'Facilitate'),
        'feedback_form': ('message', 'Feedback')
    }
    
    buttons = []
    used_types = set()
    
    # First create buttons for existing links
    for link in links:
        link_type = link.get('type', '')
        if link_type in button_config:
            icon, text = button_config[link_type]
            button_class = " .md-button--disabled" if link.get('disabled') else ""
            buttons.append(f'[:fontawesome-solid-{icon}: {text}]({link["url"]}){{ .md-button{button_class} }}')
            used_types.add(link_type)
    
    # Then add disabled buttons for missing types
    for link_type, (icon, text) in button_config.items():
        if link_type not in used_types:
            buttons.append(f'[:fontawesome-solid-{icon}: {text}](){{ .md-button .md-button--disabled }}')
    
    return '\n'.join(buttons)

def format_metadata_html(chapter_path):
    """Read metadata from .meta.yml and format it as HTML for README.md."""
    try:
        with open(chapter_path / ".meta.yml", 'r', encoding='utf-8') as f:
            metadata = yaml.safe_load(f)
        
        # Core metadata lines - each on its own line with double space at end for markdown line break
        metadata_lines = [
            f":material-account-circle: **Authors**: {', '.join(metadata.get('authors', []))}  ",
            f":material-office-building: **Affiliation**: {', '.join(metadata.get('affiliations', []))}  ",
            f":octicons-clock-24: **Last Updated**: {metadata.get('date', '')}  "
        ]
        
        # Join core metadata with newlines
        metadata_section = '\n'.join(metadata_lines)

        # Add "Also available on" section if there are regular links
        regular_links = [
            link for link in metadata.get('links', []) 
            if link.get('type') not in [
                'pdf_download', 
                'audio_version', 
                'video_version', 
                'facilitation_guide', 
                'feedback_form', 
                'ai_safety_atlas'
            ]
        ]
                        
        if regular_links:
            # Add the "Also available on" line directly to metadata_section
            metadata_section += f"\n:material-link-variant: **Also available on**:  "
            
            # Format each link with appropriate icon - note the : is inside the []
            links_formatted = [
                f'[:material-{get_link_icon(link.get("type", ""), link["url"])}: {link["name"]}]({link["url"]})'
                for link in regular_links
            ]
            
            metadata_section += '\n' + ' · '.join(links_formatted)

        # Add action buttons with single newline
        button_links = create_button_links(metadata.get('links', []))
        metadata_section += f"\n\n{button_links}"
            
        return metadata_section
    except Exception as e:
        logger.error(f"Error formatting metadata HTML: {e}")
        return ""

def get_link_icon(link_type, url):
    """Determine appropriate icon based on link type or URL."""
    icon_mapping = {
        'forum': 'forum',              # Alignment Forum, LessWrong
        'alignmentforum': 'forum',
        'lesswrong': 'forum',
        'docs.google': 'google',       # Google Docs
        'github': 'github',            # GitHub
        'medium': 'medium',            # Medium
        'arxiv': 'file-pdf',          # ArXiv
        'youtube': 'video',            # YouTube
        'twitter': 'twitter',          # Twitter
        'linkedin': 'linkedin'         # LinkedIn
    }
    
    for domain, icon in icon_mapping.items():
        if domain in url.lower():
            return f'{icon}'  # Removed the 'material-' prefix since we'll add it in the link formatting
    
    return 'link'  # Default icon without prefix


def create_readme(content, chapter_path):
    """Create README content, write it to README.md, and update Output.md."""
    try:
        # Extract introduction section from content
        intro_match = re.search(r'# Introduction\n(.*?)(?=\n# |\Z)', content, re.DOTALL)
        if not intro_match:
            logger.error("Could not find Introduction section")
            return content
            
        intro_content = intro_match.group(1).strip()

        # Get formatted metadata HTML
        metadata_section = format_metadata_html(chapter_path)

        # Combine sections with appropriate spacing
        final_readme = "\n".join([
            "# Introduction",
            "",  # Blank line after title
            metadata_section,
            "",  # Blank line before content
            intro_content
        ])

        # Write README content
        with open(chapter_path / "README.md", 'w', encoding='utf-8') as file:
            file.write(final_readme)

        logger.info(f"Created README.md in {chapter_path}")
        
        # Return the content without the introduction section
        return re.sub(r'# Introduction\n.*?(?=\n# |\Z)', '', content, flags=re.DOTALL)

    except Exception as e:
        logger.error(f"Error creating README: {e}")
        return content  # Return original content in case of error
