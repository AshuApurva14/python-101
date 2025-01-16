# Date: 14th January 2025

# This is a simple program that generates a random number between 1 and 10

# I will use this random number in the guessing game program
# where the user has to guess the number between 1 and 10

# The random module provides a random number generator.

#import the random module
import random

# Take user input
user_input = int(input("Enter a number between 1 and 10: "))

# The randint() method generates a random integer between the specified integers.

# Generate a random number between 1 and 10
random_num = random.randint(1, 10)

# Check if the user input is equal to the random number

if user_input == random_num:
    print("You guessed it right!")
else:
    print("You guessed it wrong!")
    print("The random number was:", random_num)
