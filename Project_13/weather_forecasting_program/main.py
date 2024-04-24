import requests
from twilio.rest import Client
import os

account_sid = os.environ.get("TWILIO_ACC_ID")
auth_token = os.environ.get("TWILIO_AUTH")
api_Key=os.environ.get("OWM_API_KEY")
LAT=33.449329
LON=-7.648520

parameters={
    "lat":LAT,
    "lon":LON,
    "appid":"984f028e7c20e75aa0393d1b4a355660",
    "cnt":4 #make sure we get data for the next four timestamps(correspoding to 12hours)
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=parameters)
response.raise_for_status()
weather = response.json()
print(weather)

# since we predict in steps of 3hours over 12 hours we can decide to get hold of all
# the weather status for these days


will_rain=False
for three_hour_interval in weather["list"]:
    condition=three_hour_interval["weather"][0]["id"]
    if int(condition)>700:
        will_rain=True
    if will_rain:
        client=Client(account_sid,auth_token)
        message = client.messages \
        .create(
            body="There will be no rain tomorrow",
            from_='+12058592141',  # number sending sms
            to='+212709034389'     # the number receiving the sms
        )

        print(message.sid)
#
