def is_positive(num):
    if num < 0:
        return False
    else:
        return True


user_number = int(input("what's your number? "))
print(f"is your number positive? {is_positive(user_number)}")