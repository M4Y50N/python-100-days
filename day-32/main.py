import datetime as dt
import smtplib
import random

now = dt.datetime.now()
my_email = "pethersonreis@gmail.com"
password = "mpcf zyug mygv zefj"

if now.weekday() == 6:
    with open("./quotes.txt", mode="r", encoding="utf-8") as file:
        data = file.read()
        quotes = data.split('\n')
        day_quote = random.choice(quotes)
        print(day_quote)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="mayson.reiz@gmail.com",
            msg=f"Subject:Monday Motivation\n\n{day_quote}".encode("utf-8"))
