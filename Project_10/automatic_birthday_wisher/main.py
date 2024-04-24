import smtplib
import datetime as dt
import pandas as pd
import random
import os
# importing data from the csv file
data=pd.read_csv("birthdays.csv")


# Set the date and time to now

now =dt.datetime.now()
month=now.month
day=now.day
today=(month,day)
content=""
# Setting email sending parameters
password = os.environ.get('GMAIL_APP_PASSWORD')
email_sender='danyanderson2222@gmail.com'
# Creating the messages to be sent as well as managing everything related to message

# Birthday dictionary
birthday_dict=data.to_dict(orient="records")
for person in birthday_dict:
    name=person['name']
    email=person['email']
    birthday=(int(person['month']),int(person['day']))
    if today==birthday:
        with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as letter_file:
            content=letter_file.read()
            content=content.replace("[NAME]",name)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email_sender, password=password)
        connection.sendmail(from_addr=email_sender,
                            to_addrs="dany.guimefack@centrale-casablanca.ma",
                            msg=f"Subject:Happy Birthday!!! \n\n {content}"
        )
