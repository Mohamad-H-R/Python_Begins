import time
import os

width = 30        # width of the line
pos = 0           # starting position
direction = 1     # 1 = moving right, -1 = moving left

while True:
    os.system('cls' if os.name == 'nt' else 'clear')  # clear the terminal
    print(" " * pos + "🏀")                           # print the ball at current position
    time.sleep(0.05)

    # move the ball
    pos += direction

    # bounce when reaching edges
    if pos == 0 or pos == width:
        direction *= -1
