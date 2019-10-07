from turtle import *
import time


pen1=Pen()
pen1.screen.bgcolor("Black")

#Bottom
turtle=Turtle()
turtle.up()
turtle.goto(0,-260)
turtle.down()
turtle.color("White")
turtle.width(width=2)
turtle.circle(100)
turtle.hideturtle()

#Centre
turtle=Turtle()
turtle.up()
turtle.goto(0,-60)
turtle.down()
turtle.color("White")
turtle.width(width=2)
turtle.circle(80)
turtle.hideturtle()

#Top
turtle=Turtle()
turtle.up()
turtle.goto(0,100)
turtle.down()
turtle.color("White")
turtle.width(width=2)
turtle.circle(60)
turtle.hideturtle()

#Right Eye
turtle.up()
turtle.goto(20,180)
turtle.down()
turtle.color("White")
turtle.width(width=2)
turtle.circle(5)
turtle.hideturtle()

#Left Eye
turtle.up()
turtle.goto(-9,180)
turtle.down()
turtle.color("White")
turtle.width(width=2)
turtle.circle(5)
turtle.hideturtle()

#Right Smile
turtle.up()
turtle.goto(-5,140)
turtle.down()
turtle.circle(30,50)

#Left Smile
turtle.up()
turtle.setheading(180)
turtle.goto(-5,140)
turtle.down()
turtle.circle(-30,50)

time.sleep(2)
turtle.getscreen().bye()
