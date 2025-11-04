# Recursion
# Author: Ubial
# 20 ConnectionAbortedError

# Create a program that draws treess recursively
import turtle

# Set up the Environment

screen = turtle.Screen()
t = turtle.Turtle()
t.left(90)
t.penup()
t.goto(0, -200)
t.color("brown")
t.width(10)
t.shape("arrow")

screen.setup(width=800, height=600, startx=0, starty= 0)
screen.bgcolor("lightblue")

def draw_tree(level: int, branch_length: float):
    """Draw a tree recursively at a given level
    level - the levels of branches
    branch_length - length of branch in pixels
    """

    # If the level is greater than Zero
    # def draw_tree(level: int, branch_length: float):
    """Draw a tree recursively at a given level
        level - the levels of branches
        branch_length - length of branch in pixels
        """
    t.pendown()

        # If the level is greater than zero
    if level > 0:
            # 1. Move forward branch_length
            t.forward(branch_length)
            # 2. Turn left and draw a "smaller tree"
            t.left(47)
            draw_tree(level - 1, branch_length * 0.8)
            # 3. Turn right and draw a "smaller tree"
            t.right(94)
            draw_tree(level - 1, branch_length * 0.8)
            # 4. Return to the beginning
            t.left(47)
            t.backward(branch_length)
    else:
            # create a leaf
            t.color("green")
            t.stamp()
            t.color("brown")

draw_tree(4, 150)

screen.exitonclick()
