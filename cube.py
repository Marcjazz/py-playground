import turtle as t
import colorsys as co
import random as r

t.speed(10)
t.setup(500, 500)
t.bgcolor("black")
t.width(0.5)
t.forward(125)


def draw_c(x):
    t.color(co.hsv_to_rgb(15/r.randint(20, 50), 15 /
            r.randint(20, 50), 15/r.randint(20, 50)))
    t.left(x)
    t.forward(190)
    t.left(90)
    t.forward(190)
    t.left(90)
    t.forward(190)
    if x > 0:
        draw_c(x-1)

draw_c(90)
t.done()