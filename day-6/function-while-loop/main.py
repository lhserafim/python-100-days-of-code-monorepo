def print_name(name):
    print(f"Hi {name}")


name = input("What is your name?\n")

print_name(name)

###


def press_y_to_exit():
    key = "n"
    while key != "y":
        key = input("press y to exit\n")

press_y_to_exit()
