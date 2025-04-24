# Question 4 Solution
# Program to separate names starting with 'A' or 'B' into two sets

names = {"Apple", "Banana", "Apricot", "Blueberry", "Avocado", "Blackberry", "Cherry"}
a_names = {name for name in names if name.startswith('A')}
b_names = {name for name in names if name.startswith('B')}

print("Original set:", names)
print("Names starting with A:", a_names)
print("Names starting with B:", b_names)