# Problem Scenario 2

'''
02> Create a program that asks the user for their temperature. 
If the user enters a temperature above 98.6, print back to the user "You have a fever".
'''


temperature=input("Do you want to find whether you have fever🤒 or not...\n Please Enter your temperature ")

temperature=float(temperature)

if temperature > 98.6:
    print("You have a Fever🤒")

