# file_tree.py
"""

"""
import os

# Define the directory to map
project_root = "."

# Exclude specific directories
exclude_dirs = {".idea", ".git", "cdk.out"}

# Output file
output_file = "project_structure.txt"

def generate_file_tree(directory, prefix=""):
    """
    Generate a tree structure of the files and directories in a given directory
    :param directory: the directory to recursively search
    :param prefix:
    :return:
    """
    file_tree = []
    try:
        entries = sorted(os.listdir(directory))
        for index, entry in enumerate(entries):
            path = os.path.join(directory, entry)
            if entry in exclude_dirs:
                continue

            connector = "└── " if index == len(entries) - 1 else "├── "
            file_tree.append(f"{prefix}{connector}{entry}")

            if os.path.isdir(path):
                extension = "    " if index == len(entries) - 1 else "│   "
                file_tree.extend(generate_file_tree(path, prefix + extension))
    except PermissionError:
        pass  # Skip directories that can't be accessed
    return file_tree

# Generate the file tree
file_tree = generate_file_tree(project_root)

# Save to file
with open(output_file, "w") as f:
    f.write("\n".join(file_tree))

# Provide output file path
output_file
