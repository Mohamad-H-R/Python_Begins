def is_even(n):
    return n % 2 == 0


number = int(input("What's your number? "))
if is_even(number) == True:
    print(f"{number} is even")
else:
    print(f"{number} is odd")