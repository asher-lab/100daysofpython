from turtle import Turtle, Screen
import random










screen = Screen()

screen.listen()



is_race_on = False
screen.setup(500,400, 0,0)
user_bet = screen.textinput(title="Who will win the race?", prompt="Enter the color: ")
print(user_bet)

colors = ["red", "orange", "yellow", "green", "blue", "violet"]

x = -220
y = -100

turtles = []
for i in range(0,6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x, y)
    y = y+30
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"{user_bet} - colored Turtle Won. Congratulations!")
                is_race_on = False
            else:
                print(f"You lose. {turtle.pencolor()} won the race.")
                is_race_on = False

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()
