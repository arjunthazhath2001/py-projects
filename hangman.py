import random
import hangman_Art

words = ["cat", "rat", "dog", "lion", "tiger", "elephant", "giraffe", "zebra", "bear", "wolf"]
placeholder=""
lives=6
animal=words[random.randint(0,len(words)-1)]
print(animal)

for a in animal:
    placeholder+="_ "

print(placeholder+"\n")

chances= len(animal)

correct_letters=[]

gameOver= False


while not gameOver:
    print(hangman_Art.stages[lives-1])
    
    guess= input("Take a guess: ").lower()

    
    
    if guess not in animal:
        lives-=1
    
    chances-=1
    
    display=""
    
    


    for i in range(len(animal)):
        if animal[i]==guess:
            display+="{} ".format(guess)
            correct_letters.append(guess)
        elif (animal[i] in correct_letters):
            display+="{} ".format(animal[i])
        else:
            display+="_ "
    
    if '_' not in display:
        print("YOU WIN")
        gameOver=True
    elif lives==0:
        print("YOU LOOSE")
        gameOver=True


    print(display+"\n\n\n")
