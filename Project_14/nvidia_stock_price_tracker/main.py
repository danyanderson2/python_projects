import requests
import datetime as dt
from math import fabs
from twilio.rest import Client
import smtplib

my_email_address="danyanderson2222@gmail.com"
# SETTING THE NEWS AND STOCK ENDPOINTS
WATCH_CHANGE = 10
NEWS_ENDPOINT = 'https://newsapi.org/v2/top-headlines'
STOCK_ENDPOINT = 'https://www.alphavantage.co/query'
new_parameters = {
    "apiKey" : "newspaperapikey",  # newsapi.com
    "q" :  "nvidia",
    "sources" : "cnn, bbc news, the verge , bloomberg, opera-news, google-news, cbs news, The New York Times"
}
stock_parameters = {

    "function": "TIME_SERIES_DAILY",
    "symbol": "NVDA",
    "apikey": "alphavantage_api_key" # form alphavantage.co
}

# GETTING HOLD OF STOCK AND NEWS DATA FROM ENDPOINTS
news_data  =requests.get(NEWS_ENDPOINT,params=new_parameters).json()
stock_data =requests.get(STOCK_ENDPOINT,params=stock_parameters).json()


# PROCESSING THE STOCK ENDPOINT TO GET SPECIFIC OPENING AND CLOSING DATA BASED ON DATES
today= str(dt.datetime.now().date()-dt.timedelta(1))           # day n-1 is you're on day n
yesterday = str(dt.datetime.now().date() - dt.timedelta(2))
print(today)
today_op = float(stock_data['Time Series (Daily)'][today]['1. open'])
today_cl = float(stock_data['Time Series (Daily)'][today]['4. close'])
yest_cl = float(stock_data['Time Series (Daily)'][yesterday]['4. close'])
today_diff = today_op-today_cl                          # Opening and closing of today
day_diff = today_op - yest_cl                           # Closing of day n-2 beginning of day n-1


# Evaluating change percentages
today_diff_perc = fabs((today_diff/today_op)*100)
day_diff_perc = fabs(day_diff/yest_cl) *100


# Formatting the outputs for stock differences
day_result = ""
inter_day_result = ""
if today_diff < 0:
    day_result = "There was a stock price drop of the order of {:.2f}% today".format(today_diff_perc)
elif today_diff>=0:
    day_result = "There was a rise of the stock price by {:.2f}% today".format(today_diff_perc)
if day_diff <0 :
    inter_day_result = "The stock price dropped by {:.2f}% between yesterday and today".format(day_diff_perc)
elif day_diff >=0:
    inter_day_result = "The stock price rose by {:.2f}% between yesterday and today".format(day_diff_perc)


# CONFIGURING THE NEWS DATA AND PREPARING THEIR DISPLAY
total_result=news_data['totalResults']
news=""
if total_result == 0:
    news = "There's no major news around NVIDIA right now"
for i in range(0,total_result):
    news+=f"{news_data['articles'][i]['title']}\n"


# I send an email to myself if the watch change is surpassed
if day_diff_perc>WATCH_CHANGE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="danyanderson2222@gmail.com",password="gmail_password")
        connection.sendmail(from_addr=my_email_address,
                            to_addrs="danyanderson2222@gmail.com",
                            msg=f"Subject: New NVIDIA Stock Price update \n\n{news}\n\n{day_result}\n\n{inter_day_result}"
                            )


# ALTERNATIVELY, SEND A TEXT SMS TO MY PHONE NUMBER WITH THE TWILIO API
#     client = Client(account_sid, auth_token)
#     message = client.messages \
#             .create(
#                 body="There will be no rain tomorrow",
#                 from_='+12058592141',
#                 to='+212709034389'
#             )
#
#     print(message.sid)
