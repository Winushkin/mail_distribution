import smtplib
from email.mime.text import MIMEText

def send_email(message, emails):
    sender: str = input("Введите email отправителя: ")
    password = input("Введите пароль сторонних приложений: ")
    mess = MIMEText(_text=message, _subtype="html")

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        print("port: 587")
    except smtplib.SMTPServerDisconnected:
        server = smtplib.SMTP("smtp.gmail.com", 465)
        print("port: 465")

    server.starttls()
    server.login(sender, password)
    for email in emails:
        try:

            server.sendmail(sender, email, bytes(mess))

            print("Сообщение отправлено")
        except Exception as _ex:
            print(f"Сообщение не отправлено\n{_ex} ")


def main():
    html_file = True
    emails_file = True
    while html_file:
        try:
            with open(input("html file path: "), "r") as f:
                print("[V]Файл найден")
                message = f.read()
                html_file = False
        except FileNotFoundError:
            print("[X]Файл не найден. Повторите попытку")

    while emails_file:
        try:
            with open(input("emails file path: "), "r") as f:
                print("[V]Файл найден")
                emails = [email for email in f.read().split(";")]
                emails_file = False
        except FileNotFoundError:
            print("[X]Файл не найден. Повторите попытку")

    print(send_email(message=message, emails=emails))


if __name__ == "__main__":
    main()
