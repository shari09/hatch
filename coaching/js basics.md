# JS basics

Contents  
- [Variables](#variables)
- [For Loops](#forLoops)
- [While loops](#whileLoops)
- [If...Else...Statements](#ifElse)
- [Functions](#functions)
- [Arrays](#arrays)
- [Object Literals](#objectLiterals)
- [Constructors](#constructors)



<div id='variables'/>

## Variables

```javascript
var variableName = value;

var size = 40;
```
> A name for the data that we store

**Notes**  
-- Ask if they know what *x* is in math

**Real life example:** *water bottle named Winnie* 
- Instead of saying "pass me that `clear water bottle`", we say "pass me `Winnie`" 
(`var Winnie = clear water bottle`) 
- the name is special
	- each name is unique, meaning that there can't be two of the same names in one program
	- you can change what you assign the name to. For example, I can make `Winnie` the name of my `pencil`, but then my `clear water bottle` is no longer named `Winnie`
		- if you named them both `Winnie`, when you ask someone to pass you `Winnie`, they won't know whether to pass the `pencil` or the `clear water bottle`

> Variables are convenient, a good example is if we have a certain `size` variable that we want to reuse but don't want to type in the number each time 


#### Exercise(s)
- Hold the ball (draw multiple circles at different places with the same size)



<div id='forLoops'/>

## For Loops

```javascript
for (initializer[starting point]; condition; statement2) {
  //the code here will execute as long
  //as the condition is met (for a certain amount of loops)
	
  //statement2 executes after all the
  //code here executes 
}


for (var numLaps = 0; numLaps < 10; numLaps++) {
  runAround(); //this function isn't defined yet but just pretend it exists :))
}
```
> Loops through a block of code a set number of times

**Notes**  
-- n/a

**Real life example:** *running around the school track field* 
- you are *looping* around the track field
- your coach wants you to run `10 laps`, and also wants you to high five him each time you run a lap.
	- you start at 0 laps, and run around the track
	- `for` each lap that you do, you `high five the coach`
	- every time you finish a lap, your total laps done increases by 1
	- finally, you stop when you reach 10 laps.

> If we want the code to do the same thing for a set amount of times, we can just put it inside a `for loop` rather than copying and pasting it that set amount of times

> Convenient once you start using arrays (you can use for loops to get every value in the array, etc.)

#### Exercise(s)
- Draw 10 dots across the screen, with each dot being 10 pixels apart



<div id='whileLoops'/>

## While Loops

```javascript
while (condition) {
  //code to execute
}
----------------------
while (sleeping) {
  hugYourPlush(); //pretend this function exists
}
```
> Keeps looping through a certain block of code an unknown number of times while the condition is true

**Notes**  
-- n/a

**Real life example:** 
- same as what the word `while` means in real life
- while `something is happening...`, you do `some certain action...`
- while you're sleeping, hug your plush

> `While loops` are useful if you are unsure of how many times a certain block of code will have to run. For example, if you writing a block of code that asks the user to input something and only stops when the user inputs the word `STOP`, you don't know how many times that block of code will run. However, you can simply do `while the input is not "STOP"...` and that code will run until the user inputs `STOP`!

TODO: add a picture of what I mean for stacking circles


#### Exercise(s)
- Stack circles (draw circles on top of each other) of random size until you reach 200 in height
- prompting `user for input`, `draws a circle` at a random location each time until the user inputs `STOP`





<div id='ifElse'/>

## If... Else.. Statements

```javascript
if (condition) {
  //code block
} else {
  //code block
}
--------------------
if (wearingRed) {
  doJumpingJack();
} else {
  doPushUp();
}
```
> Used to make decisions according to a condition

**Notes**  
-- n/a

**Real life example:** 
- It's what `if` and `else` means in plain English 
- `If` you are wearing a red shirt, do a jumping jack. Or `else`, do a push up.

> A lot of decisions in the code are made using if/else conditions (eg. if the mouse position is at the top of the screen, if a number is greater than another, etc.)


#### Exercise(s)
- Hold the ball - if your mouse is on the upper half of the screen, draw a rectangle. Otherwise, draw a circle.


<div id='functions'/>

## Functions

```javascript
var functionName = function(optionalParameters) {
  //do some cool stuff
  //can use the parameters/input passed to the function
  //optionally return a value (number, word, letter, etc) to whatever called this function
};
```
> A block of organized and reusable code that performs a task

**Notes**  
-- Does this look confusing? You feel like everything is everywhere and there's all the random vocabulary that makes no sense? Welp, don't worry, because ~~I honestly feel the same way~~

**Real life example:** *doing homework requires a lot of steps* 
- get pencil
- get eraser
- get handouts
- read questions
- think of answers
- write down the answers
```javascript
var doHomework = function() {
  getPencil();
  getEraser();
  getHandouts();
  readQuestions();
  thinkOfAnswers();
  writeDownAnswers();
};
```

**Real life example:** *you are a professional baker, and must `getCupcakes` depending on a specified `flavour`* 
- mix ingredients together to make batter
- put in oven
- bake for around 20min
- take it out of the oven
- put on `flavour` icing
- `return` (give) the cupcakes to the customer
```javascript
var getCupcakes = function(flavour) {
  makeBatter();
  putInOven();
  bake();
  takeItOut();

  //we can include an if/else conditional for checking what to do given a flavour
  if (flavour === 'vanilla') {
    putVanillaIcing();
  } else {
    putChocolateIcing();
  }
  
  return cupcakes; 
  //of course in actual coding, we have to 
  //initiate the variable `cupcakes`, 
  //do something with it, and then return it
};
```

> Variables are convenient because they store a value that you can reuse in your code. What if you want to reuse your instructions? That's where functions come in. They are just like variables, but instead of storing a value, they store a sequence of instructions that can be reused later.


#### Exercise(s)
- Draw Mickey Mouse, or any character that you like, at 5 different locations on the screen



<div id='arrays'/>

## Arrays

```javascript
var books = ['Harry Potter', 'Lightling Thief', 'Diary of a Wimpy Kid'];
```
> A list of similar/related values

> Before when we learned about variables, we only learned to store one value. However, using arrays, we can store multiple similar values together using only one variable.

**Notes**  
-- n/a

**Real life example:** *list of to-read books* 
- an `array` (list) of books that you will go through and read this summer

> Usually, a `for loop` is used to loop through an `array`. 

> An array's elements are indexed starting from 0. So the first element's index is 0, the second element is 1, the third element is 2, and so on. In this case, it is very convenient to use a for loop because we can make the `counter` variable (which is usually `i`) start at `0` and `increase by 1` each time. Therefore, we can easily use `array[i]` to access each element.

```javascript
var books = ['Harry Potter', 'The Lightning Thief', 'Diary of a Wimpy Kid'];
//index      0                1                      2
//we can access an element of the array using square brackets [] and an index

//arrayName.length is a convenient property that we can use
//to find the length of the array
for (var i = 0; i < books.length; i++) {
  //get the i'th index of the array 'books' and read it
  readBook(books[i]);
}
```


#### Exercise(s)
- use an array to store similar shades of a colour. Maybe with the first element being the lightest shade and the last element being the darkest shade?



<div id='objectLiterals'/>

## Object Literals

```javascript
var objectName = {
  key: value,
  key2: value2,
};
```
> Collection of related properties in the `key: value` format

**Notes**  
-- Everything around us is an object, and it has many properties. The same applies in programming.  
-- The words `property`, `key`, and `attribute` all mean the same thing so you might see any of them in different places. Don't worry about them, they're all referring to the same thing. 

**Real life example:** *water bottle* 
- *my cool water bottle is back* :sunglasses:
- what properties does my water bottle have?
- shape: cylinder
- colour: clear
- it has water
- lid colour: black
- volume: 24oz
- my water bottle is high-tech and has a cool function that can change its own colour
> When we made a function, we just assigned the function to a variable (`var functionName = function() {...}`). The same concept applies here. Since an object is just a **collection of variables**, and functions can be variables, you can also assign a function as one of the object's properties. 

```javascript
var waterBottle = {
  shape: 'cylinder',
  colour: 'clear',
  hasWater: true,
  lidColour: 'black',
  volumeInOz: 24,
  changeColour: function(newColour) { 
    //the word 'this.' is referring to this object, which is just `waterBottle`
    this.colour = newColour;
  };
};
```

> To access a property of an object, we can do `objectName.key`. For example, if we do `waterBottle.shape`, we access the `shape` property of `waterBottle` and it will give us `'cylinder'`.

> Unlike arrays, which has very tightly connected values, objects give us a `key` to work with to access a specific`value`. The `key` is essentially just like a variable name. If we were to visualize it, it's just a big container containing a bunch of related variables.  

> So why don't we use an array? Didn't you tell me that we can use an array to store related values? Am I being lied to?
> Sure, if we use an array, we can do something like this...
```javascript
var waterBottle = ['cylinder', 'clear', true, 'black', 24];
```
> ... but how are we going to remember which property is at which index? It becomes inconvenient to work with, and you don't know if `'clear'` is talking about the bottle colour or the lid colour. Unless you have a memory of a dolphin (which is extremely good), an object would be much more useful in this case.


#### Exercise(s)
- Make a `ball` that has the properties `x, y, size, colour`



<div id='constructors'/>

## Constructors

```javascript
var constructorFunctionName = function(optionalParameter) {
  //when making a new object using this constructor, 
  //the new object will have the properties defined here
  this.property = value;
  this.anotherProperty = anotherValue;
  this.moreProperty = optionalParameter;
};
```
> A constructor is something used as a template/blueprint to construct objects. The objects constructed look exactly the same as the objects constructed using object literals.

> New objects are created from a constructor using the `new` keyword

> Do keep in mind that the constructor is a function! `constructorFunctionName` does not have the properties `property`, `anotherProperty`, and `moreProperty`! Only objects made *using* this constructor function has those properties.

**Notes**  
-- Ask them if they remember what object literals are

**Real life example:** *Play-Doh molds* 
- If you have a star shaped mold, you can use it to make a `new` star shaped Play-Doh
- The Play-doh that you made from the mold will all have:
	- shape: star
	- size: 10cm wide
	- thickness: 3cm thick
```javascript
var StarPlayDoh = function() {
  //the word 'this.' is referring to the new object that you create using this constructor
  this.shape = 'star';
  this.size = 10;
  this.thickness = 3;
};

//both of these variables will have identical properties,
//which are the properties defined in the constructor
var myCooooooolestPlayDoh = new StarPlayDoh();
var mySecondStar = new StarPlayDoh();

//you can use these objects like how you would use an object literal

//this will write the word 'star' at position [200, 200]
text(mySecondStar.shape, 200, 200); 

//this will also write the word 'star' at position [200, 200]
text(myCooooooolestPlayDoh.shape, 200, 200);

```

- You can also pass in parameters when constructing the object. For example, you can have a `constructor` that makes the Play-Doh into a given  `shape` 
```javascript
var PlayDoh = function(shape) {
  this.shape = shape;
  this.size = 10;
  this.thickness = 3;
};

//create a Play-Doh with its shape property being cat 
//(cat shaped Play-Doh)
var catPlayDoh = new PlayDoh('cat');

//now this will write the word 'cat' on the screen
text(catPlaydoh.shape, 200, 200); 
```
> Constructors are very useful if you want to create objects that have the same properties but different values

> This also allows us to create objects programmatically rather than typing in a thousand similar `object literals` by hand, which can be impossible

If you made it this far, great work! These are difficult to grasp concepts. Psssssst, don't tell the others, but there is a small chance that some of the coaches here might not understand constructors

#### Exercise(s)
- Make balls that has a method called `draw()` that draws themselves onto the screen

#### Challenge
- Make circles rain from the sky


TODO: I wonder if anyone will ask about more advanced concepts of JS...
