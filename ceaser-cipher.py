
import cipher_art

print(cipher_art.title)

def encode(text,shifts):
    encoded=""
    for t in text:
        if t not in cipher_art.letters:
            decoded+=t
            
        index=cipher_art.letters.index(t)
        newShift= (index+shifts)%52
        encoded += cipher_art.letters[newShift]
    print("\n\n Decoded Text: "+ encoded)    


def decode(text,shifts):
    decoded=""
    for t in text:
        if t not in cipher_art.letters:
            decoded+=t
        index=cipher_art.letters.index(t)
        newShift= (index+-shifts)%52
        decoded+= cipher_art.letters[newShift]
    print("\n\n Encoded Text: "+decoded)    
    


def encode_decode():
    decision= input("\n\n Do you want to encode or decode? Press 'e' or 'd': ")
    if decision not in "ed":
        print("Wrong input")
        return
    text= input("\n\n Enter the text: ")
    shifts= int(input("\n\n What is the number of shifts?: "))

    if decision=="e":
        encode(text,shifts)      
    elif decision=="d":
        decode(text,shifts)        
    else:
        print("Wrong input")

    response= input("Do u wish to continue? y or n")
    if response=="y":
        encode_decode()
    else:
        return


encode_decode()