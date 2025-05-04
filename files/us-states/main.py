from turtle import Screen,Turtle
import pandas

screen= Screen()
screen.title("US-STATES")
image= "blank_states_img.gif"
screen.addshape(image)


my_turtle= Turtle()

my_turtle.shape(image)


data= pandas.read_csv("50_states.csv")

game_is_on=True
while game_is_on:
    state= screen.textinput("Guess the state", "Enter name of the state:").title()



   
    state_data= data[data["state"]==state]
    
    if not state_data.empty():
        
        text_turtle= Turtle()
        text_turtle.penup()
        text_turtle.hideturtle()
        text_turtle.goto(state_data["x"].item(),state_data["y"].item())
        text_turtle.write(f"{state_data['state'].item()}")

    else:
        print("Enter correct data")



screen.mainloop()