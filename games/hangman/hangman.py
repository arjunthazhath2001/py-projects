import random
import hangman_Art
import hangman_words

words=hangman_words.animals



placeholder=""
lives=6
animal=words[random.randint(0,len(words)-1)]


print(hangman_Art.title+"\n\n")


print(animal)

for a in animal:
    placeholder+="_ "

print(placeholder+"\n")

chances= len(animal)

correct_letters=[]

gameOver= False


while not gameOver:
    
    guess= input("Take a guess: ").lower()

    
    
    
    
    chances-=1
    
    display=""
    
    if guess in correct_letters:
        print('You have already entered: '+guess)
        continue


    for i in range(len(animal)):
        if animal[i]==guess:
            display+="{} ".format(guess)
            correct_letters.append(guess)
        elif (animal[i] in correct_letters):
            display+="{} ".format(animal[i])
        else:
            display+="_ "
    
    if guess not in animal:
        lives-=1
        print(f"********{lives} LIVES LEFT********")
        if(lives==0):
            gameOver=True
            print("********You LOOSE********")
    
    
    print(hangman_Art.stages[lives])

        
    if '_' not in display:
        print("********YOU WIN********")
        gameOver=True


    print(display+"\n\n\n")
