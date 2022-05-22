import random

names = ['John', 'Alex', 'Marty', 'Tilek', 'Kairat', 'Alina', 'DAstan']


class Solidare:
    def __init__(self):
        self.id = random.randint(1000, 9999)

    def __repr__(self):
        return f'{self.id}'


class Hero(Solidare):
    def __init__(self):
        self.id = random.randint(1000, 9999)
        self.name = random.choice(names)
        self.lvl = 1

    def lvl_up(self):
        self.lvl += 1
        return f'Герой {self.name} - {self.id} поднял уровень - {self.lvl}'

    def __repr__(self):
        return f'{self.name} {self.id} - {self.lvl}'

a = int(input('Напишите сколько будет героев '))
b = int(input('Напишите сколько будет солдат '))

list_hero = [[Hero()] for i in range(a)]

for i in range(b):
    list_hero[random.randint(0, a-1)].append(Solidare())


list_hero.sort(key=len)

for i in range(len(list_hero)):
    for j in range(i):
        print(list_hero[i][0].lvl_up())

print(list_hero)

# Unit = Hero()
# print(Unit.lvl_up())