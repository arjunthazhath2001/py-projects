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
    p_names=file.readlines()
    

print(p_names)

for i in range(len(p_names)):
    stripped_name=p_names[i].strip('\n')
    new_letter= contents.replace('[name]',stripped_name) 
    with open(f"./output/readytosend/letter_for_{stripped_name}.docx",'w') as file:
        file.write(new_letter)


    


