##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's
# actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

# 5. Colocar na nuvem: https://www.pythonanywhere.com/

import datetime as dt
import pandas
import random
import smtplib

MY_EMAIL = "lhtestepython@gmail.com"
PASSWORD = "lh109925"


def send_email(email_addrs, msg):
    with smtplib.SMTP("smtp.gmail.com") as connection:  # Endereço SMTP do meu servidor de email
        connection.starttls()  # Aplica segurança a conexão
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=email_addrs,
                            msg=f"Subject:Happy Birthday!!\n\n{msg}")


TODAY = dt.datetime(year=2021, month=2, day=9)
letter_list = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

try:
    data = pandas.read_csv("birthdays.csv")  # Gera um DataFrame
    # print(data)
    new_data = data.to_dict(orient="records")
    for i in new_data:  # Percorrendo meu dicionário
        if TODAY.month == i["month"] and TODAY.day == i["day"]:
            file_name = random.choice(letter_list)
            with open(f"letter_templates/{file_name}", mode="r") as file:
                message = file.read()
                message = message.replace("[NAME]", i["name"])
                send_email(i["email"], message)
except FileNotFoundError as error:
    print(error)





