import smtplib
import ssl
import os
from dotenv import load_dotenv

# turn on 2FA and generate a special app password in gmail
# store it in .env
load_dotenv()
PW = os.getenv('GMAIL_PW')


# send_email arguments:
# recipient - str - recipient's email address
# subject - str - subject line of email
# body - str - body of email
def send_email(recipient, subj, body):

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender = "ravenscroft.us.engineering@gmail.com"

    msg = f"From: {sender}\nTo: {recipient}\nSubject: {subj}\n\n{body}"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.ehlo()
        server.login(sender, PW)
        server.sendmail(sender, recipient, msg)
