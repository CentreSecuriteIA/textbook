"""
1. If you update a chapter on gdoc, use the 

"""

import re


def sanitize_filename(filename):
    # Remove invalid characters for filenames
    filename = re.sub(r'[\\/*?:"<>|]', "", filename)
    filename = filename.replace(" ", '-')
    return filename


def process(body:str):
    body = body.replace("TAB ", "\t")
    return body 

def split_markdown(file_path):

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    sections = content.split('\n# ')

    assert len(sections[0]) < 40 , "Error: everything should be written inside subsection '# '"
    for i, section in enumerate(sections[1:]):

        
        title, body = section.split('\n', 1)

        body = process(body)
        

        sanitized_title = sanitize_filename(title)
        output_filename = f"{i}-{sanitized_title}.md"
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            output_file.write(f"# {title}\n{body}")

        print(f"Created {output_filename}")


# Example usage
split_markdown('original/1-Capabilities/Output.md')
