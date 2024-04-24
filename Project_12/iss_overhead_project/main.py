import smtplib
import time
import requests
from datetime import datetime
import math
import os
MY_LAT = 33.449330 # Your latitude
MY_LONG = -7.648520 # Your longitude

my_email="danyanderson2222@gmail.com"
password=os.environ.get('GMAIL_APP_PASSWORD')


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
time_now = datetime.now().hour
#If the ISS is close to my current position
latitude_diff= math.fabs(iss_latitude-MY_LAT)
longitude_diff=math.fabs(iss_longitude-MY_LONG)


if longitude_diff<10 and latitude_diff<10:
    # and it is currently dark
    if time_now<=sunrise and time_now>=sunset:
# Then send me an email to tell me to look up.

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="anderson.guimefack@2ie-edu.org",
                                msg="Subject:Do not miss this ! \n\n"
                                      r"look up, the International Space"
                                    "Station is currently overhead")



