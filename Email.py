import smtplib
import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr  
from email.header import Header

load_dotenv()


def send_alert(class_name, lec_name):
    email = os.getenv("SENDER_EMAIL")
    password = os.getenv("EMAIL_PASS")
    receiver_email = os.getenv("RECEIVER_EMAIL")


    message = MIMEMultipart("alternative")
    message["Subject"] = f"{class_name} {lec_name} - UCLA CLASS OPEN!!"
    message["From"] = formataddr((str(Header('Your fav hacker', 'utf-8')), 'sanyaisthebest@ucla.edu'))
    message["To"] = receiver_email

    try:
        with open("success_email.html", "r", encoding="utf-8") as f:
            html_content = f.read()
    except FileNotFoundError:
        print("missing file")
        exit()


    part = MIMEText(html_content, "html")
    message.attach(part)



    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(email, password)
            server.sendmail(email, receiver_email, message.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")


