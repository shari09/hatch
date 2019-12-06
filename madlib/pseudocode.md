### Import	
	import random

### Initializing needed variables
Create a list of 22 empty strings named userInput

	userInput = ['']*22

Create a list named requirements {
	stores tuples of type needed (ex. adjective) and number (ex. the first box) in the madlib passage
}

	requirements = [
		('adjective', 1),
		#other tuples...
	]


Use the shuffle method from random to shuffle the requirements

	random.shuffle(requirements)

### Getting user input

for i in range(the number of boxes that needs to be filled):
	Set the variable *nextInput equal to requirements with the index of i
	Set userInput with the index of the corresponding box number to the user input of 'Enter a(n) (first item of nextInput): '


	for i in range(21):
		nextInput = requirements[i]
		userInput[nextInput[1]] = input('Enter a(n) ' + nextInput[0] + ': ')

### Output
print the madlib passage, writing {} for the blanks and call the format method with every element in userInput

	print().format()