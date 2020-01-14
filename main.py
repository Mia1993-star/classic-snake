

import turtle
import time
import random

delay = 0.1

#Score
score = 0
high_score = 0

#Set up the screen
wn = turtle.Screen()
wn.title("Snake game")
wn.bgcolor("blue")
wn.setup(width=600, height=600)
wn.tracer(0) #turns of the screen update

#Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"


#Snake food
food = turtle.Turtle
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

#list is called segment
segment = []

#Pen 
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score:0 High Score 0", align="center", font=("Courier, 24, "normal"))

#Function
def go_up():
  if head.direction != "down":
  head.direction = "up"

def go_down():
  if head.direction !="up":
  head.direction = "down"

def go_left():
  if head.direction !="right":
  head.direction = "left"

def go_right():
  if head.direction !="left":
  head.direction = "right"


def move():
  if head.direction == "up":
    y= head.ycor()
    head.sety(y + 20)

  if head.direction == "down":
    y= head.ycor()
    head.sety(y - 20)

  if head.direction == "left":
   x= head.xcor()
    head.setx(x - 20)

  if head.direction == "right":
    x= head.xcor()
    head.setx(head.xcor() + 20)

#Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")


#Main game loop
while True:
  wn.update()

  # check for a collision with the border
  if head.xcor() >290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()-290:
    time.sleep(1)
    #makes game pauze 1 sec
    head.goto(0,0)
    head.direction = "stop"
  


  #check for a collision with the food
  if head.distance(food) < 20:
    #move food rando spot
    x = random.randint(-290, 290)
    y = random.randint(-290, 290)
    #food.goto(random.randint(-290, 290), random.randint(-290, 290))
    food.goto(x, y)
    
    #add a segment
    new_segment = turtl.Turtle()
    new_segment.speed(0)
    #animation speed
    new_segment.shape("square")
    new_segment.color("white")
    new_segment.penup()
    segment.append(new_segment)
    #this appends to the segment list above

    #Shorten the delay
    delay -= 0.001
    
    
    #Increase the score
    score += 10

    if score > high_score:
      hight_score = score
      
    pen.clear()
    #prevents the score writen on top of eachother 
    pen.write("Score: {} High Score: {}".format(score, high_score), align="center"),  font=("Courier, 24, "normal"))
    
#move the end segment first in reversed order
  for index in range(len(segment)-1, 0, -1)
  #lengt of the segment is 10 ut the list start at 0. 10 - = 9/each segment is a turtle 
    x = segments[index-1].xcor()
    y = segments[index-1].ycor()
    segments[index].goto(x, y)

    #move segment 0 to where the head is/meaning only if it goes over 0 which is 1 it reacts
    if len(segment) > 0:
    #finds out if there is a segment
      x = head.xcor()
      y = head.ycor()
      segment[0].goto(x,y)


  move()
  
  #check for head collision wit the body segments
  for segment in segments:
    if segment.distance(head) < 20:
      time.sleep(1)
      head.goto(0,0)
      head.direction = "stop"

    # hide the segment
    for segment in segments:
    #goes through the whole list
     segment.goto(1000, 1000)
      #mac way move it out of the screen

    #clear the segments list
    segment.clear()

    #Reset thhe score
    score = 0:

    #reset the delay
    delay = 0.1
    
    pen.clear()
    #prevents the score writen on top of eachother 
    pen.write("Score: {} High Score: {}".format(score, high_score), align="center"),  font=("Courier, 24, "normal"))


wn.mainloop()
