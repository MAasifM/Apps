import requests
import selectorlib
import smtplib
import ssl
import sqlite3
import os


class Data:
    def __init__(self):
        self._URL = "http://programmer100.pythonanywhere.com/tours/"
        self._HEADERS = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        self._connection = sqlite3.connect("data.db")

    def scrape(self, url):
        """Scrape the page source from the URL"""
        response = requests.get(url, headers=self._HEADERS)
        source = response.text
        return source

    def extract(self, source):
        extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
        value = extractor.extract(source)["tours"]
        return value

    def send_email(self, message, username="someone@email.com", password="*****", receiver="other@email.com", host="smtp.gmail.com", port=465):
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, message)
        print("Email was sent!")

    def store(self, extracted):
        row = extracted.split(",")
        row = [item.strip() for item in row]
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO events VALUES(?,?,?)", row)
        self._connection.commit()

    def read(self, extracted):
        row = extracted.split(",")
        row = [item.strip() for item in row]
        band, city, date = row
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT * FROM events WHERE band=? AND city=? AND date=?", (band, city, date))
        rows = cursor.fetchall()
        print(rows)
        return rows
