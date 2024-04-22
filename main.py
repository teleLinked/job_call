import alerting
import alerting.mailer
import alerting.telegram


def main():
    """ main function to run script """
    alerting.mailer.send_mail(data={
        'platform': 'test',
        'title': 'test',
        'category': 'test',
        'description': 'test',
        'location': 'test',
        'date': 'now'
    })

    alerting.telegram.send_alert(data={
        'platform': 'test',
        'title': 'test',
        'category': 'test',
        'description': 'test',
        'location': 'test',
        'date': 'now'
    })



if __name__ == "__main__":
    main()
