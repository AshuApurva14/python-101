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

str5="Rakesh"
str6="Kumar"

print(str5 +" "+ str6)

# String slicing

str7="Anyone can"
str8="I can"

print(str7[3] + str8[2])

print(str7[:])


# Square bracket with different values indicates 

# [1:4:2] Here 1- indicates Start index of string
#              4 - Indicates Stop index (n-1)
#              2 - Indicates Step 

str9="Freedom"
print(str9[1:5:1])


# There can diff scenarios as well 
# [:6:1], [0:5:], [:], [0::0]

str10="India"
print(str10[:])