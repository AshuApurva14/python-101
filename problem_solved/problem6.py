# Problem Scenario 6

'''
Create a program that asks the user for two numbers (use two different input lines). 
If the second number the user enters is zero, 
print back to the user "can't divide by zero", 
otherwise divide the user's first number by the user's second number and print the result to the user.

'''

num1=int(input("Enter  first number "))
num2=int(input("Enter second number "))

if num2 == 0:
    print("can't divide by zero")

else:
    print(f"Division of Two numbers: {num1 // num2}")