from bs4 import BeautifulSoup
import requests
import smtplib
import lxml

URL="https://www.amazon.com/HP-Touchscreen-Processor-Bluetooth-Fingerprint/dp/B0CJRF8957/ref=sr_1_3?crid=9ACG833LELF3&dib=eyJ2IjoiMSJ9.m0xQWmOh2iZl_L73fYgn2AV7Q-_ojfSXLuEPEEZeOqYXwq259fCaqtPjewgwq-fssa07NaZ9VmDf5hcOWM1lNvLij-sV4szNYJigW1QUhYxTtKqmvT7Grqpqu72_ianwiVa6PkF6LDbbVZssyOH5IWGOJ_iJ40n_R7aJ2-qsci2TCC-rHr6VtS4AVzGvwWJLCrY4w4O4JXlITnko6wYcWuK2XEP7n8a6O_0NHWafdSo.czzMOvuCsVc_AG9xagnce32uJ74168HI-ftkF17lSa0&dib_tag=se&keywords=laptop+hp+envy+17+inch+32GB+RAM&qid=1705774764&sprefix=laptop+hp+envy+17+inch+32gb+ram%2Caps%2C212&sr=8-3"
USER="danyanderson2222@gmail.com"
RECIPIENT="danyanderson2222@gmail.com"
PASSWORD="MY_GMAIL_APP_PASSWORD"


headers={
    "User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "X-Forwarded-For":"41.251.254.145",
    "x-forwarded-proto":"https"
}
response=requests.get(URL, headers=headers)
web_page=response.text
soup=BeautifulSoup(web_page,"lxml")
price=soup.find(name="span", class_="a-price-whole")
text=price.getText().split(".")
print(len(text[0]))
in_words=[]
for n in text[0]:
    if n in "1234567890":
        in_words.append(n)
words="".join(in_words)
laptop_price=int(words)

if 1000<=laptop_price<=1275:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=USER,password=PASSWORD)
        connection.sendmail(
            to_addrs=USER,
            from_addr=RECIPIENT,
            msg=f"Subject: New price drop !!!\n\n Your laptop's price has now dropped to ${laptop_price}"
        )