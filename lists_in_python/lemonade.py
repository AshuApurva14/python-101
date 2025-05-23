# SELLING LEMONADE

# You sell lemoonde over two weeks, the lists show number of lemaonade sold per week
# Profit for each glass of lemonade is $1.5
# Add another day to week 2 list by capturing the number as input
# Combine the two lists as 'Sales'
# Calculate and print how much much yo have earned on:
  # Best day
  # Worst day
  # Separate and in Total


sales_week1 = [10, 20, 30, 40, 50, 60, 45]
sales_week2 = [15, 25, 35, 45, 55, 65]

sales = []

input_day_sales_number = int(input("Enter the number of sales for the new day: "))

sales_week2.append(input_day_sales_number)

sales = sales_week1+ sales_week2

print(f"Sales for Combined weeks:{sales}")

print(f"Best day profit is ${max(sales)*1.5}")

print(f"Worst day profit is ${min(sales)*1.5}")

print(f"Combine day profit is ${sum(sales)*1.5}")
