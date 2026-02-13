import smtplib
from email.message import EmailMessage
import os

def send_mail(sender_mail, app_password, receiver_mail, subject, body, attachment):

    msg = EmailMessage()

    msg['From'] = sender_mail
    msg['To'] = receiver_mail
    msg['Subject'] = subject

    msg.set_content(body)

    with open(attachment, "rb") as f:
        file_data = f.read()
        file_name = os.path.basename(attachment)

    msg.add_attachment(file_data,
                       maintype="application",
                       subtype="octet-stream",
                       filename=file_name)

    smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp.login(sender_mail, app_password)
    smtp.send_message(msg)
    smtp.quit()
