import os
import smtplib, ssl


def send_email(message, sender):
    global host, port, username, password
    host = "smtp.gmail.com"
    port = 465
    admin = "xfarce1@gmail.com"
    password = os.getenv("PASSWORD")
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(admin, password)
        server.sendmail(from_addr=sender, to_addrs=admin, msg=message)


