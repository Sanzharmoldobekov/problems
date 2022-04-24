'''#1Problems
x=input('Vvedite: ')
la = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
for i in la:
	if x==i:
		print('this languages is in list') '
#2problem
la = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
for i in la:
	if i=='php':
		print('php')

#3problems
#Напишите код, который берёт цифру 7, умножает саму на себя же 5 раз.
x=7;
print(x*x*x*x*x)

#problems4
la = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
for i, item in enumerate(la):
    print(i + 1, item)

#problems5
i = 1
a = True
while True:
    if a == True:
        if i == 10:
            a = False
        else:
            print(i, end=" ")
            i += 1
    else:
        if i == 0:
            break
        print(i, end=" ")
        i -= 1


#problems 6
n=('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
for i in range(0, len(n), 2):
    print(n[i])

#problems7
n=('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан')
for i in range(1, len(n), 2):
    print(n[i])

'''
# problems 8
'''Есть переменная которая хранит в себе число:

 Необходимо написать следующие условия для проверки переменной:

    1. Это число трёхзначное?

     2. Это число положительное и чётное?

    3. Это число делится на 31 без остатка?

   4. Если это число больше 100 и оно делится на 17 без остатка или это число
 больше 150 и равно 13**2 тогда показать что это за число '''
x=int(input('Chislo-'))
if x >= 100:
	print('Это число трёхзначное')
elif x>0 and x%2==0:
	print('Это число положительное и чётное')
elif x%31==0:
	print('Это число делится на 31 без остатка')
elif x>100 and x%17==0 or x>150 and x==13**2:
	print(x)
