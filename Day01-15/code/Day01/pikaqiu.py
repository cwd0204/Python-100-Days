from turtle import *

screensize(800, 600, "#fed926")
setup(width=1000, height=1000, startx=50, starty=50)
pensize(5)
pencolor("black")
speed(5)


def leftEar():
    # 海龟方向
    setheading(30)
    penup()
    fillcolor("#1f1515")
    goto(110, 150)
    # 左耳左
    pendown()
    setheading(30)
    left(5)
    circle(-410, 55)
    penup()
    # 左儿右
    goto(170, 100)
    setheading(0)
    pendown()
    right(2)
    circle(500, 39)
    # 左耳颜色
    begin_fill()
    left(124)
    circle(400, 15)
    left(-90)
    circle(200, -27)
    right(42)
    circle(400, 20)
    end_fill()
    penup()


def rightEar():
    # 右耳右
    goto(-120, 180)
    left(10)
    pendown()
    circle(400, 50)
    # 右耳左
    left(118)
    circle(400, 60)
    penup()
    # 右耳颜色
    goto(-75, 450)
    left(-140)
    pendown()
    begin_fill()
    circle(400, -13)
    right(41)
    circle(405, 17)
    left(120)
    circle(400, 10)
    end_fill()
    penup()


def head():
    # 轮廓,上
    goto(-130, 175)
    right(32)
    pendown()
    circle(400, -37)
    # 轮廓，左
    penup()
    goto(181, 99)
    left(125)
    pendown()
    right(180)
    circle(400, -20)
    left(165)
    circle(200, 40)
    left(190)
    circle(400, -40)
    circle(200, -40)
    # 轮廓，右
    penup()
    goto(-170, 160)
    left(190)
    pendown()
    circle(150, 40)
    right(180)
    circle(180, -30)
    left(170)
    circle(50, 80)
    circle(400, 20)
    penup()


# 右手
def rightHand():
    goto(-200, -130)
    right(120)
    pendown()
    circle(200, 20)
    circle(60, 120)
    circle(400, 14)
    penup()
    goto(-170, -190)
    pendown()
    left(175)
    circle(200, -30)
    penup()


# 左手
def leftHand():
    goto(130, -175)
    pendown()
    left(20)
    circle(250, 64)
    circle(10, 110)
    circle(300, 40)
    penup()


# 肚子
def tummy():
    goto(-210, -278)
    left(80)
    pendown()
    circle(50, -10)
    right(210)
    circle(400, 20)
    circle(50, 50)
    circle(400, 5)
    penup()
    # 斑点一
    fillcolor("#ce7f38")
    goto(206, -220)
    right(120)
    begin_fill()
    circle(40, 40)
    circle(5, 120)
    right(20)
    circle(40, 41)
    end_fill()
    # 斑点二
    goto(235, -350)
    left(160)
    begin_fill()
    circle(50, 50)
    circle(5, 120)
    right(15)
    circle(50, 45)
    end_fill()


def leftEye():
    penup()
    goto(80, 90)
    left(180)
    pendown()
    goto(30, 60)
    penup()
    left(45)
    # 黑眼
    fillcolor("#1c1c1b")
    begin_fill()
    circle(44, 295)
    end_fill()
    # 白眼
    fillcolor("#f7ebfc")
    goto(60, 65)
    begin_fill()
    circle(12, 360)
    end_fill()


def rightEye():
    goto(-160, 100)
    pendown()
    goto(-105, 70)
    penup()
    goto(-107, 72)
    # 黑眼
    fillcolor("#1c1c1b")
    begin_fill()
    right(110)
    circle(100, -45)
    circle(20, -95)
    right(25)
    circle(100, -43)
    end_fill()
    # 白眼
    fillcolor("#f7ebfc")
    goto(-150, 75)
    begin_fill()
    circle(12, 360)
    end_fill()


# 红脸 左
def leftBlush():
    goto(75, -5)
    pendown()
    fillcolor("#f24a23")
    begin_fill()
    right(40)
    circle(50, 360)
    end_fill()
    penup()


# 红脸右
def rightBlush():
    goto(-215, 10)
    right(35)
    pendown()
    begin_fill()
    circle(50, -135)
    right(62)
    circle(50, -75)
    goto(-217, 10)
    end_fill()
    penup()


# 鼻子
def nose():
    goto(-90, 20)
    pendown()
    fillcolor("#2a0f00")
    begin_fill()
    right(48)
    circle(30, -30)
    right(90)
    circle(30, -30)
    right(80)
    circle(30, -30)
    end_fill()
    penup()


# 嘴巴
def mouth():
    goto(-90, -30)
    left(150)
    pendown()
    circle(30, -130)
    penup()
    goto(-90, -30)
    pendown()
    circle(100, 40)
    circle(30, 110)


if __name__ == '__main__':
    leftEar()
    rightEar()
    head()
    rightHand()
    leftHand()
    tummy()
    leftEye()
    rightEye()
    leftBlush()
    rightBlush()
    nose()
    mouth()
    done()

