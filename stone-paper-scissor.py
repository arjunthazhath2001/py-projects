import random
import p1

user_choice= input("ROCK (0), PAPER (1) OR SCISSOR (2)?")
actions=["stone","paper", "scissor"]


if user_choice not in ["0","1","2"]:
    print("invalid choice")
    
else:
    user_choice= int(user_choice)
    comp_choice= random.randint(0,2)


    print("\n\nCOMPUTER CHOSE:\n"+p1.items[comp_choice])
    print("\n\nYOU CHOSE:\n"+p1.items[user_choice])

    if(user_choice==comp_choice):
        print("ITS A DRAW")
    elif (user_choice-comp_choice)%3==1:
        print("YOU WON")
    else:
        print("YOU LOSE")
    
    

