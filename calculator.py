num1 = int(input("Enter first number: "))
operation = input("Enter operation (+, -, *, /, %): ")
num2 = int(input("Enter second number: "))
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
elif operation == '%':
    if num2 != 0:
        result = num1 % num2
    else:
        result = "Error: Division by zero"
else:
    result = "Error: Invalid operation"

print(num1, operation, num2, "=", result)

# This code is a simple calculator that performs basic arithmetic operations.