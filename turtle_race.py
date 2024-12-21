from turtle import Turtle
from turtle import Screen
import random
my_screen=Screen()
my_screen.setup(width=1200,height=600)
race_on=False
user_bet=my_screen.textinput(title="make a bet..",prompt="which color of the turtle win the race:")


color=["red","yellow","blue","green","orange"]
list =[-250,-150,-50,50,150]
turtle_list=[]

for i in range(0,5):
    t = Turtle(shape="turtle")
    t.color(color[i])
    t.penup()
    t.goto(x=-580,y=list[i])
    turtle_list.append(t)


if user_bet:
    race_on=True
while race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 580:
            wining_color=turtle.pencolor()
            if(wining_color==user_bet):
                print(f"you won!,wining turtle color is{wining_color}")
            else:
                print(f"you loss the match,wining turtle color is {wining_color}")
            race_on=False


        random_distance=random.randint(1,10)
        turtle.forward(random_distance)


my_screen.exitonclick()
