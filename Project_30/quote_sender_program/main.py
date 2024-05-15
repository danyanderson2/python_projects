import os
import smtplib
from data import quotes
from datetime import datetime
from email.mime.text import MIMEText


date=datetime.now().date().strftime("%A").capitalize()
email_sender='danyanderson2222@gmail.com'
prog = 0
with open('progress.txt', 'r') as progress:
    a = progress.read().strip()
    score = int(a)
# print(score)
for i in range(score,score+1):
    author = quotes[i]['author']
    emoji= quotes[i]['emoji']
    containt = "\"" + quotes[i]['body']+ "\""

    # print(author,"\n",emoji,"\n",containt)


    with open('finished.txt', 'w',encoding='utf-8') as file:
        with open('template.txt', 'r') as temp:
            content=temp.read()
            quote_replace=content.replace('[QUOTE GOES HERE]', containt).replace('[AUTHOR NAME]', author).replace('[AUTHOR EMOJIS]', emoji)
        file.write(quote_replace)

# Send mail
with open('finished.txt', 'r', encoding='utf-8') as finished:
    content = finished.read()
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = "Motivational"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=email_sender, password=os.environ.get('GMAIL_APP_PASSWORD'))
    connection.sendmail(from_addr=email_sender,
                        to_addrs='dany.guimefack@centrale-casablanca.ma',
                        msg=msg.as_string(),
                        )
# make a tweet

prog = score+1
with open('progress.txt', 'w') as progress:
    prog = str(prog)
    progress.write(prog)


