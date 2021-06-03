from tkinter import *
from tkinter import messagebox  # O messagebox é um COMPONENTE e por isso precisa ser importado separadamente
from data_manager import DataManager


class View:
    def __init__(self):
        self.window = Tk()
        self.window.title("Flight Club")
        self.window.config(padx=20, pady=20)
        self.header_label = Label(text="Welcome to Luiz'z Flight Club.\nWe find the best flight deals and email you.")
        self.header_label.grid(column=1, row=1)

        self.first_name_label = Label(text="First Name")
        self.first_name_label.grid(column=1, row=2)
        self.first_name_entry = Entry(width=30)
        self.first_name_entry.grid(column=1, row=3)
        self.first_name_entry.insert(0, "Luiz")  # Só para começar com os dados populados na tela

        self.last_name_label = Label(text="Last Name")
        self.last_name_label.grid(column=1, row=4)
        self.last_name_entry = Entry(width=30)
        self.last_name_entry.grid(column=1, row=5)
        self.last_name_entry.insert(0, "Henrique")

        self.email_label = Label(text="Email")
        self.email_label.grid(column=1, row=6)
        self.email_entry = Entry(width=30)
        self.email_entry.grid(column=1, row=7)
        self.email_entry.insert(0, "lhserafim@gmail.com")

        self.submit_button = Button(text="Submit", command=self.submit)
        self.submit_button.grid(column=1, row=8)

        self.window.mainloop()

    def submit(self):
        data = DataManager()
        status = data.post_new_users(self.first_name_entry.get(),
                                     self.last_name_entry.get(),
                                     self.email_entry.get())
        if status == "success":
            messagebox.showinfo(title="Welcome Abord!", message=f"Dear {self.first_name_entry.get()},\n"
                                                                f"thank you for subscribing!")
        else:
            messagebox.showwarning(title="Error", message=status)
