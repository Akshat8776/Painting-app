pfrom telnetlib import TN3270E
import turtle
import random
import os
def clear():
    os.system('cls')

clear()
print("Please use smallcase letters\nInstructions\nw : forward move\ns : backward move\nd : right move a : left move\nc : clear draw\ne : exit")
print("p : penup\nO : pendown\nr : rub to white\nh : 45degree\nb : background colour\nn : input specific color")
print("1 : pensize\n2 : square\n3 : circle")
t=turtle.Turtle()
screen=turtle.Screen()
screen.title("Akshat's painting app")
t.inpcol=""
t.shape("turtle")
colours = ["Red","Yellow","Orange","brown","CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
t.c = 0
screen.bgcolor("blue")
a=screen.numinput(title="Pensize",prompt="Please enter the pensize : ")
t.pensize(a)
def col():
    if t.c==1:
        t.color("White")
    elif t.inpcol:
        t.color(t.inpcol)
    elif t.c==0:
        t.color(random.choice(colours))
    
def rubber():
    if t.c==0:
        t.c=1
    else:
        t.c=0
def half():
    t.setheading(t.heading()+45)
def move_for():
    col()
    t.forward(20)
def move_back():
    col()
    t.setheading(t.heading()+180)
    t.forward(20)
def move_right():
    t.setheading(t.heading()+270)
    t.forward(20)
def move_left():
    t.setheading(t.heading()+90)
    t.forward(20)
def clear_draw():
    t.clear()
def pen_up():
    t.penup()
def pen_down():
    t.pendown()
def owncolor():
    t.inpcol=str(screen.textinput(title="Specific colour",prompt="Please enter the colour : "))
    screen.listen()
def background():
    screen.bgcolor(str(screen.textinput(title="Specific colour",prompt="Please enter the colour : ")))
    screen.listen()
def pensize():
    a=screen.numinput(title="Pensize",prompt="Please enter the pensize : ")
    t.pensize(a)
    screen.listen()
def drawsquare():
    b=screen.numinput(title="square length",prompt="Please enter the length of side : ")
    screen.listen()
    for i in range(0,4):
        t.forward(b)
        t.left(90)
        
def drawcircle():
    b=screen.numinput(title="Circle",prompt="Please enter the radius : ")
    screen.listen()
    t.circle(b)
def drawtriangle():
    b=screen.numinput(title="Triangle",prompt="Please enter the length : ")
    screen.listen()
    for i in range(0,3):
        t.forward(b)
        t.left(120)
def drawoval():
    rad=screen.numinput(title="oval",prompt="Please enter the radius of arc : ")
    screen.listen()
    t.left(315)
    for i in range(2):
        t.circle(rad,90)
        t.circle(rad//2,90)
screen.listen()
screen.onkeypress(key="w",fun=move_for)
screen.onkeypress(key="s",fun=move_back)
screen.onkeypress(key="d",fun=move_right)
screen.onkeypress(key="a",fun=move_left)
screen.onkeypress(key="h",fun=half)
screen.onkey(key="c",fun=clear_draw)
screen.onkey(key="p",fun=pen_up)
screen.onkey(key="o",fun=pen_down)
screen.onkey(key="r",fun=rubber)
screen.onkey(key="e",fun=exit)
screen.onkey(key="n",fun=owncolor)
screen.onkey(key="b",fun=background)
screen.onkey(key="1",fun=pensize)
screen.onkey(key="2",fun=drawsquare)
screen.onkey(key="3",fun=drawcircle)
screen.onkey(key="4",fun=drawtriangle)
screen.onkey(key="5",fun=drawoval)
screen.exitonclick()