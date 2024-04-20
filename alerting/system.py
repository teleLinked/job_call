from notify import notification

from . import FORMATTED_TEXT_ALERT


def send_notification(data):
    notification("New Job Alert!", FORMATTED_TEXT_ALERT.format(
        platform=data['platform'],
        title=data['title'],
        category=data['category'],
        description=data['description'],
        location=data['location'],
        date=data['date'],
    ))
    return 1
