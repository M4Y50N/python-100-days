from dotenv import load_dotenv
import smtplib
import os

load_dotenv()


class NotificationManage:
    def __init__(self):
        self.MY_SMTP_EMAIL = os.getenv("MY_SMTP_EMAIL")
        self.MY_EMAIL = os.getenv("MY_EMAIL")
        self.MY_APP_PASSWORD_EMAIL = os.getenv("MY_APP_PASSWORD_EMAIL")

        self.message = "Subject:Product Promotion\n\n"
        self.message_initial_len = len(self.message)

    def create_message(self, url):
        self.message += f"Product {url} price is lower, go and get it!\n\n"

    def send_email(self):
        with smtplib.SMTP(self.MY_SMTP_EMAIL, port=587) as connection:
            connection.starttls()
            connection.login(self.MY_EMAIL, self.MY_APP_PASSWORD_EMAIL)
            connection.sendmail(from_addr=self.MY_EMAIL,
                                to_addrs="pethersonreis@gmail.com",
                                msg=self.message)
