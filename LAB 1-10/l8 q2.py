# Name: Heet Ghiya, Roll Number: 24BCH085 - Question 2 Solution
# Program to create a set of 10 random numbers (15-45), count numbers <30, and delete numbers >35

import random

random_numbers = set(random.randint(15, 45) for _ in range(10))
count_less_than_30 = len([num for num in random_numbers if num < 30])
filtered_numbers = {num for num in random_numbers if num <= 35}

print("Original random numbers:", random_numbers)
print("Count of numbers less than 30:", count_less_than_30)
print("Set after removing numbers > 35:", filtered_numbers)