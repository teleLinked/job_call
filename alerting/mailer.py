import smtplib
from email.message import EmailMessage

from . import FORMATTED_TEXT_ALERT


def send_mail(data):
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
    message['From'] = FROM_EMAIL
    message['To'] = TO_EMAIL

    s = smtplib.SMTP('localhost')
    s.send_message(message)
    s.quit()
    return 1
