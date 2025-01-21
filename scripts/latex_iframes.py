import re
from typing import List, Tuple

def process(content: str) -> str:
    """Remove iframes, videos, and their captions, preserve regular figures."""
    
    # Remove iframe blocks and their captions
    iframe_pattern = r'<iframe.*?</iframe>\s*(?:<caption-iframe>.*?</caption-iframe>\s*)?'
    content = re.sub(iframe_pattern, '', content, flags=re.DOTALL)
    
    # Remove YouTube embeds and their captions
    youtube_pattern = r'<embed-youtube>.*?</embed-youtube>\s*(?:<caption-video>.*?</caption-video>\s*)?'
    content = re.sub(youtube_pattern, '', content, flags=re.DOTALL)
    
    # Clean up extra newlines
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    return content

def test_processor():
    """Test function with sample content."""
    test_content = '''
![Regular figure](Images/test1.png)
<caption>
Regular figure caption
</caption>

<iframe src="https://example.com"></iframe>
<caption-iframe>
Iframe caption to remove
</caption-iframe>

<embed-youtube>
[https://youtube.com/watch?v=test](null)
</embed-youtube>
<caption-video>
Video caption to remove
</caption-video>

![Another regular figure](Images/test2.png)
<caption>
Another regular figure caption
</caption>
    '''
    
    processed = process(test_content)
    print("Processed content:")
    print(processed)

if __name__ == "__main__":
    test_processor()
