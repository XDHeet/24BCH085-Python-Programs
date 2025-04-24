# Name: Heet Ghiya, Roll Number: 24BCH085 - Solution 1
# Program to count occurrences of my name in a text file

def count_name_occurrences(filename, name):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            count = content.lower().count(name.lower())
            print(f"Number of occurrences of '{name}': {count}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

# Example usage:
count_name_occurrences('sample.txt', 'Heet Ghiya')