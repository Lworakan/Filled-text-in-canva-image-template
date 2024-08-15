import os

# Path to the directory containing the files
directory = './FRAB11-Self-Introduction% (2)'

# Prefix to add to each file name
prefix = '673405000'

# Iterate over files in the directory and rename them
for filename in os.listdir(directory):
    if filename.endswith(".jpg"):  # Only rename .jpg files
        new_name = f"{prefix}{filename}"
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))

print("Files renamed successfully.")
