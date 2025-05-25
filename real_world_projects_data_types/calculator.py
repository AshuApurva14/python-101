# This is a project that simulates a calculator. It takes in two numbers and an operator and returns the result of the operation.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

operator = input("Choose the operation from the below list \n 1. Add(+) \n 2.Substract(-) \n 3.Multiply(*) \n 4.Divide (/) \n 5.Modulus(%) \n") 

operator = operator.strip()  # Remove any leading/trailing whitespace

operator = operator.lower()  # Convert to lowercase for consistency

def is_valid_operator(op):
    if op in ["+","-", "*", "/", "%"]:
        print("Valid operator")
    else:
        print("Invalid operator ... Please try again! Valid operators are +, -, *, /, %")
        

# Perform the operation based on the operator

def perform_operation(num1, num2):
    is_valid_operator(operator)
    result = None  # Initialize result variable
    if operator == "+":
       result = print(num1 + num2)
    elif operator == "-":
        result = print(num1 - num2)
    return result


__main__ = "__main__"
if __name__ == "__main__":
    perform_operation(num1, num2)



# elif operator == "-":
#     print(num1 - num2)  
# elif operator == "*":
#     print(num1 * num2)
# elif operator == "/":
#     print(num1 / num2)
# elif operator == "%":
#     print(num1 % num2)
# else:
#     print("Invalid operator ... Please try again! Valid operators are +, -, *, /, %")


