# File: scripts/mkdocs_videos.py

import re
import json
import logging
from pathlib import Path
from typing import Optional, Match

logger = logging.getLogger(__name__)

def get_chapter_number(chapter_dir: Path) -> int:
    """Get chapter number from metadata json."""
    json_files = list(chapter_dir.glob("chapter_*_metadata.json"))
    if not json_files:
        raise FileNotFoundError(f"No metadata JSON file found in {chapter_dir}")
    
    with open(json_files[0], 'r', encoding='utf-8') as f:
        metadata = json.load(f)
    
    return metadata.get('chapter_number', 0)

def extract_video_id(url: str) -> Optional[str]:
    """Extract YouTube video ID from URL."""
    if 'youtube.com/watch?v=' in url:
        return url.split('watch?v=')[1].split('&')[0]
    elif 'youtu.be/' in url:
        return url.split('youtu.be/')[1].split('?')[0]
    return None

def process_video_embed(match: Match, chapter_number: int, video_count: int) -> str:
    """Process a single video embed match."""
    youtube_url = match.group(1) or match.group(2)
    caption = match.group(3).strip()
    
    # Clean up the URL if it's in markdown format
    if '[' in youtube_url:
        url_match = re.match(r'\[(https?://[^\]]+)\]', youtube_url)
        if url_match:
            youtube_url = url_match.group(1)
    
    video_id = extract_video_id(youtube_url)
    if not video_id:
        logger.warning(f"Invalid YouTube URL format: {youtube_url}")
        return match.group(0)
    
    embed_url = f"https://www.youtube.com/embed/{video_id}"
    
    figure_html = f'''<figure class="video-figure" markdown="span">
<iframe style="width: 100%; aspect-ratio: 16 / 9;" frameborder="0" allowfullscreen src="{embed_url}"></iframe>
  <figcaption markdown="1"><b>Video {chapter_number}.{video_count}:</b> {caption}</figcaption>
</figure>'''
    
    return figure_html

def process(content: str, chapter_dir: Path) -> str:
    """
    Convert YouTube embed tags to iframe format with captions.
    
    Example:
    <embed-youtube>[https://youtube.com/watch?v=xxxxx]()</embed-youtube>
    <caption-video>A description of the video</caption-video>
    
    Also supports youtu.be links and various markdown link formats.
    """
    # Get chapter number from metadata
    chapter_number = get_chapter_number(chapter_dir)
    
    # Pattern matches video embed with caption
    pattern = r'<embed-youtube>\s*(?:\[(https?://[^\]]+)\](?:\([^\)]*\))?\s*|(\bhttps?://\S+))\s*(?:</embed-youtube>)?\s*<caption-video>\s*(.*?)\s*</caption-video>'
    
    # Keep track of video count
    video_count = 1
    
    def replacement(match: Match) -> str:
        nonlocal video_count
        result = process_video_embed(match, chapter_number, video_count)
        video_count += 1
        return result
    
    # Process all video instances
    processed_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    logger.info(f"Processed {video_count - 1} video embeds")
    return processed_content

def test_processor():
    """Test function with sample content."""
    test_dir = Path("test_chapter")
    test_dir.mkdir(exist_ok=True)
    
    metadata = {
        "chapter_number": 2,
        "chapter_title": "Test Chapter"
    }
    
    with open(test_dir / "chapter_2_metadata.json", 'w') as f:
        json.dump(metadata, f)
    
    test_content = '''# Chapter 2 - Test Chapter

Here's a video:

<embed-youtube>
[https://www.youtube.com/watch?v=dQw4w9WgXcQ]()
</embed-youtube>
<caption-video>First test video</caption-video>

And another:

<embed-youtube>
https://youtu.be/dQw4w9WgXcQ
</embed-youtube>
<caption-video>Second video with *markdown* and **formatting**</caption-video>
'''
    
    processed = process(test_content, test_dir)
    print("\nProcessed content:")
    print(processed)
    print("\nNote: Check that videos are numbered 2.1, 2.2, etc.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    test_processor()
