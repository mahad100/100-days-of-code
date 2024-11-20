import art
import random

lives = 0

def gameplay():
    i = False
    answer = random.randint(1, 100)
    if difficulty == "easy":
        global lives
        lives = 10
    else:
        lives = 5

    while i is False:
        print(f"You have {lives} lives remaining")
        if lives == 0:
            i = True
            print(f"Unlucky :( \nThe answer was {answer} \nRefresh to try again")
            break

        guess = int(input("Make a Guess:"))
        if guess < answer:
            lives -= 1
            print("Too low")
        elif guess > answer:
            lives -= 1
            print("Too high")
        elif guess == answer:
            i = True
            print(f"You got it! \nYou had {lives} lives remaining \nWell done!")
        else:
            return "Invalid input Try again"






print(art.logo)
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")

gameplay()





