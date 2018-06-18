import turtle

turtle.left(90)

def drawSemiOver(nextNumber, r, dir):
    turtle.setheading(90)
    if dir == 0:
        #forward
        turtle.penup()
        turtle.setposition(nextNumber, 0)
        turtle.pendown()
        turtle.circle(r, 180)
        turtle.penup()
        turtle.setposition(nextNumber, 0)
        turtle.pendown()
    else:
        #backward
        turtle.circle(r, 180)

def drawSemiUnder(nextNumber, r, dir):
    turtle.setheading(270)
    if dir == 1:
        #         forward
        turtle.penup()
        turtle.setposition(nextNumber, 0)
        turtle.pendown()
        turtle.circle(r, 180)
        turtle.penup()
        turtle.setposition(nextNumber, 0)
        turtle.pendown()
    else:
        #         backward
        turtle.circle(r, 180)



turtle.exitonclick()
