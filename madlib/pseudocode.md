import random

Create a list of 22 empty strings named userInput
Create a list named requirements {
  stores tuples of type needed (ex. adjective) and number (ex. the first box) in the madlib passage
}

Use the shuffle method from random to shuffle the requirements

for i in range(21): (the number of boxes that needs to be filled)
  Set the variable nextInput equal to requirements with the index of i
  Set userInput with the index of the corresponding box number to the user input of 'Enter a(n) (first item of nextInput): '

print the madlib passage, writing {} for the blanks and call the format method with every element in userInput