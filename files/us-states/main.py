from turtle import Screen,Turtle
import pandas

screen= Screen()
screen.title("US-STATES")
image= "blank_states_img.gif"
screen.addshape(image)


my_turtle= Turtle()

my_turtle.shape(image)

guesses=[]
data= pandas.read_csv("50_states.csv")


all_states= data.state.to_list()

game_is_on=True
while game_is_on:
    state= screen.textinput(f"{len(guesses)}/50 States correct", "Enter name of the state:").title()

    
    if state=="Exit":
        game_is_on=False        
        break
    
    if state in all_states:
        state_data= data[data["state"]==state]
        if state not in guesses:
            guesses.append(state_data["state"].item())
            text_turtle= Turtle()
            text_turtle.penup()
            text_turtle.hideturtle()
            text_turtle.goto(state_data["x"].item(),state_data["y"].item())
            text_turtle.write(f"{state_data['state'].item()}")
        else:
            continue
    else:
        continue


data_dict={
    "States not guessed": [s for s in all_states if s not in guesses]
}


df= pandas.DataFrame(data_dict)
df.to_csv('trial.csv')
