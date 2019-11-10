class user(object):
	def __init__(self,name,email,password):
		self.name=name
		self.email=email
		self.password=password
		self.freind_list=[]
		self.posts=[]
	def add_freind(self,email):
		self.freind_list.append(email)
		print(self.name+"email has add"+email+ "from  as freind_list")
	def remove_freind(self,email):
		self.freind_list.pop(email)
		print(self.name+" has remove"+email+"from as a freind_list")
	def post(self,text):
		self.posts.append(text)
		print(self.name+"has posted",text)
	def get_userInfo(self):
		print("___________________")
		print("Name:"+self.name)
		print("Email:"+self.email)
		print("Password:"+self.password)
		print("Freind:"+str(self.freind_list))
		print("Posts:"+str(self.posts))
		print("___________________")
user1=user("lolo","ahmad@mail.com","pass1234")
user2=user("ames","ahmos@gmail.com","pass123456")
user1.add_freind("mosa")
user2.add_freind("meme")

user1.get_userInfo()
user2.get_userInfo()




