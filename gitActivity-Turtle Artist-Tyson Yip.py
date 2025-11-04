# Recursion
# Author: Tyson
# October 28 2025

# Create a program that draws an awesome flower
import turtle

# Setting up the position

screen = turtle.Screen()
t = turtle.Turtle()
t.left(90)
t.penup()
t.goto(0, 0)
t.color("red")
t.width(10)
t.shape("arrow")

screen.setup(width=800, height=600, startx=0, starty= 0)
screen.bgcolor("lightblue")

# Drawing the petals
def draw_flowerpetal(level: int, branch_length: float):
    t.pendown()
    for _ in range(5):
        t.left(120)
        t.circle(120, 100)
        t.left(120)
        t.circle(120, 100)


draw_flowerpetal(5, 1)

# Draw a circle
t.penup()
t.setheading(0)
t.goto(-50, -100)
t.pendown()
t.begin_fill()
t.color("black")
t.circle(20)
t.end_fill()
screen.exitonclick()
