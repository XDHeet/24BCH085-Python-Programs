print("Name:Heet Ghiya")
print("Roll No.:24BCH085")
import random as r
a = [r.randint(1, 30) for _ in range(50)]
print(f"Generated list: {a}")
b = []
for item in a:
    if item not in b:
        b.append(item)
print(f"List without duplicates: {b}")