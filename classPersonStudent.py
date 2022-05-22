'''Создайте класс Person с атрибутами: имя и возраст строки типа.
Создайте метод display(), который отображает имя и возраст объекта, созданного с помощью класса Person.
Создайте дочерний класс Student, который наследуется от класса Person и также имеет атрибут раздела.
Создайте метод displayStudent(), который отображает имя, возраст и раздел объекта
,созданного с помощью класса Student.
Создайте объект Student через создание экземпляра в классе Student, а затем протестируйте метод displayStudent
'''
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age = age

    def display(self):
        print('Person name - ',self.name)
        print('Person age - ',self.age)


class Student(Person):
    def __init__(self,name,age,lesson):
        self.name = name
        self.age = age
        self.lesson = lesson
    def Studentdisplay(self):
        print('Student name - ',self.name)
        print('Age - ',self.age)
        print('Student section - ',self.lesson)

####################
P = Person("Tomas Wild", 37)
P.display()
S = Student("Albert", 23 , "Mathematics")
S.Studentdisplay()

#######ВЫХОД#######
'''
Person name :  Tomas Wild
Person age =  37
-------------------------------
Student name :  Albert
Student age =  23
Student section =  Mathematics
'''