//for hatch IDE
var SIZE = 400;

function setup() {
  createCanvas(400, 400);
}

var Molecule = function(xPos, yPos, targetX, targetY) {
  this.xPos = xPos;
  this.yPos = yPos;
  this.size = 4;
  this.targetX = targetX;
  this.targetY = targetY;
  this.xSpeed = Math.abs(this.targetX-this.xPos)/(SIZE/2);
  this.ySpeed = Math.abs(this.targetY-this.yPos)/(SIZE/2);
  this.display = function() {
    stroke(0);
    strokeWeight(1);
    fill(130);
    ellipse(this.xPos, this.yPos, this.size, this.size);
  };
  this.move = function() {
    this.xPos += this.targetX > this.xPos ? this.xSpeed : -this.xSpeed;
    this.yPos += this.targetY > this.yPos ? this.ySpeed : -this.ySpeed;
  };
  this.end = function() {
    if (this.targetX+this.xSpeed > this.xPos
        && this.targetX-this.xSpeed < this.xPos
        && this.targetY+this.ySpeed > this.yPos
        && this.targetY-this.ySpeed < this.yPos) {
      return true;
    }
    return false;
  };
};

var molecules = [];

var generateMolecules = function() {
  molecules = [];
  var num = random(20, 70);
  var gap = SIZE/Math.sqrt(num);
  var offset = gap/4;
  for (var i = 0; i < SIZE; i+=gap) {
    for (var j = 0; j < SIZE; j+=gap) {
      molecules.push(new Molecule(random(0, SIZE), random(0, SIZE), i+offset, j+offset)); 
    }
  }
};


var displayMolecules = function() {
  molecules.forEach(function(molecule) {
    molecule.display();
    molecule.move();
  });
  
};

// generateMolecules();

var draw = function() {
  background(220);
  displayMolecules();
  if (molecules.every(function(molecule) {return molecule.end()})) {
    generateMolecules();
  }
};

  
