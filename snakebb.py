import turtle
import time
import random

score=0
high_score=0

canvas=turtle.Screen()
canvas.title("Sanke Game")
canvas.setup(width=700,height=700)
canvas.bgcolor("#00bfff")
canvas.tracer(0) #turn off all animation

def go_up():
	if head.direction!="down":
		head.direction="up"


def go_down():

	if head.direction!="up":
		head.direction="down"


def go_left():
	if head.direction!="right":
		head.direction="left"


def go_right():
	if head.direction!="left":
		head.direction="right"			

def move_snake():
	y=head.ycor()
	x=head.xcor()

	if head.direction=="up":
		head.sety(y+20)

	if head.direction=="down":
		head.sety(y-20)

	if head.direction=="right":
		head.setx(x+20)

	if head.direction=="left":
		head.setx(x-20)		

#head of the snake
head=turtle.Turtle()
head.speed(0)
#ToDo: change the shape to triangle and then move accordingly
head.shape("square")
head.color("black")
head.penup() #so that it doesn't draw anything
head.goto(0,0)
head.direction="stop"

#food 
food=turtle.Turtle()
food.speed(0)
#ToDo: change the shape to triangle and then move accordingly
food.shape("circle")
food.color("red")
food.penup() #so that it doesn't draw anything
food.goto(0,100)

#for displaying score
wr=turtle.Turtle()
wr.shape("square")#will not be visible
wr.speed(0)
wr.color("white")
wr.penup()
wr.direction="stop"
wr.hideturtle()
wr.goto(0,310)
wr.write("Score: 0 High Score: 0",align="center",font=("Courier",24,"normal"))

delay=0.1

segments=[]

#keyboard setup
canvas.listen()
canvas.onkeypress(go_up,"Up")
canvas.onkeypress(go_down,"Down")
canvas.onkeypress(go_right,"Right")
canvas.onkeypress(go_left,"Left")

while True:
	canvas.update()

	#check collision with canvas boundary
	if head.xcor()>340 or head.xcor()<-340 or head.ycor()>340 or head.ycor()<-340:
		head.goto(0,0)
		head.direction="stop"
		for segment in segments:
			segment.goto(1000,1000) #hide all the previous segments
		segments.clear()
		time.sleep(1)

		score=0 
		wr.clear()
		wr.write("Score: {} High Score: {}".format(score,high_score),align="center",font=("Courier",24,"normal"))	
		delay=0.1

	
	#check collision with food
	if head.distance(food)<20:
		x=random.randint(-340,340)
		y=random.randint(-340,340)
		food.goto(x,y)
	

		new_segment=turtle.Turtle()
		new_segment.speed(0)
		new_segment.color("gray")
		new_segment.penup()
		new_segment.shape("square")
		segments.append(new_segment)

		score+=10
		if score>high_score:
			high_score=score
		wr.clear()	
		wr.write("Score: {} High Score: {}".format(score,high_score),align="center",font=("Courier",24,"normal"))	

		#make the game faster
		delay-=0.001

	for i in range(len(segments)-1,0,-1):
		x=segments[i-1].xcor()
		y=segments[i-1].ycor()
		segments[i].goto(x,y)

	if len(segments)>0:
		x=head.xcor()
		y=head.ycor()
		segments[0].goto(x,y)
			
	move_snake()

	#check the collision of head with the body
	for segment in segments:
		if segment.distance(head)<20:
			time.sleep(1)
			head.goto(0,0)
			head.direction="stop"
			for segment in segments:
				segment.goto(1000,1000) #hide all the previous segments
		
			
			segments.clear()

			score=0
			wr.clear()
			wr.write("Score: {} High Score: {}".format(score,high_score),align="center",font=("Courier",24,"normal"))	

			#reset the delay
			delay=0.1



	time.sleep(delay)


canvas.mainloop()  # startover

