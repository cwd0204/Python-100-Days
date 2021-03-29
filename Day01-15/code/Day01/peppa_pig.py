"""
绘制小猪佩奇
"""
from turtle import *

def setting():
    """设置参数"""
    pensize(4)
    # 隐藏海龟
    hideturtle()
    colormode(255)
    color((255, 155, 192), "pink")
    setup(840, 500)
    speed(10)

def nose(x,y):
    """画鼻子"""
    penup()
    # 将海龟移动到指定的坐标
    goto(x,y)
    pendown()
    # 设置海龟的方向（0-东、90-北、180-西、270-南）
    setheading(-30)
    begin_fill()
    a = 0.4
    for i in range(120):
        if 0 <= i < 30 or 60 <= i <90:
            a = a + 0.08
            # 向左转3度
            left(3)
            # 向前走
            forward(a)
        else:
            a = a - 0.08
            left(3)
            forward(a)
    end_fill()
    penup()
    setheading(90)
    forward(25)
    setheading(0)
    forward(10)
    pendown()
    # 设置画笔的颜色(红, 绿, 蓝)
    pencolor(255, 155, 192)
    setheading(10)
    begin_fill()
    circle(5)
    color(160, 82, 45)
    end_fill()
    penup()
    setheading(0)
    forward(20)
    pendown()
    pencolor(255, 155, 192)
    setheading(10)
    begin_fill()
    circle(5)
    color(160, 82, 45)
    end_fill()


def head(x, y):
    """画头"""
    color((255, 155, 192), "pink")
    penup()
    goto(x,y)
    setheading(0)
    pendown()
    begin_fill()
    setheading(180)
    circle(300, -30)
    circle(100, -60)
    circle(80, -100)
    circle(150, -20)
    circle(60, -95)
    setheading(161)
    circle(-300, 15)
    penup()
    goto(-100, 100)
    pendown()
    setheading(-30)
    a = 0.4
    for i in range(60):
        if 0<= i < 30 or 60 <= i < 90:
            a = a + 0.08
            lt(3) #向左转3度
            forward(a) #向前走a的步长
        else:
            a = a - 0.08
            lt(3)
            forward(a)
    end_fill()


def ears(x,y):
    """画耳朵"""
    color((255, 155, 192), "pink")
    penup()
    goto(x, y)
    pendown()
    begin_fill()
    setheading(100)
    circle(-50, 50)
    circle(-10, 120)
    circle(-50, 54)
    end_fill()
    penup()
    setheading(90)
    forward(-12)
    setheading(0)
    forward(30)
    pendown()
    begin_fill()
    setheading(100)
    circle(-50, 50)
    circle(-10, 120)
    circle(-50, 56)
    end_fill()


def eyes(x,y):
    """画眼睛"""
    color((255, 155, 192), "white")
    penup()
    setheading(90)
    forward(-20)
    setheading(0)
    forward(-95)
    pendown()
    begin_fill()
    circle(15)
    end_fill()
    color("black")
    penup()
    setheading(90)
    forward(12)
    setheading(0)
    forward(-3)
    pendown()
    begin_fill()
    circle(3)
    end_fill()
    color((255, 155, 192), "white")
    penup()
    seth(90)
    forward(-25)
    seth(0)
    forward(40)
    pendown()
    begin_fill()
    circle(15)
    end_fill()
    color("black")
    penup()
    setheading(90)
    forward(12)
    setheading(0)
    forward(-3)
    pendown()
    begin_fill()
    circle(3)
    end_fill()


def cheek(x,y):
    """画脸颊"""
    color((255, 155, 192))
    penup()
    goto(x,y)
    pendown()
    setheading(0)
    begin_fill()
    circle(30)
    end_fill()


def mouth(x,y):
    """画嘴巴"""
    color(239, 69, 19)
    penup()
    goto(x, y)
    pendown()
    setheading(-80)
    circle(30, 40)
    circle(40, 80)


def body():
    '''画身体'''
    color("red",(255,99,71))
    penup()
    seth(90)
    forward(-20)
    seth(0)
    forward(-78)
    pendown()
    begin_fill()
    seth(-130)
    circle(100,10)
    circle(300,30)
    seth(0)
    forward(230)
    seth(90)
    circle(300,30)
    circle(100,3)
    color((255,155,192),(255,100,100))
    seth(-135)
    circle(-80,63)
    circle(-150,24)
    end_fill()

def hand():
    '''画手'''
    color((255,155,192))
    penup()
    seth(90)
    forward(-40)
    seth(0)
    forward(-27)
    pendown()
    seth(-160)
    circle(300,15)
    penup()
    seth(90)
    forward(15)
    seth(0)
    forward(0)
    pendown()
    seth(-10)
    circle(-20,90)
    penup()
    seth(90)
    forward(30)
    seth(0)
    forward(237)
    pendown()
    seth(-20)
    circle(-300,15)
    penup()
    seth(90)
    forward(20)
    seth(0)
    forward(0)
    pendown()
    seth(-170)
    circle(20,90)

def foot():
    '''画脚'''

    pensize(10)
    color((240,128,128))
    penup()
    seth(90)
    forward(-75)
    seth(0)
    forward(-180)
    pendown()
    seth(-90)
    forward(40)
    seth(-180)
    color("black")
    pensize(15)
    forward(20)
    pensize(10)
    color((240,128,128))
    penup()
    seth(90)
    forward(40)
    seth(0)
    forward(90)
    pendown()
    seth(-90)
    forward(40)
    seth(-180)
    color("black")
    pensize(15)
    forward(20)

def tail():
    '''画尾巴'''
    pensize(4)
    color((255,155,192))
    penup()
    seth(90)
    forward(70)
    seth(0)
    forward(95)
    pendown()
    seth(0)
    circle(70,20)
    circle(10,330)
    circle(70,30)



def main():
    """主函数"""
    setting() 
    nose(-100, 100)
    head(-69, 167)
    ears(0, 160)
    eyes(0, 140)
    cheek(80, 10)
    mouth(-20, 30)
    body()
    hand()
    foot()
    tail()
    done()


if __name__ == '__main__':
    main()
