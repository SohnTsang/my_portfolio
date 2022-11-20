import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "xfarce1@gmail.com"
password = "iodhbqqcmcdfryuk"
receiver = "tsangkaho12@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: Hi!
Hello
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)

