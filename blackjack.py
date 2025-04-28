import random
from bj_art import *

print(logo)

user_cards=[]
comp_cards=[]

def generateCard():
    card= cards[random.randint(0,len(cards)-1)]
    return card

def game():
    #generate two cards for user and comp
    for i in range(2):
        comp_cards.append(generateCard())
        user_cards.append(generateCard())

    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
    print(f"Computer's first card: {comp_cards[0]}")

    if sum(user_cards)==21 and sum(comp_cards)!=21:
            print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
            print(f"Computer's final hand: {comp_cards[0]}, final score: {comp_cards[0]}")
            print("You Win with a Blackjack 😎")
            return

    user_choice= input("\n\nType 'y' to get another card and type 'n' to pass: ")

    if(user_choice=="n"):
        if sum(comp_cards)==21:
            print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
            print(f"Computer's final hand: {comp_cards}, final score: {sum(comp_cards)}")
            print("Lose, opponent has Blackjack 😱")
            
            
        while sum(comp_cards)<17:
            comp_cards.append(generateCard())
        
        print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
        print(f"Computer's final hand: {comp_cards}, final score: {sum(comp_cards)}")
        
        if sum(comp_cards)>21:    
            print("Opponent went over. You win 😁")
            
        elif sum(comp_cards) >=17:
            if sum(comp_cards)>sum(user_cards):
                print("You lose 😤")
                
            elif sum(user_cards)>sum(comp_cards):
                print("You win 😁")

game()