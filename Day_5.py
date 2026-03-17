# Data Structure - List

# List is a collection which is ordered and changeable. Allows duplicate members.
# List is written with square brackets.
# Create a List
mylist = ["apple", "banana", "cherry"]

# Access List Items
print(mylist[0])  # Output: apple
print(mylist[1])  # Output: banana
print(mylist[2])  # Output: cherry

# Change Item Value
mylist[1] = "blackcurrant"
print(mylist)  # Output: ['apple', 'blackcurrant', 'cherry']

# Loop Through a List
for x in mylist:
    print(x)

# Check if Item Exists
if "apple" in mylist:
    print("Yes, 'apple' is in the fruits list")

# List Length
print(len(mylist))  # Output: 3

# Add Items
mylist.append("orange")
print(mylist)  # Output: ['apple', 'blackcurrant', 'cherry', 'orange']

mylist.insert(1, "watermelon")
print(mylist)  # Output: ['apple', 'watermelon', 'blackcurrant', 'cherry', 'orange']

# Add Items Extend a List
tropical = ["mango", "pineapple", "papaya"]
mylist.append(tropical)
print(mylist)  # Output: ['apple', 'watermelon', 'blackcurrant', 'cherry', 'orange', 'mango', 'pineapple', 'papaya']

# Remove Items
mylist.remove("banana")
print(mylist)  # Output: ['apple', 'watermelon', 'blackcurrant', 'cherry', 'orange', 'mango', 'pineapple', 'papaya']    

mylist.pop(1)
print(mylist)  # Output: ['apple', 'blackcurrant', 'cherry', 'orange', 'mango', 'pineapple', 'papaya']

mylist.pop()
print(mylist)  # Output: ['apple', 'blackcurrant', 'cherry', 'orange', 'mango', 'pineapple']

del mylist[0]
print(mylist)  # Output: ['blackcurrant', 'cherry', 'orange', 'mango', 'pineapple']

mylist.clear()
print(mylist)  # Output: []

# Copy a List
mylist = ["apple", "banana", "cherry"]
mylist2 = mylist.copy()
print(mylist2)  # Output: ['apple', 'banana', 'cherry']

mylist3 = list(mylist)
print(mylist3)  # Output: ['apple', 'banana', 'cherry'] 



