from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def contact():
    message = Mail(
        from_email='cap5192@icloud.com',
        to_emails='cap5192@gmail.com',
        subject='New Message',
        html_content='msg')

    sg = SendGridAPIClient('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')
    response = sg.send(message)
contact()