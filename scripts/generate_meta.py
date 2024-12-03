# File: scripts/generate_meta.py

import re
import yaml
import logging
from pathlib import Path
from datetime import datetime

logger = logging.getLogger(__name__)

def parse_authors(author_line):
    """Parse authors from line like 'Authors: Markov Grey, Charbel-Raphael Segerie'"""
    authors = author_line.replace('Authors:', '').strip().split(',')
    return [author.strip() for author in authors]

def parse_acknowledgements(ack_line):
    """Parse acknowledgements from line like 'Acknowledgements: Person 1, Person 2'"""
    return [name.strip() for name in ack_line.replace('Acknowledgements:', '').strip().split(',')]

def parse_affiliations(affiliation_line):
    """Parse affiliations, handling markdown links"""
    # Remove 'Affiliations:' and extract just the organization name
    affiliation = affiliation_line.replace('Affiliations:', '').strip()
    # Handle markdown link format: [name](url)
    match = re.match(r'\[(.*?)\]\((.*?)\)', affiliation)
    if match:
        return match.group(1).strip()
    return affiliation

def parse_links(links_section):
    """Parse links section into structured format"""
    links = []
    link_mapping = {
        'PDF download': 'pdf_download',
        'Video version': 'video_version',
        'Audio version': 'audio_version',
        'Facilitation guide': 'facilitation_guide',
        'Feedback form': 'feedback_form'
    }
    
    for line in links_section:
        # Skip empty lines or the "Links:" header
        if not line.strip() or line.strip() == 'Links:':
            continue
            
        if line.strip().startswith('-'):
            # Extract link info from markdown format
            match = re.match(r'-\s*\[(.*?)\]\((.*?)\)', line.strip())
            if match:
                name = match.group(1).strip()
                url = match.group(2).strip()
                
                # Determine link type
                link_type = link_mapping.get(name, name.lower().replace(' ', '_'))
                
                links.append({
                    'name': name,
                    'url': url,
                    'type': link_type
                })
    
    # Add disabled buttons for missing types
    for button_name, button_type in link_mapping.items():
        if not any(link['type'] == button_type for link in links):
            links.append({
                'name': button_name,
                'url': '',
                'type': button_type,
                'disabled': True
            })
    
    return links

def extract_metadata(content, chapter_path):
    """Extract metadata from the chapter content."""
    try:
        # Find content between chapter title and first section
        parts = content.split('# Introduction', 1)
        if len(parts) < 2:
            logger.error("Could not find '# Introduction' section")
            return content
            
        metadata_section = parts[0]
        
        # Extract individual components using regex
        title_match = re.search(r'# Chapter (\d+) - (.+?)\n', metadata_section)
        author_match = re.search(r'Authors: (.+?)\n', metadata_section)
        affiliation_match = re.search(r'Affiliations: (.+?)\n', metadata_section)
        ack_match = re.search(r'Acknowledgements: (.+?)\n', metadata_section)
        date_match = re.search(r'Last Edited: (.+?)\n', metadata_section)
        
        # Extract description - everything after "Description:" until the next section
        description_match = re.search(r'Description: (.*?)(?=\[|\Z)', metadata_section, re.DOTALL)
        
        # Extract links section
        links_start = metadata_section.find('Links:')
        links_end = metadata_section.find('Description:') if 'Description:' in metadata_section else len(metadata_section)
        if links_start != -1:
            links_section = metadata_section[links_start:links_end].strip().split('\n')
        else:
            links_section = []
        
        if not title_match:
            logger.error("Could not find chapter title")
            return content

        # Build metadata dictionary
        metadata = {
            'title': title_match.group(2).strip(),
            'chapter_number': title_match.group(1).strip(),
            'authors': parse_authors(author_match.group(0)) if author_match else [],
            'affiliations': [parse_affiliations(affiliation_match.group(0))] if affiliation_match else [],
            'acknowledgements': parse_acknowledgements(ack_match.group(0)) if ack_match else [],
            'date': date_match.group(1).strip() if date_match else datetime.now().strftime('%Y-%m-%d'),
            'description': description_match.group(1).strip() if description_match else "",
            'links': parse_links(links_section) if links_section else [],
            'social': {
                'cards_layout': 'default'
            },
            'search': {
                'boost': 2.0
            }
        }

        # Write metadata to .meta.yml
        with open(chapter_path / ".meta.yml", 'w', encoding='utf-8') as f:
            yaml.dump(metadata, f, sort_keys=False, allow_unicode=True)
        
        logger.info(f"Created .meta.yml in {chapter_path}")
        return content

    except Exception as e:
        logger.error(f"Error extracting metadata: {e}")
        return content
