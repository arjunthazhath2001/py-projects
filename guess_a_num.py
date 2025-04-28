import random
from guess_art import *

print(logo)
print("Welcome to the Number Guessing Game!\n I'm thinking of a number between 1 and 100.")

easy_attempts=10

num= random.randint(1,100)

difficulty= input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty=="easy":
    print(f"You have {easy_attempts} attempts remaining to guess the number.")
    user_num= input("Make a guess")
    while easy_attempts>0:
        if user_num<num:
            print("Too low")
            print("Guess Again")
            attempts-=1
            print(f"You have {easy_attempts} attempts remaining to guess the number.")
        elif user_num>num:
            print("Too high")
            print("Guess Again")
            easy_attempts-=1
            print(f"You have {easy_attempts} attempts remaining to guess the number.")
        else:
            print(f"You got it. The answer was {num}")
    else:
        print("You've run out of guesses.")