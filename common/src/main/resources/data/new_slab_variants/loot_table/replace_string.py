import os
from typing import Union

def replace_string_in_file(file_path: str, old_string: str, new_string: str) -> None:
    with open(file_path, 'r') as file:
        filedata: str = file.read()

    new_data: str = filedata.replace(old_string, new_string)

    with open(file_path, 'w') as file:
        file.write(new_data)

def iterate_over_files(directory: str, old_string: str, new_string: str) -> None:
    for filename in os.listdir(directory):
        file_path: str = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            replace_string_in_file(file_path, old_string, new_string)

# Set the directory, old string, and new string
directory: str = 'blocks'
old_string: str = 'newslabvariants'
new_string: str = 'new_slab_variants'

# Call the function
iterate_over_files(directory, old_string, new_string)
