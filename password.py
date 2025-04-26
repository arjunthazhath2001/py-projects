import random
pwd=""
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



l= int(input("How many letters you need in you pwd?"))
n= int(input("How many numbers you need in you pwd?"))
s= int(input("How many symbols you need in you pwd?"))

for letter in range(0,l):
    pwd+=letters[random.randint(0,len(letters)-1)]

for num in range(0,n): 
    pwd+=numbers[random.randint(0,len(numbers)-1)]

for sym in range(0,s): 
    pwd+=symbols[random.randint(0,len(symbols)-1)]
    
l = list(pwd)
random.shuffle(l)
result = ''.join(l)

print("Your password is: "+result)

