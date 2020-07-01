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
> Name for the data that we store

**Notes**  
-- Ask if they know what *x* is in math

**Real life example:** *water bottle named Winnie* 
- Instead of saying "pass me that `clear water bottle`", we say "pass me `Winnie`" 
(`var Winnie = clear water bottle`) 
- the name is special
	- each name is unique, meaning that there can't be two of the same names in one program
	- you can change what you assign the name to. For example, I can make `Winnie` the name of my `pencil`, but then my `clear water bottle` is no longer named `Winnie`

> Convenient, example in coding is if we have a certain `size` that we want to reuse but don't want to type in the number each time 


#### Exercises
- Hold the ball (draw multiple circles at different places with the same size)



<div id='forLoops'/>

## For Loops

```javascript
for (initializer[starting point]; condition; statement2) {
  //the code here will execute as long
  //as the condition is met
	
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
- Starting at `lap 0`, as long as you ran less than `10 laps`, you have to `run around`. Each time after you `ran 1 lap`, the total number of `laps ran is incremented by 1`

> If we want the code to do the same thing, we can just put it inside a `for loop` rather than copying and pasting it `n times`

> Convenient once you get to arrays (using loops to get every value in the array)

#### Exercises
- Draw 10 dots across the screen with each dot being 10 pixels apart



<div id='whileLoops'/>

## While Loops

```javascript
while (condition) {
  //code to execute
}
----------------------
while (sleeping) {
  wearPajamas(); //pretend this function exists
}
```
> Loops through a certain block of code an unknown number of times while the condition is true

**Notes**  
-- n/a

**Real life example:** 
- same as what the word `while` means in real life
- while `blah blah blah is happening...`, you do `blah blah blah...`
- while you're sleeping, wear your pajamas

> `While loop` are convenient if you are unsure of how many times a certain block of code have to run. For example, you can ask the user to input something, and let's say, `while` the user does not input the word `STOP`, you will continue asking for user input.

TODO: add a picture of what I mean for stacking circles


#### Exercises
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
- Same as the while loop, it's just what `if` and `else` means in plain English 
- `If` you are wearing a red shirt, do a jumping jack. `Else`, do a push up.

> A lot of decisions in the code are made through conditions such as your mouse position, if something is greater than another, etc.


#### Exercises
- Hold the ball - if your mouse is on the upper half of the screen, draw a rectangle. Otherwise, draw a circle.


<div id='functions'/>

## Functions

```javascript
var functionName = function(optionalParameters) {
  //do some cool stuff
  //can use the parameters passed to the function
  //optionally return a value
};
```
> A block of organized and reusable code that is used to perform a task

**Notes**  
-- Does this look confusing? You feel like everything is everywhere and there's all the random vocabulary that makes no sense? Welp, don't worry, because ~~I honestly feel the same way~~

**Real life example:** *do homework* 
- get pencil
- get eraser
- get handouts
- read questions
- think of answer
- write down the answer
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

**Real life example:** *you are a professional baker, therefore you are responsible for executing the function `getCupcakes` given the icing `flavour`* 
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

  //we can include a conditional for checking what to do given a flavour
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

> Variables are convenient because they store a value that you can reuse in your code, but what if you want to reuse your instructions? That's where functions come in, they are just like variables, but instead of storing a value, they store a sequence of code that can be reused later.


#### Exercises
- Draw Mickey Mouse, or any character that you like, at 5 different locations on the screen



<div id='arrays'/>

## Arrays

```javascript
var books = ['Harry Potter', 'Lightling Thief', 'Diary of a Wimpy Kid'];
```
> A list of similar/related values

> Before when we learned about variables, we only learned to store one value. However, using arrays, we can store similar values altogether inside one variable.

**Notes**  
-- n/a

**Real life example:** *list of to-read books* 
- an `array` of books that you will go through and read this summer

> Usually, a `for loop` is used to loop through the `array`

```javascript
var books = ['Harry Potter', 'Lightling Thief', 'Diary of a Wimpy Kid'];
//index      0                1                  2
//we can access an element of the array using square brackets [] and an index

//arrayName.length is a convenient property that we can use
//to find the length of the array
for (var i = 0; i < books.length; i++) {
  //the i'th index of the array books 
  readBook(books[i]);
}
```


#### Exercises
- an array to store similar shades of a colour. Maybe with the first element being the lightest shade and the last element being the darkest shade?



<div id='objectLiterals'/>

## Object Literals

```javascript
var objectName = {
  key: value,
  key2: value2,
};
```
> Collection of properties in the `key: value` format

>  Essentially a collection of related variables (note, not *just* related *values* as opposed to an array) 

**Notes**  
-- Everything around us is an object, and it has many properties. The same applies in programming.  
-- The words `property`, `key`, `attribute` can be used interchangeably so you might see different words looking at different places. Just don't worry about them, they're all referring to the same thing. 

**Real life example:** *water bottle* 
- *my cool water bottle is back* :sunglasses:
- what observations can we make?
- shape: cylinder
- colour: clear
- it has water
- lid colour: black
- volume: 24oz
- my water bottle has a cool function that change its own colour
> Remember when we made a function, we just assigned the function to a variable (`var functionName = function() {...}`). The same concept applies here. Since I said that and object is just a **collection of variables**, and variables can be functions. Therefore, you can also assign a function as one of the object's properties

```javascript
var waterBottle = {
  shape: 'cylinder',
  colour: 'clear',
  hasWater: true,
  lidColour: 'black',
  volumeInOz: 24,
  changeColour: function() { 
    //the word 'this.' is referring to this object, which is just `waterBottle`
    this.colour = randomColour();
  };
};
```

> To access a property of the object, we can easily do `objectName.key`. In this case, if we do something like `waterBottle.shape`, it will give us `'cylinder'`.

> Unlike arrays with very tightly connected values. Objects give us a `key` to work with, which is essentially just like a variable name. To visualize it, it's just a big box containing a bunch of related variables.  

> If we were to use an array, like sure, we can do something like 
```javascript
var waterBottle = ['cylinder', 'clear', true, 'black', 24];
```
> But how are we going to remember which property is at which index? Like it's so easy to forget that `'clear'` is talking about the bottle colour and not the lid colour. Unless you have a memory of a dolphin (which is extremely good), I'd recommend you to use an object in this case to save some trouble...


#### Exercises
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
> A constructor, is something used as a template/blueprint to construct objects. The objects constructed look exactly the same as the objects constructed through the method of making object literals.

> New objects are created from a constructor using the `new` keyword

**Notes**  
-- Ask them if they remember what object literals are

**Real life example:** *Play-Doh molds* 
- If you have a star shaped mold, you can use it to make `new` star shaped Play-Dohs
- The Play-doh that you made from the mold will all have:
	- shape: star
	- size: 10cm wide
	- thickness: 3cm thick
```javascript
var StarPlayDoh = function() {
  //the word 'this.' is referring to the new object that you create
  this.shape = 'star';
  this.size = 10;
  this.thickness = 3;
};

//both of these variables will have identical properties,
//which is the properties defined in the constructor
var myCooooooolestPlayDoh = new StarPlayDoh();
var mySecondStar = new StarPlayDoh();

//you can use these objects like how you would use an object literal

//this will write the word 'star' at position [200, 200]
text(mySecondStar.shape, 200, 200); 

//this will also write the word 'star' at position [200, 200]
text(myCooooooolestPlayDoh.shape, 200, 200);

```

- You can also pass in parameters when when constructing the object. For example, you can have a `constructor` that makes the Play-Doh into a given  `shape` 
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
> They are very useful if you want to create objects that have the same properties but different values

> This also enables us to create objects programmatically rather than typing in a thousand similar `object literals` by hand. And sometimes, it is just impossible

If you made it this far, great! Because these are difficult to grasp concepts. Pssssss, don't tell others, but maybe some of the coaches here don't even understand constructors

#### Exercises
- Make balls that has a method called `draw()` that draws themselves onto the screen

#### Challenge
- Make circles rain from the sky


TODO: I wonder if anyone will ask about more advanced concepts of JS...
