import turtle

ts = turtle.Screen()
ts.bgcolor("black")

tp = turtle.Turtle()
tp.pensize(2)
tp.color("white")
tp.speed(7)


def tier(c, x, y):
    tp.penup()
    tp.goto(x=x, y=y)
    tp.pendown()
    tp.circle(c)


def tl(t, x, y, f):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.left(30)
    t.forward(f)


def tle(t, l, f):
    t.left(l)
    t.forward(f)


def tr(t, r, f):
    t.right(r)
    t.forward(f)


def cur(t, rng, r, f):
    for i in range(rng):
        tr(t, r, f)


tp.goto(-300, 0)
tr(tp, 90, 15)

for x in [600, 15, 300]:
    tle(tp, 90, x)

tp.penup()
tp.forward(150)
tp.pendown()
tp.right(180)


tier(60, -150, 0)
tier(45, -150, 15)
tier(20, -150, 40)

tp2 = turtle.Turtle()
tp2.pensize(2)
tp2.color("white")
tp2.speed(7)

tl(tp, -150, 55, 90)
tl(tp2, -160, 60, 87)

tle(tp, 50, 25)
tle(tp2, 50, 35)

tr(tp, 130, 25)

tle(tp, 50, 30)
cur(tp, 9, -20, 2)
tp.forward(10)
tr(tp, 60, 60)
tr(tp, 70, 130)
tr(tp, 90, 100)
tier(20, 85, 195)
tier(45, 70, 175)
tier(60, 60, 165)

tle(tp2, 155, 50)
tle(tp2, 90, 10)

tp2.penup()
tp2.goto(-90, 160)
tp2.pendown()

tr(tp2, 90, 60)

tp2.penup()
tp2.back(60)
tp2.pendown()

tr(tp2, 50, 30)
tr(tp2, 80, 20)
tle(tp2, 75, 40)

cur(tp2, 25, 4, 2)

tp2.forward(170)
cur(tp2, 15, 4, 1)

tp2.left(60)

tp2.forward(30)
tp2.left(30)
tp2.circle(-35, 180)
tle(tp2, 80, 40)
cur(tp2, 9, 20, 2)
tp2.forward(40)

tp2.left(90)
tp2.circle(-35, 100)
tle(tp2, 80, 15)
tle(tp2, 60, 80)
tle(tp2, 50, 45)
cur(tp2, 9, 15, 2)
tle(tp2, 40, 10)
tp2.penup()
tp2.back(5)
tr(tp2, 85, 15)
tp2.pendown()
tp2.forward(45)
cur(tp2, 10, 5, 1)
tp2.forward(50)
tle(tp2, 120, 110)
cur(tp2, 9, -10, 1)
tp2.forward(60)
cur(tp2, 9, 10, 1)
tle(tp2, 165, 100)
tle(tp2, 50, 10)
tr(tp2, 50, 5)
tp2.penup()
tr(tp2, 70, 15)
tp2.pendown()
tr(tp2, 35, 150)


for i in range(200):
    tp.circle(1)
