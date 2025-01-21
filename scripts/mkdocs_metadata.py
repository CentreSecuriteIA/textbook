# File: scripts/mkdocs_metadata.py

import json
import yaml
from pathlib import Path
from typing import Dict, List, Any

def process_metadata_json(json_path: Path) -> Dict[str, Any]:
    """Convert chapter metadata JSON to MkDocs YAML format."""
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Process authors: split comma-separated string into list
    authors = [author.strip() for author in data['Authors'].split(',')]
    
    # Process affiliations: create list from single string
    affiliations = [data['Affiliations'].strip()]
    
    # Process acknowledgements: split comma-separated string into list
    acknowledgements = [ack.strip() for ack in data['Acknowledgements'].split(',')]
    
    # Process links
    links = []
    # Add "Also available on" links
    for link in data.get('Also available on', []):
        link_type = link['name'].lower().replace(' ', '_')
        links.append({
            'name': link['name'],
            'url': link['url'],
            'type': link_type
        })
    
    # Add other types of links if they exist
    extra_links = ['Feedback', 'Watch', 'Facilitate']
    for link_type in extra_links:
        if link_type in data:
            links.append({
                'name': link_type,
                'url': data[link_type],
                'type': link_type.lower()
            })
    
    # Build metadata dictionary in required format
    metadata = {
        'chapter_number': data['chapter_number'],
        'chapter_title': data['chapter_title'],
        'authors': authors,
        'affiliations': affiliations,
        'acknowledgements': acknowledgements,
        'date': data['Last Edited'],
        'links': links
    }
    
    return metadata

def write_metadata_yaml(metadata: Dict[str, Any], output_path: Path) -> None:
    """Write metadata dictionary to YAML file."""
    with open(output_path, 'w', encoding='utf-8') as f:
        yaml.dump(metadata, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

def process(chapter_dir: Path) -> None:
    """Main processing function to convert metadata from JSON to YAML."""
    # Find metadata JSON file
    json_path = None
    for file in chapter_dir.glob("chapter_*_metadata.json"):
        json_path = file
        break
    
    if not json_path:
        raise FileNotFoundError(f"No metadata JSON file found in {chapter_dir}")
    
    # Create mkdocs directory if it doesn't exist
    mkdocs_dir = chapter_dir / "mkdocs"
    mkdocs_dir.mkdir(exist_ok=True)
    
    # Convert and write metadata
    metadata = process_metadata_json(json_path)
    write_metadata_yaml(metadata, mkdocs_dir / ".meta.yml")

def test_processor():
    """Test function."""
    test_json = {
        "chapter_number": 1,
        "chapter_title": "Capabilities",
        "Authors": "Markov Grey, Charbel-Raphael Segerie",
        "Affiliations": "French Center for AI Safety (CeSIA)",
        "Acknowledgements": "Jeanne Salle, Charles Martinet, Vincent Corruble",
        "Last Edited": "2024-11-20",
        "Also available on": [
            {
                "name": "AI Safety Atlas",
                "url": "https://ai-safety-atlas.com/chapters/01/"
            }
        ],
        "Feedback": "https://forms.gle/Example"
    }
    
    # Write test JSON
    test_dir = Path("test_chapter")
    test_dir.mkdir(exist_ok=True)
    with open(test_dir / "chapter_1_metadata.json", 'w') as f:
        json.dump(test_json, f, indent=2)
    
    # Process it
    process(test_dir)
    
    # Print result
    with open(test_dir / "mkdocs" / ".meta.yml", 'r') as f:
        print(f.read())

if __name__ == "__main__":
    test_processor()
