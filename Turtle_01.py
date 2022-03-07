# from turtle import Turtle, Screen
#
# timmy = Turtle()
# screen = Screen()
# screen.screensize(2000, 1500)
# timmy.shape("turtle")
# timmy.speed(1)
# timmy.color("green")
# for x in range(1, 5):
#     timmy.forward(200)
#     timmy.left(90)
# print(timmy)
#
# sh = Screen()
# print(sh.canvheight)
# print(sh.canvwidth)
# sh.exitonclick()
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name",[ "Pikachu", "Pigi", "Eeve"])
table.add_column("Type", ["Electric", "Flying", "Normal"])
print(table.align)
table.align = "l"
print(table.align)
#table.align["Pokemon Name"] = "r"
print(table)
