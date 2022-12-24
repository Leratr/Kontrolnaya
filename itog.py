class Babchenok:
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        if name == 'Олег':
            self.name = name
        else:
            self.name = f'Я не {name}, а Олег!!!'
            self.age = age


ivan = Babchenok("Иван",31)
kolyn = Babchenok("Николай", 14)
print(ivan.name)
print(kolyn.name)