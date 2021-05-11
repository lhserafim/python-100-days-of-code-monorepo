# As classes utilizam o padrão PascalCase
class Classe:
    # O pass é como se fosse um retorno null
    pass


# No Python (assim como JS) posso ir adicionando atributos a minha classe

classe_1 = Classe()
classe_1.id = 109391
print(classe_1.id)


class User:
    # o __init__ é o construtor da classe no Python
    # o self é como se fosse o this
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0 # Valor default
        self.following = 0

    # Sempre que criamos um método em uma classe, precisamos do self
    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User(109391, "Luiz")

user_2 = User(109992, "Dani")
user_1.follow(user_2)

print(user_1.id)
print(user_1.username)
print(user_1.followers)
print(user_1.following)


print(user_2.id)
print(user_2.username)
print(user_2.followers)
print(user_2.following)
