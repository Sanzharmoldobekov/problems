'''Написать Функцию которая принимает предложение как аргумент,
считает количество букв и возвращает сколько символов он ввёл.
НЕ ИСПОЛЬЗОВАТЬ функцию len()'''

#Напишите функцию которая принимает 2 Dictionary и добавляет втрорую Dictionary к первой.
def kley(b,**a):
    x = a.copy()
    x.update(b)
    return  x
'''Cat Years
    15 cat years for first year
    +9 cat years for second year
    +4 cat years for each year after that
Dog Years
    15 dog years for first year
    +9 dog years for second year
    +5 dog years for each year after that'''
def years(h,c,d):
    if h==1 :
        c==15
        d==15
    elif h==2:
        c==24
        d==24
    elif h>=3:
        c=24
        d=24




