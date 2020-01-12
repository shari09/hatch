//size of the screen:
var SIZE = 400;

function setup() {
  createCanvas(SIZE, SIZE);
  angleMode(DEGREES);
  
}

// configuration //////////////////////

// amplitudes, in pixels
var AMP    = [100, 50, -20];
// waveLengths, in pixels
var WAVE_LENGTH = [360, 180, 100];
// horizontal speeds, in pixels per loop
var SPEED  = [3, 1, 2];

//////////////////////////////////

var OFFSET_Y = SIZE/2; 

// time
var t = 0;

// for drawing the original waves
var y;
var yPrev = [0, 0, 0];

// for drawing the final combined wave
var ySum;
var ySumPrev = 0;

// to calculate the coefficient on x
// beforehand instead of during every single
// draw
var X_SCALE = [];


for (var i = 0; i < WAVE_LENGTH.length; i++) {
  // waveLength of sin(kx) = 360degrees/k
  // so k = 360/waveLength
  X_SCALE[i] = 360/WAVE_LENGTH[i];
}


var draw = function() {
  background(220);
  
  for (var x = 0; x < SIZE; x++) {
    ySum = 0;
    stroke(0, 0, 255);
    strokeWeight(0.2);
    
    for (var i = 0; i < AMP.length; i++) {
      y = AMP[i] * sin(X_SCALE[i] * (x+t*SPEED[i]));
      line(x, y+OFFSET_Y, x-1, yPrev[i]+OFFSET_Y);
      
      ySum += y;
      yPrev[i] = y;
    }
    
    stroke(255, 0, 0);
    strokeWeight(1);
    line(x, ySum+OFFSET_Y, x-1, ySumPrev+OFFSET_Y);
    ySumPrev = ySum;
  }
  
  t++;
};