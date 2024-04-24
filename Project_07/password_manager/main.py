from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pwd():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_list = password_letter + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)  # This method concatenates all the element of the list into a string
    password_input.insert(0,password)  # inserts password in the password_input list it will create position [0]
    pyperclip.copy(password)   # pyperclip's copy() method copies the value of password to the system's clipboard


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():  # triggered when the saved button is clicked. It sends a custom email with values of website, email and password
    website=website_input.get()
    email=email_input.get()
    password=password_input.get()

    if len(website)==0 or len(email)==0 or len(password)==0:
        is_ok=messagebox.showerror(title="Oops", message="Please leave no fields empty")

    else:
        is_ok=messagebox.askokcancel(title=f"{website}", message=f"These are the details you entered: \nEmail: {email} \nPassword: {password}\n Is it ok to save")
        if is_ok:
            with open("data.txt", "a") as data_file:
             data_file.write(f"{website} | {email:} | {password}  \n")
             website_input.delete(0,END)
             password_input.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()

window.config(padx=20,pady=20) # config attribute is available for all tkinter elements to adjust them
window.title("Password Manager")

#Here lies our canvas
canvas=Canvas(height=200,width=200)           # Creates canvas (object) unto which other elements are laid
img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=img)     # Canvas() method for adding and image. The photoImage is required
canvas.grid(row=0,column=1)

#---------------------Labels-------------------------
website=Label(text="Website:")
website.grid(row=1,column=0)
email_username=Label(text="Email_Username:")
email_username.grid(row=2, column=0)
password=Label(text="Password:")
password.grid(row=3, column=0)                       # grid is universal tkinter method for positioning elements

#-------------------------Input bar-----------------
website_input=Entry(width=35)
website_input.grid(row=1,column=1,columnspan=2)
website_input.focus()
email_input=Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0,"your_email@gmail.com")

password_input=Entry(width=17)
password_input.grid(row=3,column=1)

#------------------------------Buttons--------------------
generate_password=Button(text="Generate Password", command=generate_pwd) # command attribute of Button class takes function as argument
generate_password.grid(row=3,column=2)
add=Button(text="Add", width=36, command=save) # save is the function declared above that sends email
add.grid(row=4,column=1, columnspan=2)





window.mainloop()



