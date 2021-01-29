//size of the screen:
var SIZE = 800;

function setup() {
  createCanvas(SIZE, SIZE);  
}

//priority
//check for cohesion
//then check steering for separation
//lastly, align the vector


const NUM_BOIDS = 200;
const COHERANCE = 15;
const ALIGNMENT = 30;
const SEPERATION = 10;
let pause = false;

const Boid = function(
  xPos = Math.round(Math.random()*SIZE), 
  yPos = Math.round(Math.random()*SIZE),
) {
  this.xPos = xPos;
  this.yPos = yPos;
  //velocity vector
  this.velocity = this.getRandomVelocity();
};

Boid.prototype.speed = 2;
//vector has the magnitude of Boid.prototype.speed
Boid.prototype.getRandomVelocity = function() {
  const x = Math.random()*this.speed*2-this.speed;
  const y = Math.sqrt(Math.pow(this.speed, 2)-Math.pow(x, 2)) 
          * (Math.random() > 0.5 ? 1 : -1);
  return {
    x: x,
    y: y,
  };

};

Boid.prototype.display = function() {
  const tip = [this.velocity.x*5 + this.xPos, this.velocity.y*5 + this.yPos];
  // const slope = this.velocity.y/this.velocity.x;
  // const bottomLeft = [];
  // triangle(...tip, );
  fill(0);
  ellipse(this.xPos, this.yPos, 4, 4);
  line(...tip, this.xPos, this.yPos);
};

Boid.prototype.move = function() {
  this.xPos += this.velocity.x;
  this.yPos += this.velocity.y;
  this.xPos = this.xPos > 0 ? this.xPos % SIZE : SIZE - this.xPos;
  this.yPos = this.yPos > 0 ? this.yPos % SIZE : SIZE - this.yPos;
};

Boid.prototype.findNeighbours = function(boids, radius) {
  //linear search
  const neighbours = [];
  boids.forEach(boid => {
    if (
      (Math.abs(boid.xPos - this.xPos) <= radius 
        || Math.abs(this.xPos - boid.xPos) <= radius)
      && (Math.abs(boid.yPos - this.yPos) <= radius 
          || Math.abs(this.yPos - boid.yPos) <= radius)
      && Math.sqrt(Math.pow(boid.xPos-this.xPos, 2)
         + Math.pow(boid.yPos-this.yPos, 2))
    ) {
      neighbours.push(boid);
    }
  });
  return neighbours;
};

Boid.prototype.cohesionSteering = function(boids) {
  //no neighbours
  const neighbours = this.findNeighbours(boids, COHERANCE);
  if (neighbours.length === 0) return;

  let xTotal = 0;
  let yTotal = 0;
  neighbours.forEach(neighbour => {
    xTotal += neighbour.xPos;
    yTotal += neighbour.yPos;
  });
  const xAvg = xTotal > 0 ? xTotal / neighbours.length : 0;
  const yAvg = yTotal > 0 ? yTotal / neighbours.length : 0;

  //scaling the vector so the magnitude will equal to speed
  const magnitude = Math.sqrt(
    Math.pow(this.xPos-xAvg, 2) 
    + Math.pow(this.yPos-yAvg, 2)
  );
  const scaleFactor = magnitude / this.speed / 2;
  this.velocity.x = -(this.xPos-xAvg) / scaleFactor;
  this.velocity.y = -(this.yPos-yAvg) / scaleFactor;
  fill(10, 255, 10);
  ellipse(this.xPos, this.yPos, 4, 4);
};


Boid.prototype.align = function(boids) {
  const neighbours = this.findNeighbours(boids, ALIGNMENT);
  if (neighbours.length === 0) return;

  let xDirTotal = 0;
  let yDirTotal = 0;
  neighbours.forEach(boid => {
    xDirTotal += boid.velocity.x;
    yDirTotal += boid.velocity.y;
  });
  const magnitude = Math.sqrt(
    Math.pow(xDirTotal, 2) 
    + Math.pow(yDirTotal, 2)
  );
  const scaleFactor = magnitude / this.speed;
  this.velocity.x = xDirTotal / scaleFactor;
  this.velocity.y = yDirTotal / scaleFactor;
  fill(10, 0, 255);
  ellipse(this.xPos, this.yPos, 4, 4);
  // console.log(this.velocity);
};


Boid.prototype.seperationSteering = function(boids) {
  const neighbours = this.findNeighbours(boids, SEPERATION);
  if (neighbours.length === 0) return;

  let xDirTotal = 0;
  let yDirTotal = 0;
  neighbours.forEach(neighbour => {
    const magnitude = Math.sqrt(
      Math.pow(this.xPos-neighbour.xPos, 2) 
      + Math.pow(this.yPos-neighbour.yPos, 2)
    );
    const scaleFactor = magnitude / this.speed;
    xDirTotal += (this.xPos - neighbour.xPos) / scaleFactor;
    yDirTotal += (this.yPos - neighbour.yPos) / scaleFactor;
  });
  const magnitude = Math.sqrt(
    Math.pow(xDirTotal, 2) 
    + Math.pow(yDirTotal, 2)
  );
  const scaleFactor = magnitude / this.speed;
  this.velocity.x = xDirTotal / scaleFactor;
  this.velocity.y = yDirTotal / scaleFactor;
  fill(255, 0, 100);
  ellipse(this.xPos, this.yPos, 4, 4);
};


const boids = [];

function mouseClicked() {
  boids.push(new Boid(mouseX, mouseY));
  boids.shift();
};

function keyPressed() {
  const SPACE = 32;
  if (keyCode === SPACE) {
    pause = !pause;
  }
};


//green = cohesion
//blue = align
//red = separation

function draw() {
  if (pause) return;
  background(220);
  if (boids.length < NUM_BOIDS) {
    boids.push(new Boid());
  }
  boids.forEach(boid => {
    boid.display();
    boid.align(boids);
    boid.cohesionSteering(boids);
    boid.seperationSteering(boids);
    boid.move();
  });
};