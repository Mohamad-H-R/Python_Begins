# Create a variable called 'price' as a string with the value '19.99'.
price = "19.99"

# Convert 'price' to a float and store it in a new variable called 'price_float'.
price_float = float(price)

# Create a variable called 'quantity' as an integer with a value 5.
quantity = 5

# Calculate the total cost by multiplying 'price_float' and 'quantity', and store it in a variable called 'total_cost'.
total_cost = price_float * quantity

# Convert 'total_cost' to an integer (round down) and store it in a variable called 'total_cost_int'.
total_cost_int = total_cost

# Print out 'price', 'price_float', 'quantaty', 'total_cost', 'total_cost_int' along with their types.
print(f"""
      Price: {price}: {type(price)}
      Price_float: {price_float}: {type(price_float)}
      Quantity: {quantity}: {type(quantity)}
      total_cost: {total_cost}: {type(total_cost)}
      total_cost_int: {total_cost_int}: {type(total_cost_int)}
""")