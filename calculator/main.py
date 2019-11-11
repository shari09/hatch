#the most basic calculator made with Turtles
#lots of functions can be added
import turtle

calculator = turtle.Turtle()
screen = turtle.Screen()
turtle.tracer(0, 0)

turtle.hideturtle()
calculator.hideturtle()

calculator.penup()
SIZE = 50

class Screen:
  def __init__(self, x, y, width, height, numLines):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.fontSize = 10
    self.numLines = numLines
    self.lineHeight = self.height//self.numLines
    self.height = self.lineHeight*self.numLines
    self.lines = ['']*self.numLines

  def reset(self):
    self.fontSize = 10
    self.lines = ['']*self.numLines

  def add(self, value):

    if len(self.lines[0]) * self.fontSize >= self.width-self.fontSize \
       or len(self.lines[1]) * self.fontSize >= self.width-self.fontSize:
      if (self.fontSize > 5):
        self.fontSize -= 1
      else:
        return

    #reset the screen if you typed a new digit
    if len(self.lines[1]) == 0 and value.isdigit():
      self.lines[0] = ''
    elif len(self.lines[1]) == 0 and not value.isdigit():
      self.lines[1] = self.lines[0]

    self.lines[0] += value
    self.lines[1] = evaluate(self.lines[0])

  def evaluate(self):
    self.lines[0] = self.lines[1]
    self.lines[1] = ''


  def display(self):
    calculator.goto(self.x, self.y)
    calculator.pendown()
    for i in range(2):
      calculator.forward(self.width)
      calculator.left(90)
      calculator.forward(self.height)
      calculator.left(90)
    calculator.penup()
    for lineIdx in range(len(self.lines)):
      lineLen = len(self.lines[lineIdx])
      for charIdx in range(lineLen):
        calculator.goto(self.x+self.width - self.fontSize - self.fontSize*(lineLen-charIdx), self.y + self.numLines*self.lineHeight-(lineIdx+1)*self.lineHeight)
        calculator.write(self.lines[lineIdx][charIdx], font=('Arial', self.fontSize, 'normal'))

class Button:
  def __init__(self, x, y, value):
    self.x = x
    self.y = y
    self.value = str(value)
    self.size = SIZE

  def clicked(self, xPos, yPos):
    if self.x < xPos < self.x + self.size \
        and self.y < yPos < self. y + self.size:
      return True

  def display(self):
    calculator.goto(self.x, self.y)
    calculator.pendown()
    for i in range(4):
      calculator.forward(self.size)
      calculator.left(90)
    calculator.penup()
    calculator.goto(self.x+self.size/2, self.y)
    calculator.write(self.value, align='center', font=('Arial', 30, 'normal'))

def addToScreen(value, screen):
  if value == '=':
    screen.evaluate()
  else:
    screen.add(value)


def evaluate(line):
  closedBracket = True
  for i in range(len(line)):
    if (line[i] == '('):
      closedBracket = False
    elif (line[i] == ')'):
      closedBracket = True
  if (closedBracket 
      and line[-1] != '+' 
      and line[-1] != '-'
      and line[-1] != '/'
      and line[-1] != '*'):
    return str(eval(line))
  return 'Error'

def check(x, y):
  calculator.clear()
  for button in buttons:
    if button.clicked(x, y):
      if button.value == 'C':
        calcScreen.reset()
      else:
        addToScreen(button.value, calcScreen)
  displayAll()

def displayAll():
  for button in buttons:
    button.display()
  calcScreen.display()


#creating the buttons/screen
buttons = []
for i in range(3):
  for j in range(1, 4):
    buttons.append(Button(i*SIZE, j*SIZE, i+(j-1)*3+1))
buttons.append(Button(0, 0, 0))
buttons.append(Button(SIZE, 0, '.'))
buttons.append(Button(2*SIZE, 0, '='))
buttons.append(Button(3*SIZE, 0, '/'))
buttons.append(Button(3*SIZE, SIZE, '*'))
buttons.append(Button(3*SIZE, 2*SIZE, '-'))
buttons.append(Button(3*SIZE, 3*SIZE, '+'))
buttons.append(Button(-SIZE, 3*SIZE, 'C'))
buttons.append(Button(-SIZE, 2*SIZE, '('))
buttons.append(Button(-SIZE, SIZE, ')'))
calcScreen = Screen(0, 4*SIZE, 4*SIZE, SIZE, 2)


#main driving code
displayAll()
while True:
  screen.onclick(check)
  turtle.update()
