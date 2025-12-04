import time

answer = input('Do you want to know about "Dhū al-Aktāf"? ').lower()
if answer.startswith('y'):
    text = ("""In 325 AD, due to the attacks of Arab tribes on Iran — including the plundering of cities and the assault on Iranian women and children — a war broke out between Sassanid Iran and the Arab tribes.
At that time, Shapur II was the king of Iran, and he managed to defeat the Arabs decisively. He then ordered that the shoulders of those captured Arabs be pierced and that they be hung from trees. This act caused such terror among the Arabs that they gave Shapur the Sassanid the title "Dhū al-Aktāf," meaning “the piercer of shoulders.”""")
    for char in text:
         print(char, end='', flush=True ), time.sleep(0.055)
elif answer.startswith('n'):
    print("Okay, maybe next time!")
else:
    print("Invalid input. Please answer with 'yes' or 'no'.")