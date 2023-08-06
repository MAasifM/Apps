import smtplib
import imghdr
from email.message import EmailMessage


class Email:

    def __init__(self):
        self.PASSWORD = "YOUR_PASSWORD"
        self.SENDER = "YOUR_EMAIL"
        self.RECEIVER = "RECEIVER'S EMAIL"

    def send_email(self, image_path):
        print("send_email function started")
        email_message = EmailMessage()
        email_message["Subject"] = "New customer showed up!"
        email_message.set_content("Hey, we just saw a new customer!")

        with open(image_path, "rb") as file:
            content = file.read()
        email_message.add_attachment(
            content, maintype="image", subtype=imghdr.what(None, content))

        gmail = smtplib.SMTP("smtp.gmail.com", 587)
        gmail.ehlo()
        gmail.starttls()
        gmail.login(self.SENDER, self.PASSWORD)
        gmail.sendmail(self.SENDER, self.RECEIVER, email_message.as_string())
        gmail.quit()
        print("send_email function ended")

    if __name__ == "__main__":
        send_email(image_path="images/19.png")