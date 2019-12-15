asus=[]
users=[]
posts=[]
class  post ():
	def __init__(self, user, content):
		self.user=user
		self.content=content
	
	
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
		print(self.name+"email has add."+ email + " from  as freind_list")
	def remove_freind(self,email):
		
		self.freind_list.pop(email)
		print(self.name+" has remove"+email+"from as a freind_list")
	def add_posts(self,text):
		posts.append(post(self.posts,text))
		print(self.name+"has posted",text)
	def get_userInfo(self):
		print("___________________")
		print("Name:"+self.name)
		print("Email:"+self.email)
		print("Password:"+self.password)
		print("Freind:"+str(self.freind_list))	
		print("___________________")
user1=user("Ahmad "  ,  " Ahmad@mail.com"," i dont want to tell you my pass hhhhhhhh")
user2=user("fadi " , "fadi@gmail.com","123456a")
user1.add_freind(" sadeq")
user2.add_freind(" osama ")

user2.add_posts("  i am nerd:it mean i study all the time")
user1.add_posts("sadeq ,i love you,mustafa you too i love you, jenefir you too i love  you,and mosa ,and ahmed ,i love you all ")
user1.get_userInfo()
user2.get_userInfo()
user1.add_freind("  samer  ")
print(asus)


