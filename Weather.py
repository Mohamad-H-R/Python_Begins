import os
import random
import time

width = 40   # width of the screen
flakes = ["❄", "*", "·"]  # different snowflake symbols

while True:
    # build one line of random snow
    line = "".join(random.choice(flakes + [" "]*6) for _ in range(width))
    
    # clear the screen and print the line
    os.system('cls' if os.name == 'nt' else 'clear')
    print(line)

    time.sleep(0.15)  # small delay for animation speed
