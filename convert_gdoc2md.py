"""
If you update a chapter on gdoc, use this script to update the website

0. Check that you have commited the last version beforehand
1. Use the extension "Doc to Markdown pro" on gdoc, convert the page to a zipped markdown
2. Unzip the zip
3. Execute the script

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


def read_file(file_path):
    """
    Read the contents of a file and return as a string.
    """
    with open(file_path, 'r') as file:
        return file.read()

def replace_occurrences(big_file:str, snippets_directory):
    """
    Replace occurrences of file names in the big file with the contents of those files.
    """
    # List all snippet files
    snippet_files = os.listdir(snippets_directory)

    # Replace occurrences of snippet file names with their contents
    for snippet_file in snippet_files:
        if snippet_file in big_file:
            print(f"{snippet_file} will be included")
            snippet_file_path = os.path.join(snippets_directory, snippet_file)
            snippet_content = read_file(snippet_file_path)
            print(snippet_content)
            big_file = big_file.replace(snippet_file, snippet_content)

    return big_file

def process(body:str):
    body = body.replace("$$$$", "    ")
    # Otherwise the parser for tab is stochastic
    body = replace_occurrences(body, "include_snippets")
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
    folder_source='/Users/raph/Downloads/Chapter 1 - Capabilities - [Commentable]_28-05-2024_13_32_29',
    chapter = "1-Capabilities",
    # Last revision
)
print("Don't forget to check the result of the formating and then commit")
