from art import logo

print(logo)


# Add
def add(n1, n2):
    # o uso de 3 " cria uma docstring
    """ Função soma """
    return n1 + n2


# Subtract
def subtract(n1, n2):
    """ Função subtração """
    return n1 - n2


# Multiply
def multiply(n1, n2):
    """ Função multiplicação """
    return n1 * n2


# Divide
def divide(n1, n2):
    """ Função divisão """
    return n1 / n2


# Estou usando um dictionary para "cadastrar" as operações, isso simplifica meu código caso eu queira criar novas
# operações no futuro
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    should_continue = True
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the second number?: "))

        # INTERESSANTE! Ao invés de chamar a função diretamente, eu carrego ela dentro de uma varável e executo a
        # variável. Assim eu evito IF's no código!
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ").lower() == "y":
            num1 = answer
        else:
            should_continue = False
            # Este é um exemplo de recursion
            calculator()


calculator()













