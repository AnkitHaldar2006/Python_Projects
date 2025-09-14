import random

number = random.randint(1, 20)
attempts = 0

print("I'm thinking of a number between 1 and 20...")

while True:
    guess = int(input("Take a guess: "))
    attempts += 1
    if guess == number:
        print("Correct! You guessed it in", attempts, "tries ")
        break
    elif guess < number:
        print("Too low ⬇️")
    else:
        print("Too high ⬆️")
