from turtle import Screen, Turtle
from random import randint

def race_start():
    End_race = False
    while not End_race:
        for i in turtle_objects:
            i.penup()
            i.forward(randint(1,5))
            (x,y) = i.pos()
            if x >= 315:
                return i
                End_race = True
                break

def draw_line():
    tom = Turtle(shape="classic")
    tom.penup()
    tom.goto(x=-340, y=-160)
    tom.pendown()
    tom.goto(x=-340, y=160)
    tom.penup()
    tom.goto(x=330, y=-160)
    tom.pendown()
    tom.goto(x=330, y=160)
    tom.right(90)

screen = Screen()
screen.setup(width=700, height=400)
user_choice = screen.textinput("Turtle Bet", "Which color will win? ")


color = ["green", "blue", "orange", "black", "red", "pink"]
y_coordinat = [-150, -100, -50, 0, 50, 100]
turtle_objects = []
draw_line()
for i in range(0,6):
    turt = Turtle(shape="turtle")
    turt.color(color[i])
    turt.penup()
    turt.goto(x=-330, y=y_coordinat[i])
    turtle_objects.append(turt)

winning_turtle = race_start()
winnig_color = winning_turtle.color()[0]
if user_choice == winnig_color:
    print("You won the bet")
else:
    print(f"You lose! The {winnig_color} turtle won the race")

screen.exitonclick()