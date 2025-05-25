# Commutative Property of Addition
# Take two numbers as input from the user

# Show the results of the Commutative Property of Addition

a = int(input("Enter your First Number:"))
b = int(input("Enter your Second Number:"))

# Commutative Property of Addition

print(f"\nCommutative Property of Addition: {a + b} = {b + a}")

# Check if the Commutative Property of Addition holds true
print("Checking if the Commutative property of Addition holds true...\n")

if a+ b == b +a:
    print("The Commutative Property of Addition holds true.")
else:
    print('oops! Th Commutative property of Addition does not hold true.')


