function setup() {
  createCanvas(400, 400);
}

/////copy and paste the following for hatch
var NUM_ANTIBODIES = 20;
var SIZE = 400;

var Cell = function() {
  this.xPos = 200;
  this.yPos = 200;
  this.width = 200;
  this.height = 100;
  this.maxSize = SIZE;
  this.numMoleculesInside = 0;
  this.grow = function() {
    this.width += 0.5;
    this.height += 0.5;
    this.numMoleculesInside++;
    if (this.width >= this.maxSize || this.height >= this.maxSize) {
      this.reset();
    }
  };
  this.reset = function() {
    this.width = 200;
    this.height = 100;
    this.numMoleculesInside = 0;
  };
  this.display = function() {
    fill(232, 102, 102);
    ellipse(
      this.xPos, 
      this.yPos, 
      this.width, 
      this.height);
    fill(50);
    text(this.numMoleculesInside, this.xPos, this.yPos);
  };
};

var Antibody = function(xPos, yPos) {
  this.xPos = xPos;
  this.yPos = yPos;
  this.size = 5;
  this.targetX = 200;
  this.targetY = 200;

  this.move = function() {
    this.xPos += this.targetX > this.xPos ? 1 : -1;
    this.yPos += this.targetY > this.yPos ? 1 : -1;
  };
  this.collide = function(cell) {
    var left = cell.xPos - cell.width/2 + this.size;
    var right = cell.xPos + cell.width/2 - this.size;
    var up = cell.yPos  - cell.height/2 + this.size;
    var down = cell.yPos + cell.height/2 - this.size;
    if (this.xPos > left
        && this.xPos < right
        && this.yPos > up
        && this.yPos < down) {
      return true;
    }
    return false;
  };
  this.display = function() {
    fill(200);
    ellipse(this.xPos, this.yPos, this.size, this.size);
  };
};
var cell = new Cell();
var antibodies = [];


var checkCollision = function() {
  antibodies.forEach(function(antibody) {
    if (antibody.collide(cell)) {
      cell.grow();
    };
  });
};

var removeCollided = function() {
  antibodies = antibodies.filter(function(antibody) {
    return !antibody.collide(cell);
  });
};

var addAntibodies = function() {
  if (antibodies.length < NUM_ANTIBODIES) {
    antibodies.push(new Antibody(random(0, SIZE), random(0, SIZE)));
  }
};

var displayAntibodies = function() {
  antibodies.forEach(function(antibody) {
    antibody.display();
    antibody.move();
  });
}; 

var draw = function() {
  background(220);
  cell.display();
  addAntibodies();
  displayAntibodies();
  checkCollision();
  removeCollided();
};