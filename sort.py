shkola = {'1а':20, '1б':21, '6а':15, '7б':33}
print (shkola)
number = input ('Введите класс: ')
print('В этом классе учится', shkola[number], 'учеников')
a = shkola['1а'] + 3
b = shkola['2а'] - 2
c = shkola['2б'] + 1
shkola['1а'] = a
shkola['2а'] = b
shkola['2б'] = c
print (shkola) 
