# Fortune Cokkie Game

# import random module

import random

print(f"Do you want to test  your Luck!...\nPlease choose any cookie from the list")
for i in range(1,13):
    print(i)

# Lets take a user input

user_input=int(input("What is your choice:\n"))

resulted_num=random.randint(1,13)

if user_input == resulted_num:
    print("Congrats! Your luck shines..\nToday is your day.")

else:
    print("Sorry! Bad Luck. Try Next time")




