function setup() {
  createCanvas(SIZE, SIZE);
  for (var i = 0; i < 100; i++) {
    antibodies.push(new Antibody(
      random(cell.xPos-50, cell.xPos+cell.height/2), 
      random(cell.yPos-50, cell.yPos+cell.height/2)
    ));
  }
}

/////copy and paste the following for hatch
var NUM_ANTIBODIES = 3;
var SIZE = 400;

var Cell = function() {
  this.xPos = SIZE/2;
  this.yPos = SIZE/2;
  this.width = SIZE;
  this.height = SIZE/2;
  this.minSize = 50;
  this.numMoleculesInside = 100;
  this.shrink = function() {
    this.width -= 0.5;
    this.height -= 0.5;
    this.numMoleculesInside--;
    if (this.width <= this.minSize || this.height <= this.minSize) {
      this.reset();
    }
  };
  this.reset = function() {
    this.width = SIZE;
    this.height = SIZE/2;
    this.numMoleculesInside = 100;
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
  this.awayX = SIZE/2;
  this.awayY = SIZE/2;

  this.move = function() {
    this.xPos += this.awayX > this.xPos ? -1 : 1;
    this.yPos += this.awayY > this.yPos ? -1 : 1;
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
  this.inScreen = function() {
    if (this.xPos+this.size < 0
        || this.xPos-this.size > SIZE
        || this.yPos+this.size > SIZE
        || this.yPos-this.size < 0) {
      return false;
    }
    return true;
  };
  this.display = function() {
    fill(200);
    ellipse(this.xPos, this.yPos, this.size, this.size);
  };
};
var cell = new Cell();
var antibodies = [];



var displayAntibodies = function() {
  antibodies.forEach(function(antibody) {
    antibody.display();
    antibody.move();
  });
};

// var checkCollision = function() {
//   antibodies = antibodies.map(function(antibody) {
//     if (!antibody.collide(cell)) {
//       cell.shrink();
//     }
//     if (!antibody.inScreen()) {
//       return;
//     }
//     return antibody;
//   });
// };

var draw = function() {
  background(220);
  cell.display();
  displayAntibodies();
  // checkCollision();
};