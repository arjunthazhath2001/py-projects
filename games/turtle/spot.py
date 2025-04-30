# import colorgram
# colors = colorgram.extract('images.jpeg', 20)

# result=[]

# # for i in range(0,20):
# #     first_color = colors[i]
# #     rgb = first_color.rgb
# #     red = rgb[0]
# #     green= rgb[1]
# #     blue= rgb[2]
# #     result.append((red,green,blue))
import random
from turtle import Turtle, Screen
import turtle

colors= [
    (177, 173, 8),
    (239, 57, 213),
    (36, 180, 10),
    (158, 4, 90),
    (235, 48, 10),
    (212, 8, 4),
    (59, 145, 241),
    (67, 4, 146),
    (244, 53, 17),
    (221, 138, 63),
    (234, 214, 2),
    (216, 121, 200),
    (172, 52, 108)
]

y=0
def get_color():
    color= random.choice(colors)
    return color

turtle.colormode(255)

timmy= Turtle()

print(get_color())

for i in range(10):
    for j in range(10):
        timmy.dot(10, random.choice(colors))
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
    y+=30
    timmy.setpos(0,y)

    
    

screen = Screen()
screen.exitonclick()
