def sum_numbers(*args):
    result = 0
    for n in args:
        result += n
    return result


print(sum_numbers(2, 5, 3, 7))