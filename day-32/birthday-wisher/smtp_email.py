import smtplib

MY_EMAIL = "lhtestepython@gmail.com"
PASSWORD = "lh109925"
PASSWORD_YAHOO_TOKEN = "ogwptiaknnxeftvx"  # caso eu precise enviar pelo Yahoo.com

with smtplib.SMTP("smtp.gmail.com") as connection:  # Endereço SMTP do meu servidor de email
    connection.starttls()  # Aplica segurança a conexão
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL,
                        to_addrs="lhtestepython@yahoo.com",
                        msg="Subject:Hello\n\nThis is the body of my email.")
    # connection.close() # como usei o with, não preciso fechar a conexão!
