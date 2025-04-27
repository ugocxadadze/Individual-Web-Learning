from turtle import *
def draw_square():
    for i in range(4):
        forward(200)
        left(90)



color("red")
draw_square()
penup()
goto(-500,0)
pendown()
color("blue")
draw_square()
penup()
goto(-500,-500)
pendown()
color("green")
draw_square()

penup()
goto(0,-500)
pendown()
color("orange")
draw_square()


exitonclick()
