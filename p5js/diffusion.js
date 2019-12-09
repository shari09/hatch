//for hatch IDE
var SIZE = 400;

var Molecule = function(xPos, yPos, targetX, targetY) {
  this.xPos = xPos;
  this.yPos = yPos;
  this.size = 4;
  this.targetX = targetX;
  this.targetY = targetY;
  this.xSpeed = (this.targetX-this.xPos)/(SIZE/2);
  this.ySpeed = (this.targetY-this.yPos)/(SIZE/2);
  this.display = function() {
    stroke(0);
    strokeWeight(1);
    fill(130);
    ellipse(this.xPos, this.yPos, this.size, this.size);
  };
  this.move = function() {
    this.xPos += this.targetX===this.xPos ? 0 : this.xSpeed;
    this.yPos += this.targetY===this.yPos ? 0 : this.ySpeed;
  };
  this.end = function() {
    return (this.xPos === this.targetX && this.yPos === this.targetY);
  };
};

var molecules = [];

var generateMolecules = function() {
  molecules = [];
  var num = 16;
  var gap = SIZE/Math.sqrt(num);
  var offset = gap/2;
  for (var i = 0; i < SIZE; i+=gap) {
    for (var j = 0; j < SIZE; j+=gap) {
      molecules.push(new Molecule(0, SIZE, i+offset, j+offset)); 
    }
  }
};


var displayMolecules = function() {
  molecules.forEach(function(molecule) {
    molecule.display();
    molecule.move();
  });
  
};

generateMolecules();

var draw = function() {
  background(220);
  displayMolecules();
  if (molecules.every(function(molecule) {return molecule.end()})) {
    generateMolecules();
  }
};

  
