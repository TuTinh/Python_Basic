import turtle
def draw(t, h):
    t.begin_fill()
    t.left(90)
    t.write(h)
    t.forward(h)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(h)
    t.left(90)
    t.end_fill()

def drawSquare(t, size):
    for i in range(4):
        t.forward(size)
        t.left(90)


if __name__ == '__main__':

    t0 = turtle.Screen()
    t0.bgcolor("lightgreen")

    t = turtle.Turtle()
    t.color("hotpink")
    for i in range(5):
        drawSquare(t,30)
        t.penup()
        t.forward(60)
        t.pendown()



    t0.exitonclick()