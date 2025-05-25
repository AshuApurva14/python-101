# Associative Property of Addition
# Take three numbers as input from the user
# Associative Property of Addition

a = int(input("Enter your First Number: "))
b = int(input("Enter your Second Number: "))
c = int(input("Enter your Third Number: "))

# Add the numbers in different orders

sum1 = a + (b +c)
sum2 = (a + b) + c
sum3 = a + b + c

print("The sum of the three numbers i diferent orders is\n)


# Print the results

print(f"The sum of the numbers in the order a + (b + c ) is: {sum1}")

print(f"The Sum of the Numbers in the order (a + b) + c is: {sum2}")

print(f"The sum of the numbers in the order a + b +c is: {sum3}")



