#This program demonstrates turtle graphic drawings
#2/28/2020
#CTI-110 P2HW2 - Turtle Graphic
#Aaron Church

#This imports the turtle
import turtle

#To send the turtle off to the certain postition you must have it goto(_,_)
#then to draw a cirlce with a 45 degree
turtle.penup()
turtle.goto(-110,-25)
turtle.pendown()
turtle.circle(45)

#Change position of goto(_,_) to draw the second circle
turtle.penup()
turtle.goto(0,-25)
turtle.pendown()
turtle.circle(45)

#Same with the third circle
turtle.penup()
turtle.goto(110,-25)
turtle.pendown()
turtle.circle(45)

#Fourth circle
turtle.penup()
turtle.goto(-55,-75)
turtle.pendown()
turtle.circle(45)

#Fifth cirlce
turtle.penup()
turtle.goto(55,-75)
turtle.pendown()
turtle.circle(45)
