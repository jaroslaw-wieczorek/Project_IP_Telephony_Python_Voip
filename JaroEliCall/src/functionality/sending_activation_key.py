
from itsdangerous import URLSafeTimedSerializer
from flask_mail import Message
from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
mail = Mail(app)


class SendingActivationKey:
    def send_email(to, subject, template):
        msg = Message(
            subject,
            recipients=[to],
            html=template,
            sender=app.config['MAIL_DEFAULT_SENDER']
        )
        mail.send(msg)



def index():
    msg = Message("Hello",
                  sender="from@example.com",
                  recipients=["to@example.com"])

    assert msg.sender == "Me <me@example.com>"
    msg.body = "testing"
    msg.html = "<b>testing</b>"
    mail.send(msg)


index()

