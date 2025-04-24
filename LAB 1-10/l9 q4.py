print("Name:Heet Ghiya")
print("Roll No.:24BCH085")
def isPangram(string):
    a = set('abcdefghijklmnopqrstuvwxyz')
    lstring = set(string.lower())
    
    return a <= lstring
string = input("Enter a string:")
print(isPangram(string))