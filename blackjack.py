import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


user_card1= random.randint(0,len(cards)-1)
user_card2= random.randint(0,len(cards)-1)


comp_card1= random.randint(0,len(cards)-1)
comp_card2= random.randint(0,len(cards)-1)


user_cards= [cards[user_card1],cards[user_card2]]
comp_cards= [cards[comp_card1], cards[comp_card2]]

print(f"Your cards:  {user_cards}")
print(f"Computer's first card: {comp_cards[0]}")



for i in range(len(user_cards)):
    if     
