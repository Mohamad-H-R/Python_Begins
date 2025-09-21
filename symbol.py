import random
import time
import os

width = 40   # terminal width for the display
height = 15  # number of lines
symbols = ['*', '+', 'o', 'x', '#']

while True:
    # pick a random position and symbol
    x = random.randint(0, width)
    y = random.randint(0, height)
    s = random.choice(symbols)

    # clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # print empty lines until the "firework" height
    for i in range(y):
        print()
    # print the symbol at random horizontal position
    print(" " * x + s)

    time.sleep(0.2)   # pause a bit for the animation
