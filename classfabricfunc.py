# Фабрика классов
def factory(aClass, *args, **kwargs): # Кортеж или словарь с переменным количеством аргументов
	return aClass(*args, **kwargs) # Вызывает aClass

class Spam:
	def doit(self, message):
		print(message)

class Person:
	def __init__(self, name=None, job=None):
		self.name = name
		self.job = job

if __name__ == "__main__":
	myObject = factory(Spam) # Создать объект Spam
	myObject2 = factory(Person, "Alex", "Developer") # Создать объект Person
	myObject3 = factory(Person)
	myObject4 = factory(Person, job="Engineer")
	myObject.doit("Hello")
	print(myObject2.name, myObject2.job)