from twilio.rest import Client
from dotenv import load_dotenv
import smtplib
import os

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()


class NotificationManager:
    def __init__(self):
        self.TWILIO_SID = os.getenv("TWILIO_SID")
        self.TWILIO_AUTH = os.getenv("TWILIO_AUTH")
        self.TWILIO_PHONE = os.getenv("TWILIO_PHONE")
        self.MY_PHONE = os.getenv("MY_PHONE")

        self.MY_SMTP_EMAIL = os.getenv("MY_SMTP_EMAIL")
        self.MY_EMAIL = os.getenv("MY_EMAIL")
        self.MY_APP_PASSWORD_EMAIL = os.getenv("MY_APP_PASSWORD_EMAIL")

    def send_message(self, lowest_prices):
        # Send sms
        # client = Client(self.TWILIO_SID, self.TWILIO_AUTH)
        #
        # sms_message = "Temos ótimas ofertas para suas viagens desejadas!!\n\n"
        # for flight in lowest_prices:
        #     sms_message += (f"Voo com destino a {flight.destination_city}, está por apenas R${flight.price}, "
        #                     f"garanta já sua passagem. Partida, de {flight.origin_city} "
        #                     f"aeroporto de {flight.origin_airport}, "
        #                     f"ida dia {flight.out_date} e volta dia {flight.return_date}."
        #                     f"\nAcesse o link para saber mais: {flight.link}\n\n")

        #
        # message = client.messages \
        #     .create(
        #     body=sms_message,
        #     from_=self.TWILIO_PHONE,
        #     to=self.MY_PHONE
        # )
        #
        # print(message.status)
        # Send Email
        from datetime import datetime

        html_flights = ""
        for flight in lowest_prices:
            out_date = datetime.strptime(flight.out_date, '%Y-%m-%d')
            return_date = datetime.strptime(flight.return_date, '%Y-%m-%d')

            html_flights += (f"<div>"
                             f"<p style='font-size: 18px;'>Voo com destino a <strong>{flight.destination_city}</strong>, está por apenas <strong>R${flight.price}</strong>, "
                             f"garanta já sua passagem. Partida de <strong>{flight.origin_city}</strong>, aeroporto de <strong>{flight.origin_airport}</strong>, "
                             f"ida dia {out_date.strftime('%d/%m/%Y')} e volta dia {return_date.strftime('%d/%m/%Y')}."
                             f"</p>"
                             f"<a href={flight.link} style='color: white;'>"
                             f"Saiba Mais"
                             f"</a>"
                             "</div>"
                             "<hr>")

        html_text = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Promoção de Passagens</title>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        background-color: #f4f4f4;
                        padding: 20px;
                    }}
                    .container {{
                        max-width: 600px;
                        margin: auto;
                        background: #fff;
                        padding: 20px;
                        border-radius: 10px;
                        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    }}
                    h1 {{
                        color: #007bff;
                    }}
                    p {{
                        color: #333;
                    }}
                    strong {{
                        font-weight: bold;
                    }}
                    a {{
                        display: inline-block;
                        background-color: #007bff;
                        color: #fff;
                        text-decoration: none;
                        padding: 10px 20px;
                        border-radius: 5px;
                        transition: background-color 0.3s;
                    }}
                    a:hover {{
                        cursor: pointer;
                        background-color: #0056b3;
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>Promoção de Passagens</h1>
                    {html_flights}
                </div>
            </body>
            </html>
        """

        msg = MIMEMultipart('alternative')
        msg['From'] = self.MY_EMAIL
        msg['To'] = self.MY_EMAIL
        msg['Subject'] = "Promoção de Passagens"

        msg.attach(MIMEText(html_text, 'html'))
        with smtplib.SMTP(self.MY_SMTP_EMAIL, port=587) as connection:
            connection.starttls()
            connection.login(self.MY_EMAIL, self.MY_APP_PASSWORD_EMAIL)
            connection.sendmail(from_addr=self.MY_EMAIL,
                                to_addrs=self.MY_EMAIL,
                                msg=msg.as_string())
