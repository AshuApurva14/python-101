''' Try-except statements are another selection structure in Python. 
   Try-except blocks are based upon whether a line or section of code returns an error.

   before we learn how to use try-except statements, we need to understand two types of errors in Python: syntax errors and exception errors.

   Try except statements can be used to try to run sections of Python code that may return an exception error. The general syntax of a try except statement is below:
 
try:
    <code to try>
except:
    <code to run instead>


   '''

# Example 1 of Syntax error

string = "problem solving"

print(string)

'''
Output will be :
File "/workspaces/python-101/try_except_statement/try_except_file1.py", line 9
    string="problem solving
           ^
SyntaxError: unterminated string literal (detected at line 9)

'''

# Example 2 of syntax error

if 'b' == 'b':
    string = "10problems"

'''
output will be:

File "/workspaces/python-101/try_except_statement/try_except_file1.py", line 25
    string = 10problems
              ^
SyntaxError: invalid decimal literal

'''


# Exception Errors
'''
1. Syntax errors are lines of code that are not valid Python.
2. Another type of error in Python is an exception error. 
3. Exception errors result when a valid line of Python code cannot run. 
4. Lines of code with exception errors contain valid Python code, but the line of code still cannot be executed.

'''

'''
For example, the statement f = open('file.txt','r') is valid Python code.
But if the file file.txt does not exist, Python throws an exception error because f = open('file.txt','r') cannot be executed.

'''
# Example 1 Exception error
# This line of code is valid code

# f = open('file.txt', 'r') 


'''
output will be:

Traceback (most recent call last):
  File "/workspaces/python-101/try_except_statement/try_except_file1.py", line 53, in <module>
    f = open('file.txt', 'r')
        ^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'file.txt'

'''
try:
    f = open('file.txt', 'r')

except:
    print(f'File does not exists')
 


# Example 2 Exception error
'''
a = 1
print(a[5])

'''

'''
Output will be:
Traceback (most recent call last):
  File "/workspaces/python-101/try_except_statement/try_except_file1.py", line 72, in <module>
    print(a[5])
          ~^^^
TypeError: 'int' object is not subscriptable


'''

# Improved try except version

try:
    a = 5
    print(a[4])
except:
    print(f'Variable a is not a list')

