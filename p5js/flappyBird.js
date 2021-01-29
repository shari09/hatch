//size of the screen:
var SIZE = 400;

function setup() {
  createCanvas(SIZE, SIZE);  
}

var GRAVITY = 0.3;

var Bird = function() {
  this.xPos = SIZE/3;
  this.yPos = SIZE/2;
  this.size = 30;
  this.vel = 0;
  this.move = function() {
    this.vel = -GRAVITY*19;
  };
  this.update = function() {
    this.yPos += this.vel;
    this.vel += GRAVITY;
  };
  this.display = function() {
    fill(212, 70, 44);
    noStroke();
    ellipse(this.xPos, this.yPos, this.size, this.size);
  };
  this.outOfScreen = function() {
    if (this.yPos < 0 || this.yPos > SIZE) {
      return true;
    }
  };
};

var Pipe = function(xPos, yPos, width, height) {
  this.xPos = xPos;
  this.yPos = yPos;
  this.width = width;
  this.height = height;
  this.updateX = function(xPos) {
    this.xPos = xPos;
  }
  this.display = function() {
    fill(21, 194, 16);
    rect(this.xPos, this.yPos, this.width, this.height);
  };
};

var PipePair = function() {
  this.xPos = SIZE;

  this.width = parseInt(Math.random()*20)+30;
  this.gapSize = parseInt(Math.random()*30)+90;
  this.gapY = parseInt(Math.random()*(SIZE-this.gapSize));
  this.pipes = [new Pipe(this.xPos, 0, this.width, this.gapY),
                new Pipe(this.xPos, this.gapY+this.gapSize, 
                         this.width, SIZE-this.gapY+this.gapSize)];

  this.display = function() {
    this.pipes.forEach(pipe => pipe.display());
  };

  this.move = function() {
    this.xPos -= 1;
    this.pipes.forEach(pipe => pipe.updateX(this.xPos));
  };

  this.canAddPipe = function() {
    if (this.xPos < SIZE/2) {
      return true;
    }
  };

  this.outOfScreen = function() {
    if (this.xPos + this.width < 0) {
      return true;
    }
  };
};

var bird = new Bird();
var pipes = [];
pipes.push(new PipePair());

var keyPressed = function() {
  //32 is ascii for space bar
  if (keyCode === 32) {
    bird.move();
  }
};

var updatePipes = function() {
  if (pipes.every(pipe => pipe.canAddPipe())) {
    pipes.push(new PipePair());
  }
  pipes = pipes.filter(pipe => !pipe.outOfScreen());
  
  pipes.forEach(pipe => {
    pipe.move();
    pipe.display();
  });
};

var collide = function(circle, rect) {
    var distX = Math.abs(circle.xPos-(rect.xPos+rect.width/2));
    var distY = Math.abs(circle.yPos-(rect.yPos+rect.height/2));

    if (distX > (rect.width/2 + circle.size/2)) { return false; }
    if (distY > (rect.height/2 + circle.size/2)) { return false; }

    if (distX <= (rect.width/2)) { return true; } 
    if (distY <= (rect.height/2)) { return true; }

    var distSquared = Math.pow((distX - rect.width/2), 2) +
                         Math.pow((distY - rect.height/2), 2);

    return (distSquared <= Math.pow(circle.size/2, 2));
};

var gameOver = false;
var draw = function() {
  background(220);

  if (!gameOver) {
    bird.update();
    bird.display();
    updatePipes();
    var collided = pipes.some(pipePair => pipePair.pipes.some(pipe => {
      return collide(bird, pipe);
    }));
    gameOver = bird.outOfScreen() || collided;
  } else {
    textAlign(CENTER);
    fill(50);
    textSize(100);
    text('GAME', SIZE/2, SIZE/2);
    text('OVER', SIZE/2, SIZE/4*3);
  }

};