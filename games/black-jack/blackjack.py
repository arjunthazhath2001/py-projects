import random
from bj_art import *
import os




def mainGame():
    
    ###################### GENERATE 2 CARDS FOR DEALER AND PLAYER #####################
    user_cards=[]
    comp_cards=[]
    os.system('clear')
    print(logo)
    def generateCard():
        card= cards[random.randint(0,len(cards)-1)]
        return card

    for i in range(2):
        comp_cards.append(generateCard())
        user_cards.append(generateCard())
                
    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
    print(f"Computer's first card: {comp_cards[0]}")

    ##################################################################################


    ############################ THE GAME BEGINS HERE ###############################

    def game():

        if sum(user_cards)==21 and sum(comp_cards)!=21:
                print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
                print(f"Computer's final hand: {comp_cards[0]}, final score: {comp_cards[0]}")
                print("You Win with a Blackjack 😎")
                ans= input("\n Do you want another game: y or n : ")
                if ans=="y":
                    mainGame()
                else:
                    print("**************THANKS FOR PLAYING**************")
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
                else:
                    print("Its a draw")
            
            ans= input("\n Do you want another game: y or n : ")
            if ans=="y":
                mainGame()
            else:
                print("**************THANKS FOR PLAYING**************")
                return
            
                
        elif(user_choice=="y"):
            user_cards.append(generateCard())
            if sum(user_cards)<21:
                print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
                print(f"Computer's first card: {comp_cards[0]}, current score: {comp_cards[0]}")
                game()
            elif sum(user_cards)==21:
                print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
                print(f"Computer's final hand: {comp_cards}, final score: {sum(comp_cards)}")
                if sum(comp_cards)==21:
                    print("Lose, opponent has Blackjack 😱")
                else:
                    print("You win 😁")
            else:
                print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
                print(f"Computer's final hand: {comp_cards}, final score: {sum(comp_cards)}")
                print("You went over. You lose 😭")
            
            ans= input("\n Do you want another game: y or n : ")
            if ans=="y":
                mainGame()
            else:
                print("**************THANKS FOR PLAYING**************")
                return
                

    # start the game
    game()

mainGame()