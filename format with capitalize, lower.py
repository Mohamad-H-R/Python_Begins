# format with .capitalize, .lower(), .upper(), . swapcase()
 #NOTE: use print()
# get input for a variable , fav_food, that describes a favorite food 
fav_food = input("What is your favorite food: ")

# display fav_food as ALL CAPS, used in a sentence
print(f"so your favorite food is {fav_food}".upper())

# display fav_food as all lower case, used in a sentence 
print(f"so your favorite food is {fav_food}".lower())

# display fav_food with swapped case used in sentence 
print(f"so your favorite food is {fav_food}".swapcase())

# display fav_food with capitalization, used in a sentence
print(f"so your favorite food is {fav_food}".capitalize())

fav_color = "Forest Green"
# display the fav_color variable as upper, lower, swapcase, and capitalize formatting in a single print
print(f"your favorite color is:\n\r{fav_color.upper()}, {fav_color.lower()}, {fav_color.swapcase()}, {fav_color.capitalize()}")