import re
import os
import shutil

# Define the directory containing the extracted files
extraction_dir = "./Persona_67_submission"

# Function to clean up and extract the student ID from the content
def extract_clean_student_id(content):
    start_index = content.find('รหัสนักศึกษา') + len('รหัสนักศึกษา:')
    end_index = content.find('>', start_index)
    student_id = content[start_index:end_index].strip('<> \n')
    # Remove any non-alphanumeric characters and limit the length
    clean_student_id = re.sub(r'[^a-zA-Z0-9]', '', student_id)[:20]
    return clean_student_id

# Dictionary to store file paths and their content
student_ids = {}

# Read the content of each markdown file in the directory
for root, dirs, files in os.walk(extraction_dir):
    for file in files:
        if file.endswith(".md"):  # Ensure we're only dealing with markdown files
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                student_ids[file_path] = content

# Create a mapping of the extracted files with the new filenames based on the cleaned student ID
for file, content in student_ids.items():
    # Clean the student ID
    student_id = extract_clean_student_id(content)
    
    # Define the new filename
    new_filename = f'{student_id}.md'

    # Define the new file path
    new_file_path = os.path.join(os.path.dirname(file), new_filename)
    print(f"Renaming {file} to {new_file_path}")

    # Rename the file
    try:
        shutil.move(file, new_file_path)
    except Exception as e:
        print(f"Error renaming file {file} to {new_filename}: {e}")

# List the files in the directory after renaming
renamed_files = []
for root, dirs, files in os.walk(extraction_dir):
    for file in files:
        renamed_files.append(os.path.join(root, file))

# Print out the renamed files
print("Renamed files:")
for file in renamed_files:
    print(file)
