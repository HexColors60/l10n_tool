import sys
import re
import os

def get_existing_filenames(directory):
    filenames = [filename for filename in os.listdir(directory) if filename.endswith('.txt')]
    return set(filenames)

def check_file(filename):
    existing_filenames = get_existing_filenames(os.getcwd())

    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line_number, line in enumerate(lines, 1):
        match = re.match(r'(\S+) (\d+) ---(.+)', line)
        if not match:
            print(f"Invalid format on line {line_number}: {line.strip()}")
            continue

        file_name, line_num, data = match.groups()
        if file_name not in existing_filenames:
            print(f"Filename '{file_name}' on line {line_number} does not exist in the current directory.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    input_filename = sys.argv[1]
    check_file(input_filename)
