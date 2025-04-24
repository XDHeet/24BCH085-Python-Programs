# Name: Heet Ghiya, Roll Number: 24BCH085 - Question 6 Solution
# Program to merge lines from two files alternatively

with open('file1.txt', 'r') as f1, open('file2.txt', 'r') as f2:
    lines1 = f1.readlines()
    lines2 = f2.readlines()

with open('merged.txt', 'w') as out_file:
    for line1, line2 in zip(lines1, lines2):
        out_file.write(line1)
        out_file.write(line2)
    
    # Write remaining lines from longer file
    if len(lines1) > len(lines2):
        out_file.writelines(lines1[len(lines2):])
    elif len(lines2) > len(lines1):
        out_file.writelines(lines2[len(lines1):])

print("Files merged alternatively successfully!")