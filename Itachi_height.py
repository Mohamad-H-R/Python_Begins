# Itachi height
itachi_height = 166

# User height
user_height_str = input("How tall are you (cm) ?:\n")

#changing to number and fix error
try:
    user_height = int(user_height_str)
    
    # comparing Itachi height to user
    if itachi_height > user_height:
        print("How cute! You are shorter than Itachi")
    elif itachi_height == user_height:
        print("Awesome! You are as tall as Itachi")
    else:  # itachi_height < user_height
        print("Oh cool! You are taller than Itachi")
        
except ValueError:
    print("Invalid input, please enter a number.")
