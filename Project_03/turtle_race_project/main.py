from turtle import Turtle,Screen
import random

is_bet_on=False   # the bet is initially set to false.
screen = Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors=["red","orange","yellow", "green", "blue","purple"]
y_positions=[-70,-40,-10,20,50,80]
all_turtles=[]
# setting end message
def endmessage(message):
    t = Turtle()
    t.hideturtle()
    t.penup()
    t.goto(0, 0)
    t.write("You Won !!!", align='center', font=('Arial', 25, 'bold'))



for turtle_index in range(0,6):   # create six "turtle" shaped turtle instances
    t=Turtle(shape="turtle")
    t.color(colors[turtle_index])
    t.penup()
    t.goto(-230, y_positions[turtle_index])  # aligning the turtles on the screen vertically based on preset positions
    all_turtles.append(t)

is_bet_on=True   # set is bet to true in order to run the loop
while is_bet_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print("You won")
                endmessage("You won !!")
            else:
                print("You lost")
                endmessage('You lost :(')
            is_bet_on = False
        rand_distance=random.randint(1,10)
        turtle.forward(rand_distance)


"""
REVISION SPOT
tim=Turtle(shape="turtle")
tim.color(colors[0])
tim.penup()
tim.goto(-200,0)

tom=Turtle(shape="turtle")
tom.color(colors[1])
tom.penup()
tom.goto(-200,50)

a=Turtle(shape="turtle")
a.color(colors[2])
a.penup()
a.goto(-200,25)

b=Turtle(shape="turtle")
b.color(colors[3])
b.penup()
b.goto(-200,-25)

c=Turtle(shape="turtle")
c.color(colors[4])
c.penup()
c.goto(-200,-50)

d=Turtle(shape="turtle")
d.color(colors[5])
d.penup()
d.goto(-200,-75)




def move_forwards():
    tim.forward(10)
def move_backwards():
    tim.backward(10)

def counter_clockwise():
    tim.left(10)

def clock_wise():
    tim.right(10)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s",fun=move_backwards)
screen.onkey(key="a", fun=clock_wise)
screen.onkey(key="d", fun=counter_clockwise)
screen.onkey(key="c", fun=clear)
"""

screen.exitonclick()