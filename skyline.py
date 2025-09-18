def skyline(*args):
    max = 0
    for i in args:
        if i > max:
            max = i
    return max


print(f"The highest building in Tehran is {skyline (12, 54, 10, 120, 100, 250)} meters")