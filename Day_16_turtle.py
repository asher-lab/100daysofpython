#import another_module
#print(another_module.another_var)

#import turtle
#timmy = turtle.Turtle()

#from turtle import Turtle, Screen

#timmy = Turtle()
#print(timmy)
#timmy.shape("turtle")
#timmy.color("green")
#timmy.forward(100)


#my_screen = Screen()
#print(my_screen.canvheight)
#my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon", ["Pikachu", "Doraemon", "Dominum"])
table.add_column("Type", ["Electric", "Magic", "Deus"])
table.align = 'l'


print(table)
