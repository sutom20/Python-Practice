# import turtle
# from turtle import Screen
#
# timmy = turtle.Turtle()
#
# print(timmy)
#
# my_screen = Screen()
# print(my_screen.canvheight)
#
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
player_names = ['Sachin', 'Virat', 'Rohit']
centuries_scored = [100, 75, 55]

table.add_column('Player_Name', player_names)
table.add_column("100's Scored", centuries_scored)
table.align = 'r'

print(table)
