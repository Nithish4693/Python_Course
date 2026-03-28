# Exception handling in Python
# Basic try-except block

try:
    num1 = 10
    num2 = 1
    result = num1 / num2
    print("The result is:", result)
    
except Exception as e:
    print("An error occurred:", e)
    
finally:
    print("This block will always execute, regardless of whether an exception occurred or not.")

