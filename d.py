import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)
colors = ["red", "purple", "blue", "green", "orange", "yellow"]
for i in range(200):
    t.pencolor(colors[i % 6])
    t.forward(i * 2)
    t.left(59)
turtle.done()

