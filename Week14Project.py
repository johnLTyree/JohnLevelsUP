import os

# Get the current working directory
current_directory = os.getcwd()

# List to store information about files
files_info = []

# Iterate over files in the current working directory
for filename in os.listdir(current_directory):
    # Get the full path of the file
    file_path = os.path.join(current_directory, filename)

    # Check if it's a regular file
    if os.path.isfile(file_path):
        # Collect information about the file
        file_info = {
            'name': filename,
            'size': os.path.getsize(file_path)  # Size in bytes
        }

        # Append the file information to the list
        files_info.append(file_info)

# Print the information about each file
for file_info in files_info:
    print(f"File: {file_info['name']}, Size: {file_info['size']} bytes")
