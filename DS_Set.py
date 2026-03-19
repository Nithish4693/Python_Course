# Set in DS
# A set is an unordered collection of unique elements. Sets are written with curly braces {} and elements are separated by commas.
# Sets do not allow duplicate values and do not maintain any order.

# Creating a set
fruits = {"apple", "banana", "cherry"}

# Accessing elements in a set
for fruit in fruits:
    print(fruit)

# Adding elements to a set
fruits.add("orange")
print(fruits)  # Output: {'apple', 'banana', 'cherry', 'orange'}    

# Removing elements from a set
fruits.remove("banana")
print(fruits)  # Output: {'apple', 'cherry', 'orange'}

my_list = [1,2,3,4,5,1,1,1,1,1,2,2,2,2,2]

print(set(my_list)) # Output: {1, 2, 3, 4, 5}