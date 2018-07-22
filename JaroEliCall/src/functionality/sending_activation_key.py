import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("tt0815550@gmail.com", "AureliaK1609")

msg = "YOUR MESSAGE!"
server.sendmail("e.kaczmarek01@gmail.com", "tt0815550@gmail.com", msg)
server.quit()