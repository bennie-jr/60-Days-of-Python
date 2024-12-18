from dotenv import load_dotenv
import smtplib, ssl
import os

load_dotenv()

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "bensowahjr@gmail.com"
    password = os.getenv("PASSWORD")

    receiver = "bensowahjr@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)