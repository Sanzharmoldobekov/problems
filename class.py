'''Создайте класс Factory и внутри создайте 2 метода:

Метод engine который возвращает строку "Двигатель создан"

Метод bridge который возвращает строку "Ходовая часть создана"


class Factory:

    def engine(self):
        return ('двигатель создан')
    def brifge(self):
        return ('ходовая часть создана')

class B(Factory):
    pass
a=B()
print(a.engine())
print(a.brifge())
'''
class Factory:

    def engine(self):
        return ('двигатель создан')
    def brifge(self):
        return ('ходовая часть создана')

class Toyota(Factory):
    def wheels(self):
        return('Колеса готовы')
    def windows(self):
        return('стекла готовы')
a=Toyota()
print(a.engine())
print(a.brifge())
print((a.wheels(),a.windows()))

