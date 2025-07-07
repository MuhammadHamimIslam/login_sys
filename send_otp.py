import os
from dotenv import load_dotenv
from email.message import EmailMessage 
import ssl
import smtplib
import secrets

load_dotenv()

email_sender = os.getenv("EMAIL_SENDER")
email_password = os.getenv("APP_PASSWORD")

def send_otp(email_receiver):
    otp_code = "".join(str(secrets.randbelow(10)) for _ in range(6))
    email_body = f"""
Your otp is {otp_code} to sign up for pyTest.
If It's not you, You can simply ignore this email.
Stay secure,
pyTest by Muhammad Hamim Islam ©2025
"""
    # setup for sending email 
    em = EmailMessage()
    em["From"] = email_sender
    em["To"] = email_receiver
    em["Subject"] = "Otp verification from pyTest"
    em.set_content(email_body)
    # setting email context 
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context, timeout=15) as smtp: 
            # login to the sender Gmail account 
            smtp.login(email_sender, email_password)
            # now send the email to the receiver
            smtp.send_message(em)
    except Exception as e:
        print(e)