class Animal:
	def __init__(self,sound,name,age,favorite_color):
			self.sound = sound 
			self.name = name 
			self.age = age 
			self.favorite_color = favorite_color
	def eat(self,food):
			print("yummy!! " + self.name + "is eating" + food)
	def description(self):
			print(self.name + " is  " + self.age + "years old and loves the color" + self.favorite_color)
	def make_sound(self):
		print("row!!" + " row!!"+"row!!")

lion1= Animal("arow","ahmad","3","blue")
lion1.eat("banana")
lion1.description()
lion1.make_sound()




class  Person:
	def __init__(self,name,age,city,gender,food):
			self.name = name
			self.age =age
			self.city = city
			self.gender = gender
			self.food = food

	def breakfast(self,food):
			print(self.food + "is" +"the food")



Person1=Person("yousef","15","jerusalem","male","milk")
Person1.breakfast("milk")

