from datetime import datetime
from dotenv import load_dotenv
import os
import requests
import smtplib

load_dotenv()

MY_LAT = float(os.getenv("MY_LAT"))
MY_LNG = float(os.getenv("MY_LNG"))
MY_EMAIL = os.getenv("EMAIL")
MY_APP_PASSWORD_EMAIL = os.getenv("APP_PASSWORD_EMAIL")
MY_SMTP_EMAIL = os.getenv("SMTP_EMAIL")


# Get sunset and sunrise
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

response = requests.get("http://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


# Get iss position
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


time_now = datetime.now()

# Send email
if ((iss_latitude - 5 == MY_LAT or iss_latitude + 5 == MY_LNG) and
        (iss_longitude - 5 == MY_LNG or iss_longitude + 5 == MY_LNG) and sunset == time_now):
    with smtplib.SMTP(MY_SMTP_EMAIL, port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_APP_PASSWORD_EMAIL)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg="Look Up!")
