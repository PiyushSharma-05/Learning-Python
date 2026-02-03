import os

# Define the directory you want to list
# Use '.' for the current directory or provide a full path like 'C:/Users/Documents'
path = "/"

try:

    dir_contents = os.listdir(path)
    
    print(f"Contents of '{os.path.abspath(path)}':")
    print("-" * 30)
    
    for item in dir_contents:
        print(item)

except FileNotFoundError:
    print("The specified directory does not exist.")
except PermissionError:
    print("You do not have permission to access this directory.")