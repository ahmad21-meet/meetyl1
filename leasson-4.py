import turtle
from turtle import Turtle
class ball(Turtle):
	def __init__ (self, r, color, dx,dy):
		Turtle.__init__(self)
		self.r=r
		self.dx=dx
		self.dy=dy
		self.size=r/10
		self.penup()
		self.color(color)
	def move(self, screen_width,screen_height):
		ouo_pos=turtle.xpos()
		ixs_pos=ouo_pos+dx
		myo_pos=turtle.ypos()
		iyo_pos=myo_pos+dy
		right_size_ball=ixs_pos+self.r
		left_size_ball=ixs_pos+-self.r
		up_size_ball=iyo_pos+self.r
		down_size_ball=iyo_pos-self.r
		turtle.goto(ixs_pos,iyo_pos)
		while right_size_ball >= screen_width :
			turtle.goto(turtle.xcor()-1,turtle.ycor())

		while left_size_ball<=screen_width :
			turtle.goto(turtle.xcor()+1,turtle.ycor())

		while up_size_ball>=screen_height :
			turtle.goto(turtle.xcor(),turtle.ycor()-1)

		while down_size_ball>=screen_height :
			turtle.goto(turtle.xcor(),turtle.ycor()+1)
screen_width=turtle.getcanvas().winfo_width()/2
screen_l	=turtle.getcanvas().winfo_height()/2

ball1=ball(25,"red",10,5)

	
ball1.move(screen_l,screen_width)


		
		
		
		






