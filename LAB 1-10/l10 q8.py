# Name: Heet Ghiya, Roll Number: 24BCH085 - Question 8 Solution
# Program to filter articles from text file

articles = {'a', 'the', 'an'}

with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    for line in infile:
        words = line.split()
        filtered_words = [' ' if word.lower() in articles else word for word in words]
        outfile.write(' '.join(filtered_words) + '\n')

print("Articles filtered and replaced with spaces successfully!")