import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv

class EmailSend:
    
    def __init__(self) -> None:
        self.__server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        self.__user_login = self.__get_credential()[0]
        self.__user_password = self.__get_credential()[1]
        self.__server.login(self.__user_login,  self.__user_password)

    def __get_credential(self):
        with open("credentials.csv", newline='') as csvfile:
            file = csv.reader(csvfile, delimiter=",")
            credentials = [i for i in file][0]
            return credentials
            
    
    def send_email(self, message, email):
        email_msg = MIMEMultipart()
        email_msg['From'] = self.__user_login
        email_msg['To'] = email
        email_msg['Subject'] = 'Agendamento Confirmado'

        email_msg.attach(MIMEText(message, 'plain'))

        self.__server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
        self.__server.quit()