from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card Game")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

new_card={}
words_to_learn={}

# -------------------------------------------- Collecting Data with Pandas -----------------------------------------



try:
    data = pd.read_csv("data/to_be_learnt.csv")
except FileNotFoundError:
    original=pd.read_csv("data/arabic_words.csv")
    words_to_learn = original.to_dict(orient='records')
else:
    words_to_learn =data.to_dict(orient="records")



def next_word():
    global new_card, timer
    window.after_cancel(timer)
    new_card=random.choice(words_to_learn)
    canvas.itemconfig(title,text="Arabic", fill="black")
    canvas.itemconfig(word,text=new_card["Arabic"], fill="black")
    canvas.itemconfig(background,image=card_front_img)
    timer= window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(title, text="English",fill="white")
    canvas.itemconfig(word, text=new_card["English"],fill="white")
    canvas.itemconfig(background,image=card_back_img)


def is_known():
    words_to_learn.remove(new_card)
    print(len(words_to_learn))
    data=pd.DataFrame(words_to_learn)
    data.to_csv("data/to_be_learnt.csv",index=False)
    next_word()


timer = window.after(3000, func=flip_card)



################---------------------Canvas----------------###########
canvas=Canvas(width=800, height=526)
card_front_img=PhotoImage(file="images/card_front.png")
card_back_img=PhotoImage(file="images/card_back.png")
background=canvas.create_image(400,263,image=card_front_img)
title=canvas.create_text(400,158,text="Title", font=("Arial",40, "italic"))
word=canvas.create_text(400,263,text="Word", font=("Arial",60,"bold"))

canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)
# -------------------------------------------Buttons-------------------------------------------------#


w_img=PhotoImage(file="images/wrong.png")
unknown_button=Button(image=w_img,highlightthickness=0,command=next_word)
unknown_button.grid(row=1,column=0)

r_img=PhotoImage(file="images/right.png")
right_button=Button(image=r_img, highlightthickness=0,command=is_known)
right_button.grid(row=1, column=1)


next_word()
window.mainloop()