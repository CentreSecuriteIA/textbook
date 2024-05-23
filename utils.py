import os
import re

def sanitize_filename(filename):
    # Remove invalid characters for filenames
    filename = re.sub(r'[\\/*?:"<>|]', "", filename)
    filename = filename.replace(" ", '-')
    return filename

def split_markdown(file_path):
    if not os.path.isfile(file_path):
        print(f"File {file_path} does not exist.")
        return

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    sections = content.split('\n# ')
    if sections[0].strip() == '':
        sections = sections[1:]

    for i, section in enumerate(sections):
        section = section.strip()
        if not section:
            continue

        if i == 0:
            title, body = section.split('\n', 1)
        else:
            title = section.split('\n', 1)[0]
            body = section[len(title):].strip()

        sanitized_title = sanitize_filename(title)
        output_filename = f"{i}-{sanitized_title}.md"
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            output_file.write(f"# {title}\n{body}")

        print(f"Created {output_filename}")


# Example usage
split_markdown('docs/2-Risks/Chapter-2.md')
