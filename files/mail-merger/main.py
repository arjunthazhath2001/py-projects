#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



with open("./input/letters/starting_letter.txt") as file:
    contents= file.read()
    
    
    
print(contents)

with open("./input/names/invited_names.txt") as file:
    p_names=file.read()
    names= p_names.split('\n')
    



for i in range(len(names)):
    new_letter= contents.replace('[name]',names[i]) 
    file= open(f"./output/readytosend/{names[i]}.txt",'w')
    file.write(new_letter)


    


