import os

# Get the current working directory
current_directory = os.getcwd()
print("Current working directory:", current_directory)

# Construct the path to the text file in the same directory
text_file_path = os.path.join(current_directory, 'TC2.txt')

# Use the open function to read some lines from the text file
try:
    with open(text_file_path, 'r') as file:
        # Read the first three lines from the file
        lines = file.readlines()[:3]

        # Print the lines
        for line in lines:
            print(line.strip())

except FileNotFoundError:
    print(f"The file {text_file_path} does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")