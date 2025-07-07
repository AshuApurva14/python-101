# I have defined a string below and when I execute this file, Then I got the error mentioned below:

#Good Morning! MADAM  

# Error

'''  File "/workspaces/python-101/data_types_in_python/strings.py", line 2
    Good Morning! MADAM
         ^^^^^^^
SyntaxError: invalid syntax
'''

# How to fix this issue

# step 1: Do assigned this value to a variable

str1="Good Morning! MADAM"

print(str1)

# You can use quote inside a string using (\)
# For Example

str2="Hi, I am a SRE\'s "

print(str2)


# You can use \n to print in next line.
# Also, keep in mind if you add any space after \n then python will print the string in the next line with some extra space.
# For example

str3="This is my School.\nI am a ex-student now."

print(str3)


# You can create a multiline string using triple quotes(""" """)
# For exampple

str4="""This is my place.
I am a Jharkhandi.
"""

print(str4)


# String concatenation (+)

