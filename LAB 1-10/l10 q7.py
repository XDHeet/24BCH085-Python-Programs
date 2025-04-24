# Name: Heet Ghiya, Roll Number: 24BCH085 - Question 7 Solution
# Program to serialize and deserialize Employee data

import pickle

class Employee:
    def __init__(self, empcode, empname, doj, salary):
        self.empcode = empcode
        self.empname = empname
        self.doj = doj
        self.salary = salary

# Create employee
emp = Employee("E001", "John Doe", "2023-01-15", 50000)

# Serialize
with open('employee.dat', 'wb') as file:
    pickle.dump(emp, file)

# Deserialize
with open('employee.dat', 'rb') as file:
    loaded_emp = pickle.load(file)

print(f"Deserialized Employee: {loaded_emp.empcode}, {loaded_emp.empname}, {loaded_emp.doj}, {loaded_emp.salary}")