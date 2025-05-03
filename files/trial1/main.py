with open("file.txt") as file:
    content= file.read()
    print(content)


with open("abc.txt",'a') as file:
    file.write("ARJUN\n")