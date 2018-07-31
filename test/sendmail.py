import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

activ_code = 5555

to="my@email.org"

msg = MIMEMultipart()
me = "JaroEliCall"

msg['Subject'] = 'JaroEliCall: kod aktywacyjny użytkownika'
msg['From'] = me
msg['To'] = to

body_text = "Informacja: Aby zakończyć rejestracje należy użyć " \
            "poniższego kodu jako hasła.\n\n### Kod aktywacyjny do " \
            "konta: " + str(activ_code) + " ### \n" \
            "Prosimy nie odpowiadać na tą wiadomość"*100

msg.attach(MIMEText(body_text, 'plain'))

server = smtplib.SMTP("localhost")
server.starttls()
print("Set debug")
server.set_debuglevel(True)
server.sendmail(me, to, msg.as_string())
print("SENDED EMAIL!!!", me, to, msg.as_string())

server.quit()
