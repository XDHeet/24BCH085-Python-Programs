# Name: Heet Ghiya, Roll Number: 24BCH085 - Question 2 Solution
# Program to read Excel data and convert to dictionary with total marks

import csv

student_dict = {}

with open('student_records.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        rollno = int(row['RollNo'])
        marks = [int(row['Maths']), int(row['Physics']), int(row['Chemistry'])]
        total = sum(marks)
        student_dict[rollno] = {
            'Name': row['Name'],
            'Marks': marks,
            'Total': total
        }

print("Student Records:")
for rollno, details in student_dict.items():
    print(f"RollNo: {rollno}, Name: {details['Name']}, Marks: {details['Marks']}, Total: {details['Total']}")