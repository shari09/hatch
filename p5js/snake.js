var SIZE = 400;

////////ignore this for hatch ide
function setup() {
  createCanvas(SIZE, SIZE);
}
///////////

var BLOCK_SIZE = 20;
var numApples = 10;

var Apple = function(xPos, yPos) {
  this.xPos = xPos;
  this.yPos = yPos;
  this.display = function() {
    fill(129, 194, 68);
    ellipse(this.xPos*BLOCK_SIZE + BLOCK_SIZE/2, 
            this.yPos*BLOCK_SIZE + BLOCK_SIZE/2, 
            BLOCK_SIZE, 
            BLOCK_SIZE);
  };
};

var Block = function(xPos, yPos) {
  this.xPos = xPos;
  this.yPos = yPos;
  this.width = BLOCK_SIZE;
  this.height = BLOCK_SIZE;
  this.colour = [214, 137, 64];
  this.display = function() {
    fill(...this.colour);
    rect(this.xPos*BLOCK_SIZE, 
         this.yPos*BLOCK_SIZE, 
         this.width, this.height);
  };
};

var Snake = function() {
  //              d, r,  l,  u   
  this.xChange = [0, 1, -1, 0];
  this.yChange = [1, 0, 0, -1];
  this.dir = 1;
  this.blocks = [new Block(0, 0)];
  this.goDown = function() {
    this.dir = 0;
  };
  this.goRight = function() {
    this.dir = 1;
  };
  this.goLeft = function() {
    this.dir = 2;
  };
  this.goUp = function() {
    this.dir = 3;
  };
  this.grow = function() {
    this.blocks.unshift(new Block(
      this.blocks[0].xPos+this.xChange[this.dir],
      this.blocks[0].yPos+this.yChange[this.dir]
    ));
  };
  this.move = function() {
    this.grow();
    this.blocks.pop();
  };
  this.display = function() {
    this.blocks.forEach(function(block) {
      block.display();
    });
  };
  this.dead = function() {
    var head = this.blocks[0];
    if (head.xPos < 0 
        || head.xPos*(head.width+1) > SIZE
        || head.yPos < 0 
        || head.yPos*(head.height+1) > SIZE) {
      return true;
    }
    for (var i = 1; i < this.blocks.length; i++) {
      if (head.xPos === this.blocks[i].xPos
          && head.yPos === this.blocks[i].yPos) {
        return true;
      }
    }
  };
};

var snake = new Snake();
var apples = [new Apple(0, 2)];
var gameOver = false;

var generateApples = function() {
  if (apples.length < numApples) {
    apples.push(new Apple(Math.floor(Math.random()*SIZE/BLOCK_SIZE),
                          Math.floor(Math.random()*SIZE/BLOCK_SIZE)));
  }
};

var moveSnake = function() {
  var head = snake.blocks[0];
  var pLen = apples.length;
  apples = apples.filter(function(apple) {
    return !(head.xPos === apple.xPos && head.yPos === apple.yPos);
  });
  if (apples.length !== pLen && pLen === numApples) {
    snake.grow();
  } else {
    snake.move();
  }
  if (snake.dead()) {
    gameOver = true;
  }
};

var displayApples = function() {
  apples.forEach(function(apple) {
    apple.display();
  });
};

var keyTyped = function() {
  //hatch ide doesn't support one line if statements
  //wrap the expressions in curly brackets
  if (key === 'a') snake.goLeft();
  else if (key === 'd') snake.goRight();
  else if (key === 'w') snake.goUp();
  else if (key === 's') snake.goDown();
};

var timer = 0;
var draw = function() {
  if (!gameOver) {
    background(220);
    generateApples();
    displayApples();
    snake.display();
    timer++;
    if (timer === 30) { //modify timer to be max 5 for hatch ide
      timer = 0;
      moveSnake();
    }
  } else {
    textSize(50);
    textAlign(CENTER);
    text('GAME OVER', 200, 200);
  }
  
};