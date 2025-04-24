print("Name: Heet Ghiya")
print("Roll No.: 24BCH085")
import math as m
def fac(n):
    r = 1
    for j in range(1, n + 1):
        r *= j
    return r
d = int(input("Enter the value of X(in degree):"))
x = d*3.14159/180
sinX = 0
for i in range (1, 15, 2):
    a