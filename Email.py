import smtplib
import os
from dotenv import load_dotenv

load_dotenv()


def send_alert(new_value):
    email = os.getenv("SENDER_EMAIL")
    password = os.getenv("EMAIL_PASS")

    subject = "UCLA Alert - Spot Open!!"
    body = f"The tracked number has changed from zero. Current value: {new_value}"

    msg = f"Subject: {subject}\n\n{body}"

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(email, password)
            server.sendmail(email, email, msg)
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")
