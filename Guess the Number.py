import random


def guess():
    print("Welcome to guess the number!")
    x = int(input("Inputting the range. Enter a low number: "))
    y = int(input("Inputting the range. Enter a high number: "))
    while x > y:
        print("The first number must be lower than the second number")
        x = int(input("Inputting the range. Enter a low number: "))
        y = int(input("Inputting the range. Enter a high number: "))
    random_number = random.randint(x,y)
    guess = -1
    while guess != random_number:
        guess = int(input(f"Enter a number between {x} and {y}: "))
        if guess > random_number:
            print("Wrong. Try a lower number")
        elif guess < random_number:
            print("Wrong. Try a higher number")
    print(f"You guessed the right number, it was {random_number}")

guess()