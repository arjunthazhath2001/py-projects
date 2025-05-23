import random
from guess_art import *

print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

easy_attempts=10
hard_attempts=5
num= random.randint(1,100)



def game(attempts):
    for i in range(attempts,0,-1):
        print(f"You have {i} remaining")
        try:
            guess= int(input("Take a guess: "))
        except:
            print("Enter a correct number")
            return    
        if guess==num:
            print(f"You are right. The number is {num}")
            return
        elif guess<num:
            print("Too low")
            continue
        else:
            print("Too high")
            continue
    print("Sorry u have lost")

difficulty= input("Choose a difficulty. Type 'easy' or 'hard': ")
if(difficulty=="easy"):
    game(easy_attempts)
elif(difficulty=="hard"):
    game(hard_attempts)
else:
    print("Please enter correct value")