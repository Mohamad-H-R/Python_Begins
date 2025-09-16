def sum_of_squares(n1, n2):
    result = n1**2 + n2**2
    return result


number1 = int(input("What is your first number? "))
number2 = int(input("What is your second number? "))
print(f"Sum of squares of {number1} and {number2} is: ")
print(sum_of_squares(number1, number2))