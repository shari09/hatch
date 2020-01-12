
var SIZE = 400;


function setup() {
  createCanvas(400, 400);
}

var OFFSET_Y = 200;

var Medium = function() {
  this.pulses = [];
  this.y = 0;
  this.speed = 40;
  this.addPulse = function(x=0) {
    this.pulses.push(new Pulse(50, 30, x));
  };

  this.display = function() {
    stroke(0);
    for (var xPos = 0; xPos < SIZE; xPos++) {
      var collidingPulses = this.pulses.filter(pulse => pulse.inPulse);
      var yPos = collidingPulses.reduce((accumulator, pulse) => {
        return accumulator + pulse.getPos(xPos);
      });
      point(xPos, yPos+OFFSET_Y);
    }
  };
  this.update = function() {
    this.pulses.forEach(pulse => pulse.move());
  }

}

var Pulse = function(amplitude, waveLength, xPos) {
  this.dir = 1;
  this.amplitude = amplitude;
  this.waveLength = width;
  this.xPos = xPos;
  this.speed = 1;
  this.move = function() {
    if (this.xPos+this.waveLength > SIZE) {
      this.dir = -1;
    } else if (this.xPos < 0) {
      this.dir = 1;
    }
    this.xPos += this.speed;
  };
  this.inPulse = function(xPos) {
    return (this.xPos < xPos && xPos < this.xPos+this.waveLength);
  }
  this.getPos = function(xPos) {
    return Math.sin(xPos-this.xPos)*this.amplitude;
  }
};

var string = new Medium();
var draw = function() {
  background(220);
  // string.addPulse();
  // string.display();
};