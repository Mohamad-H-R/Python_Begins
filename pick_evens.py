def pic_evens(*args):
    result = []
    for n in args:
        if n % 2 == 0:
            result.append(n)
    return result

numbers = pic_evens(2, 5, 0, 100, 78, 6, 3, 21)
print(f"Even numbers: {numbers}")