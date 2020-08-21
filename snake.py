import turtle
import random
import time

#score variables
score = 0
high_score = 0

#setup the screen
widow = turtle.Screen()
widow.title("Snake Game")
widow.bgcolor("Black")
widow.setup(width=600, height=600)
widow.tracer(0)

snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("Blue")
snake.width(-1)
snake.penup()
snake.direction = "stop"

#Food

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("Red")
food.penup()
food.goto(0,100)

segments= []

#Score Board
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score:0 HighScore:0",align="center",font=("arial",24,"normal"))

#functions
def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)
    elif snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    elif snake.direction == "right":
        y = snake.xcor()
        snake.setx(y + 20)
    elif snake.direction == "left":
        y = snake.xcor()
        snake.setx(y - 20)

def up():
    if snake.direction!="down":
        snake.direction = "up"
def down():
    if snake.direction!="up":
        snake.direction = "down"
def right():
    if snake.direction!="left":
        snake.direction = "right"
def left():
    if snake.direction!="right":
        snake.direction = "left"
    
widow.listen()
widow.onkeypress(up,"Up")
widow.onkeypress(up,"w")
widow.onkeypress(down,"Down")
widow.onkeypress(down,"s")
widow.onkeypress(right,"Right")
widow.onkeypress(right,"d")
widow.onkeypress(left,"Left")
widow.onkeypress(left,"a")



while True:
    
    widow.update()
    #Border Collision
    if snake.xcor()>290 or snake.xcor()<-290 or snake.ycor()>290 or snake.ycor()<-290:
        time.sleep(1)
        snake.goto(0, 0)
        snake.direction = "stop"
        for seg in segments:
            seg.goto(1000,1000)
        segments.clear()
        #reset score
        score = 0
        pen.clear()
        pen.write("Score:{} Highscore:{}".format(score, high_score), align = "center", font=("arial",24,"normal"))
        
    move()
    #Body Collision
    for segment in segments:
        if segment.distance(snake)<20:
            time.sleep(1)
            snake.goto(0, 0)
            snake.direction = "stop"
            for seg in segments:
                seg.goto(1000, 1000)
            segments.clear()
            score = 0
            pen.clear()
            pen.write("Score:{} Highscore:{}".format(score, high_score), align = "center", font=("arial",24,"normal"))
   
            
        
    #check snake eats food or not
    if snake.distance(food) < 20:
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x, y)
        #growing snake
        snakebody = turtle.Turtle()
        snakebody.speed(0)
        snakebody.color("Blue")
        snakebody.shape("square")
        snakebody.penup()
        segments.append(snakebody)
        #score
        score+=10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score:{} Highscore:{}".format(score, high_score), align = "center", font=("arial",24,"normal"))
        
    #making snake body
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = snake.xcor()
        y = snake.ycor()
        segments[0].goto(x, y)
    
    #snake speed
    time.sleep(0.1)



widow.mainloop()
