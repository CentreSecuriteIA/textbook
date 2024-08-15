import os
from pathlib import Path

def write_directory_tree(directory, file, prefix="", include_formats=None, exclude_dirs=None):
    # Get the contents of the directory
    contents = list(Path(directory).iterdir())
    
    # Sort contents (directories first, then files)
    contents.sort(key=lambda x: (not x.is_dir(), x.name.lower()))
    
    # Process each item in the directory
    for i, item in enumerate(contents):
        # Skip .git directories
        if item.name == '.git' or (exclude_dirs and item.name in exclude_dirs):
            continue
        
        # Check if the file format should be included
        if item.is_file() and include_formats and not any(item.name.endswith(fmt) for fmt in include_formats):
            continue
        
        # Determine if this is the last item at this level
        is_last = (i == len(contents) - 1)
        
        # Write the item to the file
        file.write(f"{prefix}{'└── ' if is_last else '├── '}{item.name}\n")
        
        # If it's a directory, recursively write its contents
        if item.is_dir():
            extension = "    " if is_last else "│   "
            write_directory_tree(item, file, prefix + extension, include_formats, exclude_dirs)

def generate_tree(output_file='tree', include_formats=None, exclude_dirs=None):
    # Get the current working directory
    current_dir = os.getcwd()
    
    # Open the file for writing
    with open(output_file, 'w', encoding='utf-8') as file:
        # Write the header
        file.write(f"Directory tree of: {current_dir}\n")
        
        # Write the tree
        write_directory_tree(current_dir, file, include_formats=include_formats, exclude_dirs=exclude_dirs)
    
    print(f"Directory tree has been written to the '{output_file}' file in {current_dir}")

# Example usage
if __name__ == "__main__":
    generate_tree(include_formats=['.py', '.txt', '.svg', '.md', '.css', '.js', '.html', '.yml' ], exclude_dirs=['node_modules'])
