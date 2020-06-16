import turtle
import random

# inisialisasi
x_max = 400
x_min = 0
y_max = 400
y_min = 0
x_ran = x_max - x_min
y_ran = y_max - y_min

window = turtle.Screen()
myPen = turtle.Turtle()
window.setworldcoordinates(-20,-20,500,420)
myPen.shape("arrow")
window.title("Simulasi Random Walk 2D")

myPen.speed(0)
for line in range(4):
    myPen.forward(400)
    myPen.left(90)

# warna walk (banyaknya partikel = 10)
colors = ["LimeGreen", "Sienna", "DarkKhaki", "MediumOrchid", 
          "DimGray", "orange", "darkgreen", "cyan", "HotPink", "CornflowerBlue"]

# Simulasi berulang sebanyak partikel
for i in colors:
    myPen.color(i)
    myPen.penup()
    myPen.showturtle()
    myPen.pensize(5)
    myPen.speed(3)
    x = random.randrange(x_min, x_max, 20)
    y = random.randrange(y_min, y_max, 20)
    myPen.goto(x, y)
    
    # dengan 100 iterasi per partikel
    for j in range(100):
        direction = random.random()
        if direction <= 0.25:
            x = x + 20
        elif direction <= 0.5:
            y = y - 20
        elif direction <= 0.75:
            x = x - 20
        else:
            y = y + 20

        # cek jika walk mentok pada x_min/x_max/y_min/y_max
        if x > x_max:
            myPen.hideturtle()
            myPen.penup()
            myPen.goto(x_min,y)
            myPen.showturtle()
            myPen.pendown()
            x = x - x_ran
        elif x < x_min:
            myPen.hideturtle()
            myPen.penup()
            myPen.goto(x_max, y)
            myPen.showturtle()
            myPen.pendown()
            x = x + x_ran
        elif y > y_max:
            myPen.hideturtle()
            myPen.penup()
            myPen.goto(x, y_min)
            myPen.showturtle()
            myPen.pendown()
            y = y - y_ran
        elif y < y_min:
            myPen.hideturtle()
            myPen.penup()
            myPen.goto(x, y_max)
            myPen.showturtle()
            myPen.pendown()
            y = y + y_ran

        myPen.pendown()
        myPen.goto(x,y)


window.exitonclick()