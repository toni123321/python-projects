# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random

def setAttempts(difficulty):
    if difficulty == 'easy':
        return 10
    else:
        return 5


def game():
    attempts = 0
    isGameEnd = 0

    while not isGameEnd:
        print("I'm thinking of a number between 1 and 100.")
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
        game_num = random.randint(1, 100)

        attempts = setAttempts(difficulty) # set the attempts
        while attempts != 0:
            print(f"You have {attempts} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            if guess == game_num:
                print("Congratulations! You have guessed!")
                isGameEnd = True
                return
            elif guess > game_num:
                print("Too high")
            else:
                print("Too low")
            attempts -= 1

        if attempts == 0:
            isGameEnd = True
            print("You have run out of guesses, you loose.")
            return


print("Welcome to the Number Guessing Game!")
game()


