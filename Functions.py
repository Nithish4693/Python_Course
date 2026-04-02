# ============================================
# PYTHON FUNCTIONS - REVISION NOTES
# ============================================


# --------------------------------------------
# 1. WHAT IS A FUNCTION?
# --------------------------------------------
# A function is a reusable block of code that performs a specific task.
# Helps avoid repetition and improves code readability.


# --------------------------------------------
# 2. BASIC FUNCTION SYNTAX
# --------------------------------------------
def greet1():
    print("Hello!")

greet1()


# --------------------------------------------
# 3. PARAMETERS & ARGUMENTS
# --------------------------------------------
# Parameter -> variable in function definition
# Argument  -> value passed when calling function

def greet2(name):
    print("Hello", name)

greet2("Nathish")


# --------------------------------------------
# 4. RETURN vs PRINT
# --------------------------------------------
# print() -> displays output
# return  -> sends value back to caller

def add(a, b):
    return a + b

result = add(2, 3)
print(result)


# --------------------------------------------
# 5. DEFAULT PARAMETERS
# --------------------------------------------
# If no argument is passed, default value is used

def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Ram")

# -------------------------------------------------------------------------------------------------

# --------------------------------------------
# 6. MULTIPLE RETURN VALUES
# --------------------------------------------
# Functions can return multiple values (tuple)

def calc(a, b):
    return a + b, a * b

sum_val, mul_val = calc(2, 3)


# --------------------------------------------
# 7. *args (MULTIPLE POSITIONAL ARGUMENTS)
# --------------------------------------------
# Allows passing any number of arguments

def total(*numbers):
    return sum(numbers)

print(total(1, 2, 3, 4))


# --------------------------------------------
# 8. **kwargs (MULTIPLE NAMED ARGUMENTS)
# --------------------------------------------
# Accepts keyword arguments as dictionary

def info(**data):
    print(data)

info(name="Nathish", age=20)


# --------------------------------------------
# 9. LAMBDA FUNCTION
# --------------------------------------------
# Anonymous one-line function

add = lambda a, b: a + b
print(add(2, 3))


# --------------------------------------------
# 10. VARIABLE SCOPE
# --------------------------------------------
# Global -> defined outside function
# Local  -> defined inside function

x = 10  # global

def test():
    x = 5  # local
    print(x)

test()
print(x)


# --------------------------------------------
# 11. RECURSION
# --------------------------------------------
# Function calling itself

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))


# --------------------------------------------
# 12. PRACTICAL EXAMPLE
# --------------------------------------------
# Check even numbers in a list

def is_even(num):
    return num % 2 == 0

numbers = [1, 2, 3, 4]

for n in numbers:
    if is_even(n):
        print(n, "is even")


# --------------------------------------------
# 13. KEY TAKEAWAY
# --------------------------------------------
# Function = Input -> Process -> Output
# Use functions to:
# - Reuse code
# - Make code clean
# - Improve logic structure


# --------------------------------------------
# 14. PRACTICE TASKS
# --------------------------------------------
# 1. Function to find square of a number
# 2. Function to check palindrome
# 3. Function to find max of 3 numbers
# 4. Function to find sum of a list


