def press_y_to_exit():
    key = "n"
    while key != "y":
        def print_name(param_name, param_surname):
            print(f"Hi {param_surname}, {param_name} ")

        name = input("What is your name?\n")
        surname = input("What is your surname?\n")

        print("Passando os argumentos respeitando o POSITIONAL")
        print_name(name, surname)

        print("Passando os argumentos respeitando o KEYWORD ARGUMENT")
        print_name(param_surname=surname, param_name=name)

        key = input("press y to exit\n")


press_y_to_exit()
