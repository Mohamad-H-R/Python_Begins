def calculator(a, b, op):
    if op == "+":
        print("جمع:", a + b)
    elif op == "-":
        print("تفریق:", a - b)
    elif op == "*":
        print("ضرب:", a * b)
    elif op == "/":
        if b != 0:
            print("تقسیم:", a / b)
        else:
            print("خطا: تقسیم بر صفر ممکن نیست!")
    else:
        print("عملیات نامعتبر است!")

# گرفتن عدد از کاربر
num1 = float(input("عدد اول رو وارد کن: "))
num2 = float(input("عدد دوم رو وارد کن: "))
operator = input("عملیات رو وارد کن (+, -, *, /): ")

# فراخوانی فانکشن
calculator(num1, num2, operator)