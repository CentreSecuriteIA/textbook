"""
If you update a chapter on gdoc, use this script to update the website

0. Check that you have commited the last version beforehand
1. Use the extension "Doc to Markdown pro" on gdoc, convert the page to a zipped markdown
2. Unzip the zip
3. Delete the last version of the chapter
4. Copy the new version to the Chapter folder, and modify the title to be something like "1-Capability"




"""
import os
import re
from pathlib import Path
import shutil

def sanitize_filename(filename):
    # Remove invalid characters for filenames
    filename = re.sub(r'[\\/*?:"<>|]', "", filename)
    filename = filename.replace(" ", '-')
    return filename


def process(body:str):
    body = body.replace("TAB ", "\t") # it's no longer necessary
    return body 

def split_markdown(folder_source, chapter):
    """Update the chapter with the folder source.
    
    /folder_source:
        Images/ imag_1.png
                imag_2.png
                ...
        Output.md --> very long markdown that contains the chapter
    
        
    We want to update the chapter

    Chapters/
        1-Capabilities
            Images <- a copy of the Image folder
            1-title.md <- section 1 of Output.md
            2-title.md
            ...
    """

    folder_source = Path(folder_source)

    # Augment the source folder by creating a md per section
    file_path = folder_source / "Output.md"
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    sections = content.split('\n# ')
    # assert len(sections[0]) < 40 , "Error: everything should be written inside subsection '# '"
    for i, section in enumerate(sections[1:]):
        title, body = section.split('\n', 1)
        body = process(body)
        sanitized_title = sanitize_filename(title)
        output_filename = f"{i}-{sanitized_title}.md"

        if "0" in output_filename:
            output_filename = "README.md"

        with open(folder_source / output_filename, 'w', encoding='utf-8') as output_file:
            output_file.write(f"# {title}\n{body}")
        print(f"Created {output_filename}.")


    # delete old chapter
    chapter_path= Path("docs/Chapters") / chapter
    shutil.copytree(folder_source, chapter_path, dirs_exist_ok=True)
    os.remove(chapter_path / "Output.md")


split_markdown(
    folder_source='/Users/raph/Downloads/Chapter 1 - Capabilities - [Commentable]_24-05-2024_18_22_42',
    chapter = "1-Capabilities"
)
print("Don't forget to check the result of the formating and then commit")
