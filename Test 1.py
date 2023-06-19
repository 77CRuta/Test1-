import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen(). bgcolor('black')
t.speed(1)
n = 40
h = 20
for i in range (180):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h+= 1/n
    t.color(c)
    t.left(1)
    t.fd(1)
    for j in range (2) : 
        t. left (2)
        t. circle (100)
