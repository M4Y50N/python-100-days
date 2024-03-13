import datetime as dt
import random
import pandas
import smtplib

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# Check today's birthday
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents.replace("[NAME]", birthday_person["name"].capitalize())

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user="pethersonreis@gmail.com", password="mpcf zyug mygv zefj")
        connection.sendmail(from_addr="pethersonreis@gmail.com",
                            to_addrs=birthday_person["email"],
                            msg=f"Subject: Happy Birthday\n\n{contents}")

