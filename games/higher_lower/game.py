import random
from utils import *
import os
score=0


def compare(A,B):
    if (data[A]['follower_count']>data[B]['follower_count']):
        res="A"
    else:
        res="B"
    return res


def game(A):
    global score
    os.system('clear')
    print(logo)    
    if score:
        print(f"You're right! Current score: {score}")
    B= random.randint(0,len(data)-1)
    print(f"Compare A: {data[A]['name']}, a {data[A]['description']}, from {data[A]['country']}")
    print(vs)
    print(f"Against B: {data[B]['name']}, a {data[B]['description']}, from {data[B]['country']}")

    choice=input("Who has more followers? Type 'A' or 'B':").upper()
    res= compare(A,B)

    if choice==res:
        score+=1
        A=B
        game(A)
    else:
        print(f"Sorry, that's wrong. Final score: {score}")


A= random.randint(0,len(data)-1)
game(A)