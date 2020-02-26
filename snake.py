import turtle
import time

delay = 0.15

window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("black")
window.setup(width=500 , height= 500)
window.tracer(0)


snakeHead = turtle.Turtle()
snakeHead.speed(0)
snakeHead.shape("square")
snakeHead.color("white")
snakeHead.penup()
snakeHead.goto(0,0)
snakeHead.direction = "stop"


def go_up():
	snakeHead.direction = "up"

def go_down():
	snakeHead.direction = "down"

def go_left():
	snakeHead.direction = "left"

def go_right():
	snakeHead.direction = "right"


def move():
	if (snakeHead.direction == "up"):
		y = snakeHead.ycor()
		snakeHead.sety(y+20)

	if (snakeHead.direction == "down"):
		y = snakeHead.ycor()
		snakeHead.sety(y-20)

	if (snakeHead.direction == "right"):
		x = snakeHead.xcor()
		snakeHead.setx(x+20)

	if (snakeHead.direction == "left"):
		x = snakeHead.xcor()
		snakeHead.setx(x-20)		

#key Binding
window.listen()
window.onkeypress(go_up, 'Up')
window.onkeypress(go_down, 'Down')
window.onkeypress(go_left, 'Left')
window.onkeypress(go_right, 'Right')


while True:
	window.update()
	move()
	time.sleep(delay)



window.mainloop()