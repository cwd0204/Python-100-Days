from turtle import *
from random import *
from math import *


def tree(n,l):
    pendown()
    t = cos(radians(heading() + 45))/8 + 0.25
    pencolor(t,t,t)
    pensize(n/4)
    forward(l)

    if n > 0:
        b = random() * 15 + 10
        c = random() * 15 + 10
        d = l * (random() * 0.35 + 0.6)
        right(b)
        tree(n -1, d)
        left(b + c)
        tree(n -1, d)
        right(c)
    else:
        right(90)
        n = cos(radians(heading() -45)) /4 + 0.5
        pencolor(n,n,n)
        circle(2)
        left(90)
    penup()
    backward(l)

def setting():
    """设置参数"""
    # pensize(4)
    # 隐藏海龟
    hideturtle()
    colormode(255)
    color((255, 155, 192), "pink")
    setup(840, 500)
    speed(10)


# setting()
bgcolor(0.5,0.5,0.5)
hideturtle()
speed(0)
tracer(0,0)
left(90)
penup()
backward(300)
tree(13,100)
done()