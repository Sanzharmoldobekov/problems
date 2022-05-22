'''a) поля fullName, age, place(address)
б) метод talk(), в которых просто вывести на консоль сообщение -"Такой-то  Person говорит". Метод

move()  будет менять его адрес
в) Добавьте  конструктор  с тремя параметрами fullName, address, age = 18
г) Настроить  метод __str__  (Сделать отображение всех полей объекта)'''
class Person:
    def __init__(self,fullname,addres,age=18):
        self.fullname=fullname
        self.addres=addres
        self.age=age
    def talk(self):
        print(self.fullname,'говорит')
    def move(self,n='new adres'):
        self.addres=n
        return f'{self.fullname},{self.addres},{self.age}'
    def __str__(self):
        return f'{self.fullname},{self.addres},{self.age}'

e=Person('Молдобеков Санжар','Тунгуч',21)
print(e.__str__())
e.talk()
e.move()
print(e.move())
