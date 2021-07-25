from turtle import Turtle, Screen
import random


tim = Turtle(shape="turtle")







screen = Screen()

screen.listen()

def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def rotate_cc():
    tim.left(10)
def rotate_c():
    tim.right(10)
def reset():
    tim.reset()
screen.onkey(key = "w", fun=move_forward)
screen.onkey(key = "s", fun=move_backward)
screen.onkey(key="a", fun= rotate_cc)
screen.onkey(key="d", fun = rotate_c)
screen.onkey(key="c", fun = reset)




screen.exitonclick()
