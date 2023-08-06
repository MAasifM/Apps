import smtplib
import ssl


class SendEmail:

    def __init__(self, host="smtp.gmail.com", port=465):
        self._host = host
        self._port = port

    def send_email(self, message, username="someone@email.com", password="*****", receiver="someone@email.com"):
        host = self._host
        port = self._port
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, message)
