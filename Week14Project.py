import os

def generate_files_info(directory):
    """
    Generate a list of dictionaries containing information about files in the specified directory.
    """
    files_info = []

    # Iterate over files in the specified directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Check if it's a regular file
        if os.path.isfile(file_path):
            # Collect information about the file
            file_info = {
                'name': filename,
                'size': os.path.getsize(file_path)  # Size in bytes
            }

            # Append the file information to the list
            files_info.append(file_info)

    return files_info

def print_files_info(files_info):
    """
    Print information about files in the list of dictionaries.
    """
    for file_info in files_info:
        print(f"File: {file_info['name']}, Size: {file_info['size']} bytes")

# Get the current working directory
current_directory = os.getcwd()

# Generate the list of dictionaries containing file information
files_info_list = generate_files_info(current_directory)

# Print the information about each file
print_files_info(files_info_list)
