# Question 3 Solution
# Program to create an empty set, add 5 names, modify 1, and delete 2

names_set = set()

# Adding five names
names_set.update(["Alice", "Bob", "Charlie", "David", "Eve"])
print("Initial set:", names_set)

# Modifying 'Bob' to 'Bobby' (remove + add)
names_set.discard("Bob")
names_set.add("Bobby")
print("After modifying 'Bob' to 'Bobby':", names_set)

# Deleting two names
names_set.discard("Alice")
names_set.discard("Charlie")
print("After removing two names:", names_set)