import turtle
from math import *

print('Enter the function:')
print('e.g. y = 4*x^2')
print('       = sin(pi*x)+5')
print('(python math library allowed)')
print('(vertical asymptotes will not graph properly)')
equationStr = str(input("y = "))

equationStr = equationStr.replace('^', '**')

graph = turtle.Turtle()
screen = turtle.Screen()
graph.hideturtle()
turtle.tracer(0, 0)

SIZE = 450
SCALE = 50
FONTSIZE = 10
SAMPLE_INTERVAL = 0.1

def drawLine(x, y, x2, y2, weight=1, colour='black'):
  graph.pen(pencolor=colour)
  graph.pensize(weight)
  graph.penup()
  graph.goto(x, y)
  graph.pendown()
  graph.goto(x2, y2)

def text(text, x, y, alignment='center', fontSize=FONTSIZE):
  graph.penup()
  graph.goto(x, y)
  graph.write(text, align=alignment, font=('Arial', fontSize, 'normal'))

def drawBackground():
  for i in range(-SIZE, SIZE+1, SCALE):
    drawLine(i, -SIZE, i, SIZE, colour='gray')
    drawLine(-SIZE, i, SIZE, i, colour='gray')
  
  drawLine(0, -SIZE, 0, SIZE, 2)
  drawLine(-SIZE, 0, SIZE, 0, 2)
  for i in range(0, SIZE, SCALE):
    text(i//SCALE, i, -FONTSIZE*2)
    text(-i//SCALE, -i, -FONTSIZE*2)
    text(i//SCALE, -FONTSIZE, i-FONTSIZE)
    text(-i//SCALE, -FONTSIZE, -i-FONTSIZE)

def drawGraph(weight=5, colour='green'):
  graph.pen(pencolor=colour)
  graph.pensize(weight)
  
  x = -SIZE/SCALE
  y = eval(equationStr.replace('x', '('+str(x)+')'))
  graph.goto(x*SCALE, y*SCALE)

  graph.pendown()
  while x < SIZE/SCALE:
    y = eval(equationStr.replace('x', '('+str(x)+')'))
    graph.goto(x*SCALE, y*SCALE)
    x += SAMPLE_INTERVAL
  graph.penup()


while True:
  drawBackground()
  drawGraph()
  turtle.update()