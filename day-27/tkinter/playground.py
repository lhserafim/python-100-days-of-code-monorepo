def add(*args):
    # Argumentos ilimitados com *args
    # *args é posicional
    # O * é obrigatório. args é uma convenção, poderia ser qualquer coisa
    print(f" Valor na posição zero = {args[0]}")
    for n in args:
        print(n)


add(1, 2, 3, 4, 5)
add(1, 2, 3, 4, 5, 8, 10)


def calculate(**kwargs):
    # Argumentos ilimitados com **kwargs
    # **kwargs é key word args
    print(type(kwargs))  # gera um dicionário
    print(kwargs["add"])  # Posso acessar o valor assim, diretamente
    for key, value in kwargs.items():  # Ou fazendo o for loop padrão dos dicionários
        print(key)
        print(value)


calculate(add=3, multiply=5)


# usando **kwargs em uma classe
class Car:
    def __init__(self, **kw):
        # Posso chamar o atributo do **kwargs usando [] oiu .get(). A vantagem do .get() é que o argumento se torna
        # opcional!
        self.make = kw["make"]
        self.model = kw.get("model")


my_car = Car(make="Nissan")
print(my_car.model)  # vai retornar None, pq usei .get()

my_car2 = Car(make="Citroen", model="C4")
print(my_car2.model)
