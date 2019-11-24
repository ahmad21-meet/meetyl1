asus=[]
users=[]
posts=[]
class  post ():
	def __init__(self, user, content,date):
		self.user=user
		self.content=content
		self.date=date
	
class user(object):
	def __init__(self,name,email,password):
		self.name=name
		self.email=email
		self.password=password
		self.freind_list=[]
		self.posts=[]
		asus.append(self.name)
	def add_freind(self,email):
		self.freind_list.append(email)
		print(self.name+"email has add"+email+ "from  as freind_list")
	def remove_freind(self,email):
		self.freind_list.pop(email)
		print(self.name+" has remove"+email+"from as a freind_list")
	def add_posts(self,text):
		posts.append(post(self.posts,text,"date"))
		print(self.name+"has posted",text)

	def get_userInfo(self):
		print("___________________")
		print("Name:"+self.name)
		print("Email:"+self.email)
		print("Password:"+self.password)
		print("Freind:"+str(self.freind_list))
		
		print("___________________")
user1=user("lolo","ahmad@mail.com","pass1234")
user2=user("ames","ahmos@gmail.com","pass123456")
user1.add_freind("mosa")
user2.add_freind("meme")
user2.add_posts("tetot")
user2.add_posts("hi guys")
user1.get_userInfo()
user2.get_userInfo()

print(asus)
print(users)


