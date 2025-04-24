print("Name:Heet Ghiya")
print("Roll no.:24BCH085")
def multiplicationTable(n):
    for i in range(1, 11):
        m = n*i
        print(f"{n} x {i} = {m}")
n = int(input("Enter a number: "))
multiplicationTable(n)