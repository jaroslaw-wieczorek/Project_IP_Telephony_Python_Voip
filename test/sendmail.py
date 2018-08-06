import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

activ_code = 55355

me = "Iam@hacker.com"
#me = "jaroslaw.k.wieczorek@student.put.poznan.pl"

msg = MIMEMultipart()
#me = "e.kaczmarek01@gmail.com"
#to = "arkadiusz.wieczorek@sealcode.org"
to = "jaroslaw.wieczorek@sealcode.org"


msg['Subject'] = 'JaroEliCall: kod aktywacyjny użytkownika'
msg['From'] = me
msg['To'] = to

body_text = "Informacja: Aby zakończyć rejestracje należy użyć " \
            "poniższego kodu jako hasła.\n\n### Kod aktywacyjny do " \
            "konta: " + str(activ_code) + " ### \n" \
            "Prosimy nie odpowiadać na tą wiadomość"

msg.attach(MIMEText(body_text, 'plain'))

server = smtplib.SMTP("localhost")
server.ehlo()
#server.starttls()
#print("Set debug")
#server.set_debuglevel(True)
server.sendmail(to, me, msg.as_string())

print("SENDED EMAIL!!!", msg['From'], msg['To'], msg.as_string())

server.quit()
