import random
words = ["cat", "rat", "dog", "lion", "tiger", "elephant", "giraffe", "zebra", "bear", "wolf"]
placeholder=""
animal=words[random.randint(0,len(words)-1)]
print(animal)

for a in animal:
    placeholder+="_ "

print(placeholder+"\n")

chances= len(animal)

correct_letters=[]

while(chances):
    guess= input("Take a guess: ").lower()

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

    print(display+"\n\n\n")
