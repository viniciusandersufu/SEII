class Dog:
    def __init__(self, name):
        self.name = name
        print(name)

    def bark(self):
        print('bark')
    
    def add_one(self, x):
        return x + 1

d = Dog('Tim')
# Toda vez que um objeto for criado, um atributo precisa ser passado
# Retorna 'Tim'
