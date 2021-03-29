import turtle
import time


def setting():
    """设置参数"""
    pensize(4)
    # 隐藏海龟
    hideturtle()
    colormode(255)
    color((255, 155, 192), "pink")
    setup(840, 500)
    speed(10)

turtle.setup(840*2,500*2)    
turtle.hideturtle()
turtle.speed(10)
turtle.pensize(2)
turtle.bgcolor("black")
colors = ["red","yellow",'purple','blue']
turtle.tracer(False)

for x in range (400):
    turtle.forward(2*x)
    turtle.color(colors[x % 4])
    turtle.left(91)

turtle.tracer(True)
turtle.done()
