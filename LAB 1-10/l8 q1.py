# Name: Heet Ghiya, Roll Number: 24BCH085 - Question 1 Solution
# Program to convert words in a list to uppercase and store them in a set

words = ['apple', 'banana', 'cherry', 'date', 'elderberry']
uppercase_words = {word.upper() for word in words}

print("Original words:", words)
print("Uppercase words set:", uppercase_words)