"""Данный скрипт поволяет отправлять письма на почту с помощью Питона.
В данном скрипте используются библиотеки из пакета"""

import smtplib # TODO почитать про библитоку
from config import PASSWORD
from email.mime.text import MIMEText # используется для создания текстовых объектов (позволяет отправлять кириллицу)
from email.mime.multipart import MIMEMultipart # позволяет создавать составные сообщения (то есть прикреплять к письму разные части, то есть текс, html шаблон или какой-то файл)


def send_mail():  # message - письмо, которое мы будем отправлять
    sender = "testpythonmailsenderauto@gmail.com"  # отправитель письма
    password = PASSWORD # соответственно пароль аккаунта отправителя

    server = smtplib.SMTP("smtp.gmail.com", 587)  # TODO выяснить откуда номер порта
    server.starttls() # запуск шифрованного объекта по tlc

    # text = """
    # <!DOCTYPE html>
    # <html lang="en">
    # <head>
    #     <meta charset="UTF-8">
    #     <title>Title</title>
    # </head>
    # <body>
    #   <h1 style="color: green;">Привет мир!!!</h1>
    #   <span><u>Как ваши  дела земляне?</  u></span>
    # </body>
    # </html>
    # """

    try:
        with open("index.html", 'r') as file:
            template = file.read()
    except IOError:
        return f"the template file dosn't found!  "

    try:
        # вызываем метод логин
        server.login(sender, password)
        # msg = MIMEText(template, "html")
        msg = MIMEMultipart() # объект сообщение файл
        msg["From"] = sender
        msg["To"] = sender
        msg['Subject'] = "Я люблю тестироваться"

        msg.attach(MIMEText("Йоу чувак!"))
        msg.attach(MIMEText(template, "html"))


        with open("открой меня если сможешь.txt") as f:
            file = MIMEText(f.read())

        file.add_header('content-disposition', 'attachment', filename='открой меня если сможешь.txt')
        msg.attach(file)

        server.sendmail(sender, sender, msg.as_string())
        # server.sendmail(sender, sender, f"Subject: CLICK ME PLEASE!\n {message}")  # в аргументах указывается отправитель, получатель и сообщение (для теста получатель я сам)
                                                                                   # f"Subject: CLICK ME PLEASE!\n {message}" - конструкция для указания заголовка
        return f"The message was sent successfully!"
    except Exception as _ex:
        return f"{_ex}\nCheck your login or password please!"

def main():
    print(send_mail())

if __name__ == "__main__":
    main()
