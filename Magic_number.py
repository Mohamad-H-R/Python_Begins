# input number by user
number = int(input("What is your number?\n"))

# check if number can be divided to 3 and 5
if number % 3 == 0 and number % 5 == 0:
    print("WOW!")
    print("Your number is LEGENDARY")

# check if number can be divided to 3
elif number % 3 == 0:
    print("Cool")
    print("Your number is Magical")

# check if number can be divided to 5
elif number % 5 == 0:
    print("Nooo!")
    print("Your number is Curesd")

# check if number can't be divided to 3 or 5
else:
    print("Your number is Normal")
    