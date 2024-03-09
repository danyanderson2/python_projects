from tkinter import *

#window
window=Tk()
window.minsize(width=150 ,height=100)
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)        # configure keyword arguments of any tkinter template

#All labels
miles=Label(text="Miles") # Label is a tkinter class for writing down text
miles.grid(row=0,column=2) # the grid method is available on all tkinter templates and allows for positioning
km=Label(text="Km")
km.grid(row=1,column=2)
is_equal=Label(text="is equal to")
is_equal.grid(row=1,column=0)

#Entry
entry=Entry(width=30)  # Entry is the tkinter class for inputing text zones
entry.grid(row=0,column=1)

def calc_and_print():
    n=float(entry.get())  # gets value from entry variable and parses it to float
    m=n*1.607
    answer.config(text=m) # sets the answer label object to value of m, the distance in kilometers

answer=Label(text="0")
answer.grid(row=1,column=1)
#button
button=Button(text="Calculate", command=calc_and_print) # the second argument of the Button class represent the function
button.grid(row=2, column=1)




window.mainloop()