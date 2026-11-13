
import random

print("Welcome to the Guess the Number game!")

number = random.randint(1, 100)

guess = 0

while guess != number:
    guess = int(input("Enter your guess: "))

    if guess > number:
        print("Your guess is too high. Guess again.")

    elif guess < number:
        print("Your guess is too low. Guess again.")

    else:
        print("Congratulations! You guessed the number correctly!")
