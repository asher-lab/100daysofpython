import turtle
from turtle import Turtle, Screen
import turtle as t
import random

timmy = Turtle()
timmy.shape("circle")
timmy.color("green")


angle = 360
sides = 3
length = 100
i = 1

for _ in range(10):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

timmy.reset()

def pick_color():
    colors = ["blue","black","brown","red","deep pink","green","orange","cyan","turquoise","pink", "green yellow"]
    random.shuffle(colors)
    return colors[0]


def draw_timmy(size):
    for _ in range(size):
        timmy.forward(length)
        timmy.right(angle / sides)

for sides in range(3, 11):
    draw_timmy(sides)
    timmy.pencolor(pick_color())

timmy.reset()


timmy.speed(10)
timmy.pensize(10)
for i in range(100):
    timmy.forward(20)
    timmy.pencolor(pick_color())
    timmy.right(random.randrange(0, 360, 90))

timmy.reset()



t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

for i in range(100):
    timmy.forward(20)
    timmy.pencolor(random_color())
    timmy.right(random.randrange(0, 360, 90))

timmy.reset()


timmy.speed(0)
timmy.pensize(1)
start_tim = timmy.heading()

def draw_spiral(size_of_gap):
    while True:
        timmy.circle(100)
        timmy.pencolor(random_color())
        timmy.right(size_of_gap)
        if start_tim == timmy.heading():
            break



draw_spiral(10)

timmy.reset()


import colorgram
color_pack = []
colors = colorgram.extract('image.jpg', 20)

for _ in range (0, 5):
    current_color = colors[_]
    rgb = current_color.rgb
    r = rgb.r
    g = rgb.g
    b = rgb.b
    color_pack.append((r,g,b))

def rand_color():
    return color_pack[random.randint(0,4)]


#Final Project in Hirst Painting
timmy.speed(0)
timmy.pensize(5)

xy = 0
state_end = 9
state_n = 30.00

for i in range(99):
    timmy.dot(20)
    timmy.penup()
    timmy.forward(30)
    timmy.pendown()
    timmy.pencolor(rand_color())
    if i == state_end:
        timmy.penup()
        xy = timmy.pos()
        timmy.setpos(0, state_n)
        state_end = state_end + 10
        state_n = state_n + 30


screen = Screen()
screen.exitonclick()
