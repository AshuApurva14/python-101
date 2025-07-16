# Problem Secnario 3

'''
 Create a program that chooses a random number number between 1 and 5. 
 Ask the user for a number between 1 and 5. 
 Compare the user's number to the random number. 
 If the user guessed the random number print "you guessed it!", if the user did not guess the random number print back to the user "try again". 
 You can use the code below to choose a random number n between 1 and 5.
'''

import random

random_number=random.randint(0,5)

user_input=input("Let's check how correct you are ! \n please enter a number between 1 and 5 ")

user_input=float(user_input)

if user_input == random_number:
    print("Hurray!🥳 You guessed it right!")

else:
    print("Sorry!😞 Try again")
