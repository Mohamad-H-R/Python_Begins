def divide(a, b):
    result = a / b
    return result


while True:
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        result = divide(num1, num2)

    except ValueError:
        print("just numbers allowed!")
        continue

    except ZeroDivisionError:
        print("can't divided to zero!")
        continue

    else:
        print("Result:", result)

    finally:
        print("done")





























#print("Result:", divide(num1, num2))