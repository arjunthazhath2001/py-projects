import random
from turtle import Turtle, Screen


screen= Screen()
game_on=False

screen.setup(width=500,height=400)
user_bet= screen.textinput(title="UR BET?", prompt="Which turtle? enter color")

colors= ["red","orange","yellow","green","blue", "purple"]
turtles=[]

def generate_turtle(name, turtle_color,x,y):
    name= Turtle(shape="turtle")
    name.penup()
    name.color(turtle_color)
    name.goto(x=x,y=y)
    turtles.append(name)


y=-100
for i in range(len(colors)):
    generate_turtle(colors[i],colors[i],x=-230,y=y)
    y+=40



if user_bet:
    game_on=True


while game_on:    
    for turtle in turtles:
        if turtle.xcor()==230:
            game_on=False
            win= tuple.pencolor()
            if win==user_bet:
                print(f"{user_bet} HAS WON")
            else:
                print("YOU LOSE")
            
        number= random.randint(0,10)
        turtle.forward(number)


screen.exitonclick()