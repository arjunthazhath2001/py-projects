import random
words = ["cat", "rat", "dog", "lion", "tiger", "elephant", "giraffe", "zebra", "bear", "wolf"]
placeholder=""
animal=words[random.randint(0,len(words)-1)]
print(animal)

for a in animal:
    placeholder+="_ "

print(placeholder+"\n")
guess= input("Take a guess: ").lower()


for i in range(len(animal)):
    if animal[i]==guess:
        placeholder[i*2]=guess

print("\n\n"+''.join(placeholder)+"\n\n")
