from turtle import *


left(90)
screensize(2000, 2000)
pendown()
tracer(0)
k = 10
for i in range(2):
    forward(14*k)
    left(270)
    back(12*k)
    right(90)
penup()
forward(9*k)
right(90)
back(7 * k)
left(90)
pendown()
for i in range(2):
    forward(13*k)
    right(90)
    forward(6 * k)
    right(90)
penup()
l = 0
for x in range(-12, 1):
    for y in range(0, 15):
        goto(x * k, y * k)
        dot(3, 'red')
        l += 1
for x in range(-7, 0):
    for y in range(15, 23):
        goto(x * k, y * k)
        dot(3, 'red')
        l += 1
print(l)
update()
done()