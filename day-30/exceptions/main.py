# Exception Handling

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:  # o else só é executado se o try for executado com sucesso
    content = file.read()
    print(content)
finally:  # o finally será executado de qualquer jeito!
    # o finally pode ser útil em situações como esta, que independente de qualquer coisa tenho que fechar o arquivo
    file.close()
    # raise TypeError("This is an error that I made up.")  # o raise é identico ao Raise do pl/sql

# BMI Example

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)
