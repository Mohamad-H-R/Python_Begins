import random

print("🎯 Welcome to the Guessing Game!")
secret = random.randint(1, 50)   # secret number between 1 and 50
attempts = 0

while True:
    guess = input("Guess a number (1–50): ")
    if not guess.isdigit():
        print("Please type a number!")
        continue

    guess = int(guess)
    attempts += 1

    if guess < secret:
        print("Too low ⬇️")
    elif guess > secret:
        print("Too high ⬆️")
    else:
        print(f"🎉 Correct! The number was {secret}.")
        print(f"You found it in {attempts} attempts.")
        break
