# import key modules
import pandas as pd
from turtle import Turtle,Screen

# instantiate the turtle and window
timmy=Turtle()
turtle=Turtle()
window=Screen()

window.addshape('blank_states_img.gif')
turtle.shape('blank_states_img.gif')
# reading csv file
data=pd.read_csv('50_states.csv')
all_states=data['state'].tolist() # list to monitor user's score, contains all the states in order

# input_box = window.textinput(title='50 Score', prompt='Enter a state name').title()
# print(input_box)


game_on = True
while game_on:
    input_box = window.textinput(title=f'{50-len(all_states)}/50 Score', prompt='Enter a state name or type \'exit\' to leave ').title()
    if input_box == 'Exit':
        game_on=False
    elif input_box in all_states:
        row=data[data.state == input_box]
        x=int(row.x) # the variable row contains the row whose state was mention. This row has an x and y value
        y=int(row.y)
        timmy.hideturtle()
        timmy.penup()
        timmy.goto(x,y)
        timmy.write(input_box)
        all_states.remove(input_box)


# writing the unknown states
unknown = pd.DataFrame(all_states)
unknown.to_csv('states_to_know')


