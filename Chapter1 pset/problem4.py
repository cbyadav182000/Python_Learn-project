import os

def print_directory_contents(path):
    try:
        # Get the list of all files and directories
        entries = os.listdir(path)
        print(f"Contents of the directory '{path}':")
        for entry in entries:
            print(entry)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access the directory '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
directory_path = '/'
print_directory_contents(directory_path)
