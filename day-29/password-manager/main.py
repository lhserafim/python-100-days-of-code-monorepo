from tkinter import *  # Curiosidade. O * só vai importar as classes, métodos e atributos
from tkinter import messagebox  # O messagebox é um COMPONENTE e por isso precisa ser importado separadamente
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    # Selecionando uma quantidade aleatória de letras, números e simbolos
    nr_letters = random.randint(8, 10)
    nr_numbers = random.randint(2, 4)
    nr_symbols = random.randint(2, 4)

    # Usando list comprehension list = [new_list for items in list]
    password_letters = [random.choice(letters) for _ in
                        range(nr_letters)]  # o simbolo _ é para indicar que a variável não é usada
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)

    # Usando for loop
    # password_list = []
    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)
    #
    # random.shuffle(password_list)
    #
    # password = ""
    # for char in password_list:
    #     password += char

    pyperclip.copy(password)  # Copia o texto gerado para a memória
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    new_data = {
        website_entry.get(): {
            "email": email_username_entry.get(),
            "password": password_entry.get()
        }
    }
    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showwarning(title="Atenção", message="Os campos precisam ser preenchidos")
    else:
        is_ok = messagebox.askokcancel(title=website_entry.get(), message=f"Você deseja salvar os dados da "
                                                                          f"entrada {website_entry.get()}")
        if is_ok:
            # mode="w" -> write
            # mode="a" -> append
            with open("data.txt", mode="a") as file:  # Gerando o arquivo texto
                file.write(f"{website_entry.get()} | {email_username_entry.get()} | {password_entry.get()}\n")
            try:
                # https://docs.python.org/3/library/json.html
                with open("data.json", mode="r") as data_file:
                    # Lendo o arquivo JSON
                    data = json.load(data_file)
                    print(data)
            except FileNotFoundError:
                with open("data.json", mode="w") as data_file:
                    # em caso de exceção, gerar um novo arquivo com new_data
                    json.dump(new_data, data_file, indent=4)
            else:
                # Atualizando o arquivo com os novos dados
                data.update(new_data)
                with open("data.json", mode="w") as data_file:
                    # Atualizando o arquivo com o data atualizado
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()


# -------------------------- FIND PASSWORD ---------------------------- #
def find_password():
    website = website_entry.get()
    with open("data.json", mode="r") as data_file:
        # Lendo o arquivo JSON
        data = json.load(data_file)
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showwarning(title="Não encontrado", message=f"Website {website} não encontrado.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image_logo)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
email_username_label = Label(text="Email/Username:")
password_label = Label(text="Password:")

# Labels grid
website_label.grid(row=1, column=0)
email_username_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=18)
email_username_entry = Entry(width=35)
email_username_entry.insert(0, "lhserafim@gmail.com")  # 0 é a posição inicial, poderia usar END também ou outras opções
password_entry = Entry(width=18)

# Entries grid
website_entry.grid(row=1, column=1)
website_entry.focus()
email_username_entry.grid(row=2, column=1, columnspan=2)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
add_button = Button(text="Add", width=33, command=save)
search_button = Button(text="Search", width=13, command=find_password)

# Buttons grid
generate_password_button.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2)
search_button.grid(row=1, column=2)

window.mainloop()
