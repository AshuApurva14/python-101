# python-101

A beginner-friendly guide to learning Python, with explanations, real-world use cases, and simple code snippets for each topic.

---

## Table of Contents

1. [Variables and Data Types](#variables-and-data-types)
2. [Operators](#operators)
3. [Input and Output](#input-and-output)
4. [Strings](#strings)
5. [Lists, Tuples, Sets, Dictionaries](#lists-tuples-sets-dictionaries)
6. [Conditional Statements](#conditional-statements)
7. [Loops](#loops)
8. [Functions](#functions)
9. [Modules and Imports](#modules-and-imports)
10. [File Handling](#file-handling)
11. [Exception Handling](#exception-handling)
12. [Object-Oriented Programming](#object-oriented-programming)
13. [Popular Libraries](#popular-libraries)
14. [References & Resources](#references--resources)

---

## Variables and Data Types

**Explanation:**  
Variables store data. Data types define the kind of data (number, text, etc.).

**Use Case:**  
Storing user information, counters, flags, etc.

```python
age = 25          # integer
name = "Alice"    # string
height = 5.7      # float
is_active = True  # boolean
```

---

## Operators

**Explanation:**  
Operators perform operations on variables and values.

**Use Case:**  
Calculations, comparisons, logic in programs.

```python
a = 10 + 5      # Addition
b = 10 > 5      # Comparison (True)
c = not False   # Logical NOT (True)
```

---

## Input and Output

**Explanation:**  
Input gets data from the user; output displays data.

**Use Case:**  
Interactive programs, games, data entry.

```python
name = input("Enter your name: ")
print("Hello,", name)
```

---

## Strings

**Explanation:**  
Strings are sequences of characters.

**Use Case:**  
Storing and manipulating text, file paths, messages.

```python
greeting = "Hello, World!"
print(greeting.lower())  # hello, world!
```

---

## Lists, Tuples, Sets, Dictionaries

**Explanation:**  
- List: Ordered, changeable collection  
- Tuple: Ordered, unchangeable collection  
- Set: Unordered, unique items  
- Dictionary: Key-value pairs

**Use Case:**  
Storing collections of items, mapping data.

```python
fruits = ["apple", "banana", "cherry"]  # List
point = (10, 20)                        # Tuple
unique_numbers = {1, 2, 3}              # Set
person = {"name": "Bob", "age": 30}     # Dictionary
```

---

## Conditional Statements

**Explanation:**  
Run code based on conditions.

**Use Case:**  
Decision making, branching logic.

```python
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

---

## Loops

**Explanation:**  
Repeat actions multiple times.

**Use Case:**  
Processing lists, repeating tasks.

```python
for fruit in fruits:
    print(fruit)

count = 0
while count < 3:
    print(count)
    count += 1
```

---

## Functions

**Explanation:**  
Reusable blocks of code.

**Use Case:**  
Organizing code, avoiding repetition.

```python
def greet(name):
    print("Hello,", name)

greet("Alice")
```

---

## Modules and Imports

**Explanation:**  
Modules are files with Python code. Importing lets you use code from other files or libraries.

**Use Case:**  
Code organization, using libraries.

```python
import math
print(math.sqrt(16))
```

---

## File Handling

**Explanation:**  
Read from and write to files.

**Use Case:**  
Saving data, reading configurations.

```python
with open("data.txt", "w") as f:
    f.write("Hello, file!")
```

---

## Exception Handling

**Explanation:**  
Handle errors gracefully.

**Use Case:**  
Prevent crashes, handle invalid input.

```python
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("That's not a number!")
```

---

## Object-Oriented Programming

**Explanation:**  
Organize code using classes and objects.

**Use Case:**  
Modeling real-world things, reusable code.

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name, "says woof!")

dog = Dog("Buddy")
dog.bark()
```

---

## Popular Libraries

**Explanation:**  
Libraries add extra features to Python.

**Use Case:**  
Data analysis, web development, automation, etc.

```python
import requests
response = requests.get("https://api.github.com")
print(response.status_code)
```

---

## References & Resources

- [Official Python Docs](https://docs.python.org/3/)
- [W3Schools Python Tutorial](https://www.w3schools.com/python/)
- [Real Python](https://realpython.com/)
- [Python Tutor (visualize code)](https://pythontutor.com/)
- [LeetCode Python Problems](https://leetcode.com/problemset/all/?difficulty=Easy&tags=python)

---
