from datetime import datetime
from dotenv import load_dotenv
import os
import requests
import smtplib
import time

load_dotenv()

MY_LAT = float(os.getenv("MY_LAT"))
MY_LNG = float(os.getenv("MY_LNG"))
MY_EMAIL = os.getenv("EMAIL")
MY_APP_PASSWORD_EMAIL = os.getenv("APP_PASSWORD_EMAIL")
MY_SMTP_EMAIL = os.getenv("SMTP_EMAIL")


def get_sunset_sunrise():
    # Get sunset and sunrise
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }

    response = requests.get("http://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    return (int(data["results"]["sunrise"].split("T")[1].split(":")[0]),
            int(data["results"]["sunset"].split("T")[1].split(":")[0]))


def get_iss_position():
    # Get iss position
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    return float(data["iss_position"]["latitude"]), float(data["iss_position"]["longitude"])


time_now = datetime.now().hour

# Send email
while True:
    time.sleep(60)
    sunrise, sunset = get_sunset_sunrise()
    iss_latitude, iss_longitude = get_iss_position()
    if ((MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and
            (MY_LNG - 5 <= iss_longitude <= MY_LNG + 5) and
            (time_now >= sunset or time_now <= sunrise)):
        with smtplib.SMTP(MY_SMTP_EMAIL, port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_APP_PASSWORD_EMAIL)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg="Subject:Watch out ISS!!\n\nLook Up To The Sky!!!")
