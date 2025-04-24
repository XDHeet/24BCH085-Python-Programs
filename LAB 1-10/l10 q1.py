# Name: Heet Ghiya, Roll Number: 24BCH085 - Question 1 Solution
# Program to create a CSV file that can be opened in MS-Excel

import csv

data = [
    ["RollNo", "Name", "Maths", "Physics", "Chemistry"],
    [1, "Alice", 85, 90, 88],
    [2, "Bob", 78, 82, 80],
    [3, "Charlie", 92, 95, 90]
]

with open('student_records.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file 'student_records.csv' created successfully!")