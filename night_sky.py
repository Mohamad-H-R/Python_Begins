import random
import time
import os

width = 60   # width of the screen
height = 20  # height of the screen

while True:
    # Clear the screen (works on Windows and Linux/Mac)
    os.system('cls' if os.name == 'nt' else 'clear')

    for _ in range(height):
        line = ""
        for _ in range(width):
            # Place a star with a small probability
            line += "*" if random.random() < 0.05 else " "
        print(line)
    time.sleep(0.2)  # refresh every 0.2 seconds
