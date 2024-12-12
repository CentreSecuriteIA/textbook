# File: scripts/process_tags.py

import re
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def process_all_tags(content, snippets_dir):
    """Process all supported tags in the content."""
    content = add_snippets(content, snippets_dir)
    content = add_captions(content)
    content = add_youtube_embeds(content)
    content = add_tabs(content)
    return content

def add_snippets(content, snippets_dir):
    """Replace snippet placeholders with actual content."""
    logger.debug("Adding snippets")
    snippet_pattern = re.compile(r'\{\{(.+?)\}\}')
    
    def replace_snippet(match):
        snippet_name = match.group(1).strip()
        snippet_path = Path(snippets_dir) / snippet_name
        if snippet_path.exists():
            return snippet_path.read_text()
        logger.warning(f"Snippet not found: {snippet_name}")
        return match.group(0)  # Return original if snippet not found
        
    return snippet_pattern.sub(replace_snippet, content)

def add_captions(content):
    """Convert image markdown with <caption> tags to figure format."""
    # Pattern matches image followed by caption, even within list items or other content
    pattern = r'(!\[.*?\]\(.*?\))\s*<caption>\s*(.*?)\s*</caption>'
    
    # Keep track of figure count
    figure_count = 1
    
    def replacement(match):
        nonlocal figure_count
        image_markdown = match.group(1)
        caption = match.group(2).strip()
        
        # Create figure with numbered caption
        figure_html = f'''<figure markdown="span">
{image_markdown}{{ loading=lazy }}
  <figcaption markdown="1"><b>Figure {figure_count}:</b> {caption}</figcaption>
</figure>'''
        
        figure_count += 1
        return figure_html
    
    return re.sub(pattern, replacement, content, flags=re.DOTALL)

def add_youtube_embeds(content):
    """Convert YouTube embed tags to iframe format."""
    # Updated pattern to handle both markdown links and direct URLs
    pattern = r'<embed-youtube>\s*(?:\[(https?://[^\]]+)\](?:\([^\)]*\))?\s*|(\bhttps?://\S+))\s*</embed-youtube>'
    
    def replacement(match):
        # Get URL from either the markdown link or direct URL
        youtube_url = match.group(1) or match.group(2)
        if not youtube_url:
            logger.warning("Could not extract YouTube URL")
            return match.group(0)
            
        # Convert regular YouTube URLs to embed URLs
        if 'youtube.com/watch?v=' in youtube_url:
            video_id = youtube_url.split('watch?v=')[1].split('&')[0]
        elif 'youtu.be/' in youtube_url:
            video_id = youtube_url.split('youtu.be/')[1].split('?')[0]
        else:
            logger.warning(f"Invalid YouTube URL format: {youtube_url}")
            return match.group(0)
            
        embed_url = f"https://www.youtube.com/embed/{video_id}"
        return f'<iframe style="width: 100%; aspect-ratio: 16 / 9;" frameborder="0" allowfullscreen src="{embed_url}"></iframe>'
    
    # Process all YouTube embed tags
    return re.sub(pattern, replacement, content, flags=re.MULTILINE | re.DOTALL)

def add_tabs(content):
    """Replace $$$ with spaces and apply tab sections."""
    logger.debug("Adding tabs")
    content = content.replace("$$$$", "    ")
    
    def process_tab_content(tab_content):
        # Indent all lines
        lines = tab_content.split('\n')
        indented_lines = []
        for line in lines:
            # Skip indenting empty lines
            if line.strip():
                indented_lines.append('    ' + line)
            else:
                indented_lines.append(line)
        return '\n'.join(indented_lines)

    pattern = r'<tab>(.*?)</tab>'
    content = re.sub(pattern, 
                    lambda m: process_tab_content(m.group(1)), 
                    content, 
                    flags=re.DOTALL)
    
    return content
