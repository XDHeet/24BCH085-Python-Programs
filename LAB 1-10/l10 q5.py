# Name: Heet Ghiya, Roll Number: 24BCH085 - Question 5 Solution
# Program to copy file with lowercase converted to uppercase

with open('source.txt', 'r') as src_file:
    content = src_file.read()

with open('destination.txt', 'w') as dest_file:
    dest_file.write(content.upper())

print("File copied with all characters converted to uppercase!")