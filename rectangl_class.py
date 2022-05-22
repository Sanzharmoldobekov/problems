'''Построить
класс для описания плоской геометрической фигуры: Rectangle (Прямоугольник.).
Классдолжен содержать:
Данные:длина и ширина прямоугольника
Методы для операций с данными:
Нахождения периметра, площади, изменения размеров, печати результата.
Написать
программу, демонстрирующую работу с этим классом. Программа должна содержать
меню, позволяющее осуществить проверку всех методов класса.'''
class Rectangle:
    def __init__(self,dlina,shirina):
        self.dlina = dlina
        self.shirina = shirina

    def perimetr(self):
        return 2*(self.dlina+self.shirina)

    def ploshad(self):
        return self.shirina*self.dlina

    def izmenenie(self,new_d,new_sh):
        self.dlina=new_d
        self.shirina=new_sh
        e=2*(self.dlina+self.shirina)
        e1=self.shirina*self.dlina
        return  e,e1
    def out(self):
       x=self.ploshad()
       y=self.perimetr()
       a=self.izmenenie(2,2)
       print('Периметр и площадь прямоугольника = ',a)
       print('ploshad=',x,'perimetr=',y)

v=Rectangle(3,5)

a=input('''1 метод по нахождению площади = plo
2 метод по нахождению периметра = per
3 метод измененый размер = izm
4 метод общий вывод = o
''')
if a=='plo':
    print('Площадь =',v.ploshad())
elif a=='per':
    print('Периметр =',v.perimetr())
elif a=='izm':
    print('Периметр и площадь прямоугольника = ',v.izmenenie(2,2))
elif a=='o':
    print(v.out())








