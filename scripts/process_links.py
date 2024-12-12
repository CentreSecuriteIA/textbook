# File: scripts/process_links.py

import logging
import re

logger = logging.getLogger(__name__)

def process_links(content):
    """Extract and process links if present, return processed links and remaining content."""
    links_match = re.search(r'<links>\n(.*?)\n</links>', content, re.DOTALL)
    if not links_match:
        return None, content
        
    links_text = links_match.group(1)
    processed_links = parse_links(links_text)
    
    # Remove links section from content
    remaining_content = re.sub(r'<links>.*?</links>\n', '', content, re.DOTALL)
    
    return processed_links, remaining_content

def parse_links(links_text):
    """Parse links into structured format."""
    links = []
    link_matches = re.findall(r'\[(.*?)\]\((.*?)\)', links_text)
    
    for name, url in link_matches:
        name = name.strip()
        url = url.strip()
        links.append({
            'name': name,
            'url': url,
            'type': name.lower()
        })
    
    return links

def format_links_for_readme(links):
    """Format links for README file."""
    if not links:
        return ""
    return '\n'.join([f'[{link["name"]}]({link["url"]}){{ .md-button }}' for link in links])

