# File handling in Python
# Open a file for writing
file = open('example.txt', 'w')
# Write some text to the file
file.write('Hello, this is an example of file handling in Python.\n')
# Close the file
file.close()    

# Open the file for reading
file = open('example.txt', 'r')
# Read the contents of the file
content = file.read()
# Print the contents of the file
print(content)
# Close the file
file.close()

# Using 'with' statement for file handling (automatically closes the file)
with open('example.txt', 'w') as file:
    file.write('This is another example using the with statement.\n')
    
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
# Appending to a file
with open('example.txt', 'a') as file:
    file.write('Appending some more text to the file.\n')
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
