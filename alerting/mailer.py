import smtplib
from email.message import EmailMessage

from decouple import config

from . import FORMATTED_TEXT_ALERT

EMAIL_FROM = config("EMAIL_FROM")
EMAIL_PASSWORD = config("EMAIL_PASSWORD")
EMAIL_HOST = config("EMAIL_HOST")
EMAIL_PORT = config("EMAIL_PORT")
EMAIL_USER = config("EMAIL_USER")


def send_mail(data):
    """ send alert with email smtp """
    message = EmailMessage()
    message.set_content(FORMATTED_TEXT_ALERT.format(
        platform=data['platform'],
        title=data['title'],
        category=data['category'],
        description=data['description'],
        location=data['location'],
        date=data['date'],
    ))
    message['Subject'] = 'New job alert!'
    message['From'] = EMAIL_FROM
    message['To'] = EMAIL_USER

    smtp = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
    smtp.starttls()
    smtp.login(EMAIL_FROM, EMAIL_PASSWORD)
    smtp.send_message(message)
    smtp.quit()
    return 1
