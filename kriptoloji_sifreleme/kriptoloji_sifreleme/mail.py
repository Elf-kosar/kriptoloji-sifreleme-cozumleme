import smtplib
from email.message import EmailMessage

def send_email(subject, body):
    sender_email = "elif.kosar.163@gmail.com"
    receiver_email = "ferayyaren22@gmail.com"
    password = "bqdt zzdu zjzs eqzs"  # Google hesabı için 'uygulama şifresi' kullan

    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, password)
        smtp.send_message(msg)
