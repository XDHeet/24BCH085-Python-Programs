print("Name:Heet Ghiya")
print("Roll no.:24BCH085")
def RemoveString(s1,s2):
 
 if s2 in s1:
    return s1.replace(s2,"")
 else:
    return s1
     
 
s1 = input("Enter the main string: ")
s2 = input("Enter the string to remove: ")
r = RemoveString(s1,s2)
print(f"The resulting string is:{r}")