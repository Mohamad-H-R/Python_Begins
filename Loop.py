# input number by user
number = int(input("Choose your number: "))
x = number

# loop exactly 'number' times
for _ in range(number):
    if x % 2 == 1:   # if odd
        x = 2 * x - 1
    else:            # if even
        x = x // 2
    print(x)
