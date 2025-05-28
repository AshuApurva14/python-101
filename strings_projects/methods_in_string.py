# Different string methods in python

# Python provides a rich set of methods to manipulate strings

# 1. upper() - Converts all characters in a string to uppercase.

upper_string = "This is a Uppercase String."
print(upper_string.upper())

# 2. lower() - Converts all characters in a string to lowercase.

lower_string = "This is a Lowercase String."
print(lower_string.lower())

# 3. title() - Converts the first character of each word to uppercase.
title_string = "this is a title string."
print(title_string.title())

# 4.capitalize() - Coverts the first character of a string to uppercase and the rest to lowercase.
capitalize_string = "this is a capitalize string."
print(capitalize_string.capitalize())


# 5. strip() - Removes leading and trailing whitespace from a string.abs
strip_string = "  This is a string with leading and trailing spaces.   "
print(strip_string.strip())

# 6. split() - Splits a string into a list of substrings based on a specified delimiter.
split_string = "This is a string that will be split into words."
print(split_string.split())

# 7. replace() - Replaces occurrences of a specified substring with another substring.abs
replace_string = "This is a string that will be replaced."
print(replace_string.replace("replaced", "modified"))

# 8. find() - Returns the index of the first occurrence of a specified substring, or -1 if not found.
find_string = "This is a string that will be searched."
print(find_string.find("searched"))  # Returns the index of the first occurrence
print(find_string.find("notfound"))  # Returns -1 if not found

# 9.count() - Returns the number of occurrences of a specified substring in a string.
count_string = "This is a string that will be counted."
print(count_string.count("is"))  # Counts occurrences of "is"

# 10. startswith() - Checks if a string starts with a specified substring.
startswith_string = "This is a string that starts with 'This'."
print(startswith_string.startswith("This"))  # Returns True

# 11. endswith() - Checks if a string ends with a specified substring.
endswith_string = "This is a string that ends with 'ends with'."
print(endswith_string.endswith("ends with"))  # Returns True

# 12. join() - Joins a list of strings into a single string with a specified delimiter.
join_list = ["This", "is", "a", "joined", "string."]
join_string = " ".join(join_list)
print(join_string)  # Joins the list with spaces

# 13. isdigit() - Checks if all characters in a string are digits.
isdigit_string = "123456"
print(isdigit_string.isdigit())  # Returns True

# 14. isalpha() - Checks if all characters in a string are alphabetic.
isalpha_string = "HelloWorld"
print(isalpha_string.isalpha())  # Returns True









