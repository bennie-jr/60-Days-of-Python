import smtplib
import imghdr
from email.message import EmailMessage
from dotenv import load_dotenv
import os


load_dotenv(override=True)

def send_email(image_path):
    print("send email function started")

    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    receiver = os.getenv("RECEIVER")

    email_message = EmailMessage()
    email_message["Subject"] = "Someone showed up!"
    email_message.set_content("Hey, someone entered your office space")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(username, password)    
    gmail.sendmail(username, receiver, email_message.as_string())
    gmail.quit()

    print("send email function ended")


if __name__ == "__main__":
    send_email(image_path="images/1.png")