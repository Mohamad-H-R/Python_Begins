import time
import os
from datetime import datetime

while True:
    # clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # get current time in HH:MM:SS format
    now = datetime.now().strftime("%H:%M:%S")

    # print a nice clock display
    print("🕒  " + now)

    # update every second
    time.sleep(1)
