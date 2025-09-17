def is_greater(n1, n2):
    return n1 > n2


number1 = float(input("Choose your first number: "))
number2 = float(input("Choose your second number: "))

if is_greater(number1, number2) == True:
    print(f"{number1} is greater than {number2}")
else:
    print(f"{number1} isn't greater than {number2}")








