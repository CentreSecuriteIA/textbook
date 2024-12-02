# File: scripts/generate_pages.py

import os
import yaml
import re

def clean_title(title):
    return re.sub(r'\s+\{.*\}$', '', title).strip()

def get_full_chapter_title(docs_path, chapter_number):
    full_chapters_dir = os.path.join(docs_path, 'chapters', 'Full Chapters')
    for filename in os.listdir(full_chapters_dir):
        if filename.startswith(f"Chapter {chapter_number.zfill(2)} -"):
            return filename.replace(f"Chapter {chapter_number.zfill(2)} - ", "").replace(".md", "")
    return None

def generate_chapter_pages_yml(docs_path, chapter_path):
    chapter_number = os.path.basename(chapter_path)
    files = [f for f in os.listdir(chapter_path) if f.endswith('.md')]
    
    pages = []
    # First add README.md/Introduction if it exists
    if 'README.md' in files:
        pages.append({'Introduction': 'README.md'})
        files.remove('README.md')
    
    # Then add the rest of the files in sorted order
    sorted_files = sorted(files)
    for file in sorted_files:
        with open(os.path.join(chapter_path, file), 'r') as f:
            first_line = f.readline().strip()
        title = clean_title(first_line.lstrip('#').strip())
        pages.append({title: file})

    chapter_title = get_full_chapter_title(docs_path, chapter_number)
    if not chapter_title:
        with open(os.path.join(chapter_path, 'README.md'), 'r') as f:
            chapter_title = clean_title(f.readline().strip().lstrip('#').strip())
    
    content = {
        'title': f'{chapter_number} - {chapter_title}',
        'nav': pages
    }

    with open(os.path.join(chapter_path, '.pages.yml'), 'w') as f:
        yaml.dump(content, f, default_flow_style=False)

def generate_main_chapters_pages_yml(chapters_path):
    content = {
        'nav': [
            'index.md',
            '...'
        ]
    }

    with open(os.path.join(chapters_path, '.pages.yml'), 'w') as f:
        yaml.dump(content, f, default_flow_style=False)

def generate_root_pages_yml(docs_path):
    content = {
        'nav': [
            {'Home': 'index.md'},
            {'Chapters': [
                'chapters/index.md',
                '...'
            ]},
            {'Courses': 'courses.md'}
        ]
    }

    with open(os.path.join(docs_path, '.pages.yml'), 'w') as f:
        yaml.dump(content, f, default_flow_style=False)

def generate_all_pages_yml(docs_path):
    chapters_path = os.path.join(docs_path, 'chapters')
    
    generate_root_pages_yml(docs_path)
    generate_main_chapters_pages_yml(chapters_path)
    
    for chapter in os.listdir(chapters_path):
        chapter_path = os.path.join(chapters_path, chapter)
        if os.path.isdir(chapter_path) and chapter.isdigit():
            generate_chapter_pages_yml(docs_path, chapter_path)

if __name__ == "__main__":
    docs_path = "/home/markov/git/textbook/docs"
    generate_all_pages_yml(docs_path)

