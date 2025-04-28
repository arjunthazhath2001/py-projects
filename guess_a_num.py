import random
from guess_art import *

print(logo)
attempts=10
print("Welcome to the Number Guessing Game!\n I'm thinking of a number between 1 and 100.")

num= random.randint(1,100)

difficulty= input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty=="easy":
    print(f"You have {attempts} attempts remaining to guess the number.")