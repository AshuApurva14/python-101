# This is a project that simulates a calculator. It takes in two numbers and an operator and returns the result of the operation.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter operator: ")

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)  
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("Invalid operator")

# Run the code and test it with different numbers and operators.

