# Dictionary in Python


# A dictionary is a collection of key-value pairs. Each key is unique and maps to a value.
# Dictionaries are written with curly braces {} and key-value pairs are separated by commas.
# Key must be of an immutable data type (like strings, numbers, or tuples), and values can be of any data type.

# Creating a dictionary
student_1 = {
    "name": "John", 
    "age": 20, 
    "city": "New York", 
    "is_major": True
}

# Accessing values in a dictionary

print(student_1["name"])  # Output: John
print(student_1["age"])   # Output: 20
print(student_1["city"])  # Output: New York
print(student_1["is_major"])  # Output: True

# changing values in a dictionary
student_1["age"] = 21
print(student_1["age"])  # Output: 21

# Adding new key-value pairs to a dictionary
student_1["grade"] = "A"
print(student_1)  # Output: {'name': 'John', 'age': 21, 'city': 'New York', 'is_major': True, 'grade': 'A'}

# Removing key-value pairs from a dictionary
del student_1["is_major"]
print(student_1)  # Output: {'name': 'John', 'age': 21, 'city': 'New York', 'grade': 'A'}
student_1.pop("city")
print(student_1)  # Output: {'name': 'John', 'age': 21, 'grade': 'A'}

