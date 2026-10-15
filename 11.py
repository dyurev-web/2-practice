from turtle import *
screensize(1000, 1000)
tracer(0)
hideturtle()

xc = int(input("xс = "))
yc = int(input("yс = "))
r = int(input("r = "))
x = int(input("x = "))
y = int(input("y = "))

up()
goto(xc, yc - r)
down()
circle(r)

up()
goto(x, y)
down()
dot(8, 'red')

update()

dist = ((x - xc) ** 2 + (y - yc) ** 2)
r2 = r ** 2

if dist < r2:
    res = "Точка находится внутри окружности"
elif dist == r2:
    res = "Точка лежит на окружности"
else:
    res = "Точка находится за пределами окружности"

up()
goto(0, yc+90)
color('red')
write(res, align='center', font=('Arial', 13, 'bold'))

update()
exitonclick()
