# File: scripts/process_metadata.py

import yaml
import logging
import re
from pathlib import Path

logger = logging.getLogger(__name__)

def process_metadata(content):
    """Extract and process metadata if present, return processed metadata and remaining content."""
    metadata_match = re.search(r'<metadata>\n(.*?)\n</metadata>', content, re.DOTALL)
    if not metadata_match:
        return None, content
        
    metadata_text = metadata_match.group(1)
    metadata = parse_metadata(metadata_text)
    
    # Remove metadata section from content
    remaining_content = re.sub(r'<metadata>.*?</metadata>\n', '', content, re.DOTALL)
    
    return metadata, remaining_content

def parse_metadata(metadata_text):
    """Parse metadata text into structured format."""
    metadata = {
        'authors': [],
        'affiliations': [],
        'acknowledgements': [],
        'date': '',
        'links': []
    }
    
    for line in metadata_text.split('\n'):
        if ':' not in line:
            continue
            
        key, value = line.split(':', 1)
        key = key.strip()
        value = value.strip()
        
        if key == 'Authors':
            metadata['authors'] = [a.strip() for a in value.split(',') if a.strip()]
        elif key == 'Affiliations':
            metadata['affiliations'] = [value.strip()] if value.strip() else []
        elif key == 'Acknowledgements':
            metadata['acknowledgements'] = [a.strip() for a in value.split(',') if a.strip()]
        elif key == 'Last Edited':
            metadata['date'] = value
        elif key == 'Also available on':
            # Parse markdown links
            links = re.findall(r'\[(.*?)\]\((.*?)\)', value)
            metadata['links'].extend([{
                'name': name,
                'url': url,
                'type': name.lower().replace(' ', '_')
            } for name, url in links])
    
    return metadata

def write_metadata_yaml(metadata, filepath):
    """Write metadata to YAML file."""
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            yaml.dump(metadata, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
        return True
    except Exception as e:
        logger.error(f"Error writing metadata YAML: {e}")
        return False
