# Tuple in Python
# A tuple is an ordered collection of items that is immutable (cannot be changed after creation).
# Tuples are written with round brackets () and items are separated by commas.

# Creating a tuple
mytuple = ("apple", "banana", "cherry")

# Accessing elements in a tuple
print(mytuple[0])  # Output: apple
print(mytuple[1])  # Output: banana
print(mytuple[2])  # Output: cherry 

# Length of a tuple
print(len(mytuple))  # Output: 3

# Tuples are immutable, so you cannot change their values after they have been created.
# However, you can create a new tuple by concatenating two tuples together.
mytuple2 = ("orange", "grape")
new_tuple = mytuple + mytuple2
print(new_tuple)  # Output: ('apple', 'banana', 'cherry', 'orange', 'grape')

