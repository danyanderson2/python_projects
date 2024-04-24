from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


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

    password_letter = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list = password_letter + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_input.get()
    email=email_input.get()
    password=password_input.get()
    new_data={
        f"{website}":{
        "email":email,
        "password": password
    }
    }

    if len(website)==0 or len(email)==0 or len(password)==0:
        is_ok=messagebox.showerror(title="Oops", message="Please leave no fields empty")

    else:
        try:
            with open("data.json", "r") as data_file:
                #reading old data
                data=json.load(data_file)
                #updating the old data
                data.update(new_data)
                #dump the updated data
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
            with open("data.json", "w") as data_file:
                 json.dump(data,data_file,indent=4)

        finally:
            website_input.delete(0,END)
            password_input.delete(0,END)



# ----------------------------Manage Search-----------------------------------------
def find_password():
    website=website_input.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.error(title="website", message="No data file found")
    else:
        if website in data:
            email=data[website]["email"]
            password=data[website]["password"]
            messagebox.showinfo(title= website,message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showerror(title="Error", message=f"No details for {website} exits. ")




# ---------------------------- UI SETUP ------------------------------- #

window=Tk()

window.config(padx=20,pady=20)
window.title("Password Manager")

#Here lies our canvas
canvas=Canvas(height=200,width=200)
img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=img)
canvas.grid(row=0,column=1)

#---------------------Labels-------------------------
website=Label(text="Website:")
website.grid(row=1,column=0)
email_username=Label(text="Email_Username:")
email_username.grid(row=2, column=0)
password=Label(text="Password:")
password.grid(row=3, column=0)

#-------------------------Input bar-----------------
website_input=Entry(width=17)
website_input.grid(row=1,column=1)
website_input.focus()
email_input=Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0,"danyanderson2222@gmail.com")

password_input=Entry(width=17)
password_input.grid(row=3,column=1)

#------------------------------Buttons--------------------
generate_password=Button(text="Generate Password", command=generate_pwd)
generate_password.grid(row=3,column=2)
add=Button(text="Add", width=36, command=save)
add.grid(row=4,column=1, columnspan=2)

search=Button(text="Search", command=find_password)
search.grid(row=1, column=2)





window.mainloop()

#A good way to apply what I learnt here would be by using pandas to save to csv file and be able to do some manipulations
#Extra personal project