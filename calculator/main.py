import turtle;
calculator = turtle.Turtle()
screen = turtle.Screen()
turtle.tracer(0, 0)
turtle.penup()

buttons = [1, 2, 3, 4, 5, 6, 7, 8, 9, '%', 0, '.']
def test(x, y):
    print(x, y)
style = ('Arial', 30, 'normal')
while True:
    screen.onclick(test)
    turtle.write(1, font=style)
    turtle.goto(50, 0)
    turtle.write(2, font=style)

    turtle.update()
