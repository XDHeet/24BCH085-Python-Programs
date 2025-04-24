# Name: Heet Ghiya, Roll Number: 24BCH085 - Question 4 Solution
# Program to create subdirectory and copy a file

import os
import shutil

# Create subdirectory
os.makedirs('new_directory', exist_ok=True)

# Copy file
shutil.copy('source_file.txt', 'new_directory/copied_file.txt')

print("File copied to new directory successfully!")