import turtle

#@shape drawing programing of turtle by Ayan Upadhaya

#key commands
#left arrow -for left drawing
#right arrow- for right drawing
#up arrow - for up drawing
#down arrown- for down drawing
#x- to penup
#c- to pendown
#d- create eraser
#r- restet pen

#move the player left and right
def moveLeft():
	playerXPosition=playerx.xcor()
	vel=15
	playerx.setx(playerXPosition-vel)
	win.update()

def moveRight():
	playerXPosition=playerx.xcor()
	vel=15
	playerx.setx(playerXPosition+vel)
	win.update()
#move the player up and bottom

def moveUp():
	playerYPosition=playerx.ycor()
	vel=15
	playerx.sety(playerYPosition+vel)
	win.update()
def moveDown():
	playerYPosition=playerx.ycor()
	vel=15
	playerx.sety(playerYPosition-vel)
	win.update()

#to penup and pedown event

def notDraw():
	playerx.penup()

def draw():
	playerx.pendown()

#make the eraser

def eraser():
	playerx.color('black','white')
	
def reset():
	playerx.color('yellow','black')


#playerx profile

playerx=turtle.Turtle()
playerx.shape('triangle')
playerx.color('yellow')
playerx.goto(0,0)
playerx.setheading(90)
playerx.speed(0)

#Screen Profile
win=turtle.Screen()
win.title("Draw as you like")
win.bgcolor('black')
win.setup(width=600,height=600)
win.tracer(0)

#screen event listner

win.listen()
win.onkeypress(moveLeft,'Left')
win.onkeypress(moveRight,'Right')
win.onkeypress(moveUp,'Up')
win.onkeypress(moveDown,'Down')
win.onkeypress(notDraw,'x')
win.onkeypress(draw,'c')
win.onkeypress(eraser,'d')
win.onkeypress(reset,'r')

#keeps the screen on untill we close it.
win.mainloop()
