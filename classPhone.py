'''а) Создайте класс Phone, который содержит атрибуты number, model и weight.
б) Создайте три экземпляра этого класса. 
в) Выведите на консоль значения их атрибутов. 
г) Добавить конструктор в класс Phone, который принимает на вход
три параметра для инициализации переменных класса - number, model и weight.
д) Создать метод sendMessage. Данный метод принимает на вход номера телефонов
которым будет отправлено сообщение. Метод выводит на консоль номера этих телефонов.
'''
class Phone:
	number='0709809999'
	model='xs max'
	weight=0.2
	def __init__(self,number,model,weight):
		self.weight = weight
		self.model = model
		self.number = number
	def sendMessage(self,x,y,z,n):
		return f'{x},{y},{z},{n}'

a = Phone
b = Phone
c = Phone
print('Модель - ',a.model)
print('Номер телефона - ',b.number)
print('Вес телефона - ',c.weight)
print('Номера телефонов на котрые будет отправлено сообщение:',c.sendMessage('0777342513','0808054850','090580','453845394','4534534534'))