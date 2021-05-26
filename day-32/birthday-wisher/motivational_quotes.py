import datetime as dt
import random
import smtplib

my_email = "lhtestepython@gmail.com"
password = "lh109925"
day_of_week = dt.datetime.now().weekday()
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

try:
    with open("quotes.txt", mode="r") as data:
        quotes = data.readlines()
        quote = random.choice(quotes)
        print(quote)
except FileNotFoundError as error_message:
    print(error_message)


subject = f"Here comes your motivational message from {weekdays[day_of_week]}"
with smtplib.SMTP("smtp.gmail.com") as connection:  # Endereço SMTP do meu servidor de email
    connection.starttls()  # Aplica segurança a conexão
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="lhtestepython@yahoo.com",
                        msg=f"Subject:{subject}\n\n{quote}")