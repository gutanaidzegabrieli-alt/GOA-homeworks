from turtle import *


#we want to paint a house

#step 1:   draw a square
speed(30)
color("purple")
width(7)
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square
#drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(110)    #height of the door
right(90)
forward(60)
right(90)
forward(110)
end_fill()


penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#end of the roof
#drawing the windows

penup()
goto(30, 170)
pendown()

color("blue")
left(30)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)

penup()
goto(30, 150)
pendown()

left(180)
forward(40)

penup()
goto(50, 170)
pendown()

right(90)
forward(40)

penup()
goto(160, 170)
pendown()

forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)

penup()
goto(140, 170)
pendown()

right(90)
forward(40)

penup()
goto(160, 150)
pendown()

right(90)
forward(40)

exitonclick()


