# Savings Calculator Starter File

# Task 1: Setting Up Variables
# Create variables for monthly savings here
month1 = 50
month2 = 43
month3 = 81

# Task 2: Calculating Total Savings
# Calculate total savings here
total_savings = month1 + month2 + month3

# Task 3: Calculating Average Savings
# Calculate average savings here
num_month = 3
average_savings = total_savings / num_month

# Task 4: Formatting and Printing Results
# Print the formatted results here
print(f"total saving: {total_savings}$\r\naverage saving: {average_savings}$")

# Bonus Challenges:
# 1. Modify the program to handle 4 months of savings
month4 = 31
num_month += 1
total_savings += month4
average_savings = total_savings / num_month
print(f"total saving: {total_savings}$\r\naverage saving: {average_savings}$")
# 2. Round the average savings to the nearest whole dollar
rounded_average_savings = round(average_savings)
print(f"rounded average saving: {rounded_average_savings}$")
# 3. Calculate what persentage each month's savings contribute to the total
p_month1 = month1 * 100 / total_savings
p_month2 = month2 * 100 / total_savings
p_month3 = month3 * 100 / total_savings
p_month4 = month4 * 100 / total_savings
print("The contribution of each month in total saving is like this:")
print(f"""Month1: {p_month1:.2f}% 
Month2: {p_month2:.2f}%
Month3: {p_month3:.2f}%
Month4: {p_month4:.2f}%""")