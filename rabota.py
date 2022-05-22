x=input('Язык программирования: ')
y=int(input('Возраст: '))
a=int(input('Опыт: '))
b=int(input('Желаемая зарплата'))
p='python'
j='java'
js='javascript'
age=18
zp=60000
if (x==p or x==j or  x==js) and( 65>=y>=age) and( b<=zp) and( a>=3):
	print('Вы приняты на работу!')
else :
	print('Мы вам позвоним)')
