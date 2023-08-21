import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def contact_me_email(contact_email, message):
    # Secret values need to be added to perm environment variables
    USERNAME = os.getenv("PY_USERNAME")
    PASSWORD = os.getenv("PY_PASSWORD")
    # RECIVER added for re-usability
    RECIEVER = os.getenv("PY_USERNAME")

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "PythonShowcase"
    msg['From'] = USERNAME
    msg['To'] = RECIEVER

    html = f'<html><body><h3>{contact_email}</h3></br><p>Message:</br>{message}</p></body></html>'
    email_body = MIMEText(html, 'html')

    msg.attach(email_body)

    # Send the message via gmail's regular server, over SSL:
    s = smtplib.SMTP_SSL('smtp.gmail.com')

    # uncomment if interested in the actual smtp conversation - DEBUG
    # s.set_debuglevel(1)

    s.login(USERNAME, PASSWORD)
    s.sendmail(USERNAME, RECIEVER, msg.as_string())
    s.quit()