"""Данный скрипт поволяет отправлять письма на почту с помощью Питона.
В данном скрипте используются библиотеки из пакета"""

import smtplib # TODO почитать про библитоку
from config import PASSWORD
from email.mime.text import MIMEText # используется для создания текстовых объектов (позволяет отправлять кириллицу)

def send_mail(message):  # message - письмо, которое мы будем отправлять
    sender = "testpythonmailsenderauto@gmail.com"  # отправитель письма
    password = PASSWORD # соответственно пароль аккаунта отправителя

    server = smtplib.SMTP("smtp.gmail.com", 587)  # TODO выяснить откуда номер порта
    server.starttls() # запуск шифрованного объекта по tlc

    try:
        # вызываем метод логин
        server.login(sender, password)
        msg = MIMEText(message)
        msg['Subject'] = "Смотри, что творит этот человек"
        server.sendmail(sender, sender, msg.as_string())
        # server.sendmail(sender, sender, f"Subject: CLICK ME PLEASE!\n {message}")  # в аргументах указывается отправитель, получатель и сообщение (для теста получатель я сам)
                                                                                   # f"Subject: CLICK ME PLEASE!\n {message}" - конструкция для указания заголовка
        return f"The message was sent successfully!"
    except Exception as _ex:
        return f"{_ex}\nCheck your login or password please!"

def main():
    message = input("Type your message: ")
    print(send_mail(message=message))

if __name__ == "__main__":
    main()
