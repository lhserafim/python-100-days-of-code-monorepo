import time

current_time = time.time()
# print(current_time)


def speed_calc_decorator(function):
    def wrapper_function():
        # Imprimir o nome da function
        function_name = function.__name__
        # Executar a function recebida como paramêtro
        function()
        end_time = time.time()
        # Achar em segundos o tempo gasto
        print(f"{function_name} time elapsed: {end_time - current_time}")

    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()

