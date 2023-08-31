import smtplib
import os
from email.message import EmailMessage
# https://docs.python.org/3/library/email.mime.html

def contact_me_email(contact_email, message):
    # Secret values need to be added to perm environment variables
    USERNAME = os.getenv("PY_USERNAME")
    PASSWORD = os.getenv("PY_PASSWORD")
    # RECIVER added for re-usability
    RECIEVER = os.getenv("PY_USERNAME")

    msg = EmailMessage()
    msg['Subject'] = "PythonShowcase"
    msg['From'] = USERNAME
    msg['To'] = RECIEVER

    html = f'''
    <html>
        <body>
            <h3>
                {contact_email}
                <br>
            </h3>
            <p>
                Message:
                <br>
                {message}
            </p>
        </body>
    </html>
    '''

    msg.set_content(html, subtype="html")

    # Send the message via gmail's regular server, over SSL:
    s = smtplib.SMTP_SSL('smtp.gmail.com')
    with smtplib.SMTP_SSL('smtp.gmail.com') as s:
        # uncomment == DEBUG
        s.set_debuglevel(1)
        s.login(USERNAME, PASSWORD)
        s.send_message(msg)

if __name__ == "__main__":
    try:
        contact_me_email("test@ChrisHarris.uk", "<br>Testing<br>")
    except:
        print("Email sending failed, set debug via 's.set_debuglevel(1)'")
        print('REMINDER: Export secrets locally')