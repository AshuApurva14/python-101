# Problem Scenario 5

'''
Create a program that asks a user for one of three trig functions: sine, cosine or tangent. Calculate the sine, cosine or tangent of 
π
/
4
 depending on the user's input and print the result of the calculation back to the user.


'''
import math

trig_func=input('Enter the trignometric function from the list: \nsine\ncosine\ntangent\n\n')
pi=3.14

if trig_func == 'sine':
     
   print(math.sin(pi/4))

elif trig_func == 'cosine':
    print(math.cos(pi/4))

else:
    print(math.tan(pi/4))


