//size of the screen:
var SIZE = 400;

function setup() {
  createCanvas(SIZE, SIZE);
}
////////////////////////////

const asteroids = [];
const projectiles = [];
const circleBorder = {
  x: 200,
  y: 200,
  radius: 170,
};
let score = 0;
let gameOver = false;
/////////////////////////////

/**
 * Returns the square of a number.
 * @param {number} num   the number to square 
 */
const square = (num) => {
  return Math.pow(num, 2);
};

/**
 * Returns a random number between the given range.
 * @param {number} min   the min number
 * @param {number} max   the max number
 * @returns {number}  the random number between min and max
 */
const randNum = (min, max) => {
  return Math.random() * (max - min) + min;
};

/**
 * Checks if two circles are colliding.
 * @param {circle} a   the first circle 
 * @param {circle} b   the second circle 
 */
const isCollide = (a, b) => {
  const dist = Math.sqrt(square(a.x - b.x) + square(a.y - b.y));
  return dist <= (a.size/2 + b.size/2);
};

/**
 * Creates an asteroid that moves through space.
 * @constructor
 * @param {number} x       the initial x position of the asteroid
 * @param {number} y       the initial y position of the asteroid
 * @param {number} size    the size of the asteroid
 * @param {number} speed   the speed of the asteroid
 */
function Asteroid(x, y, size, speed) {
  this.x = x;
  this.y = y;
  this.size = size;
  this.velocity = (() => {
    const xSpeed = randNum(-speed, speed);
    const yDir = Math.random() > 0.5 ? 1 : -1;
    const ySpeed = Math.sqrt(square(speed) - square(xSpeed)) * yDir;
    return {
      x: xSpeed,
      y: ySpeed,
    };
  })();
}

/**
 * Moves the asteroid based on its velocity.
 */
Asteroid.prototype.move = function() {
  this.x += this.velocity.x;
  this.y += this.velocity.y;
};


Asteroid.prototype.circleBorder = circleBorder;

/**
 * Checks whether the asteroid collides with the border.
 * @param {*} circleBorder   the circle border properties (x, y, radius)
 */
Asteroid.prototype.isBorderCollide = function(circleBorder = this.circleBorder) {
  const dist = Math.sqrt(
    square(this.x - circleBorder.x) + square(this.y - circleBorder.y)
  );
  return dist >= circleBorder.radius;
};


/**
 * Draws the asteroid.
 */
Asteroid.prototype.draw = function() {
  fill(56, 156, 106);
  ellipse(this.x, this.y, this.size, this.size);
};


/**
 * Represents an asteroid emitter.
 * @constructor
 * @param {number} x       the x position
 * @param {number} y       the y position
 * @param {number} size    the size/diameter
 */
function AsteroidEmitter(x, y, size) {
  this.x = x;
  this.y = y;
  this.size = size;
}

AsteroidEmitter.prototype.draw = function() {
  fill(0);
  ellipse(this.x, this.y, this.size, this.size);
};

AsteroidEmitter.prototype.emitAsteroid = function() {
  asteroids.push(new Asteroid(this.x, this.y, 20, randNum(0.2, 0.8)));
};


function Character(circleBorder, centerPoint) {
  this.x = 0;
  this.y = 0;
  this.centerPoint = centerPoint;
  this.circleBorder = circleBorder;
}


/**
 * Updates the position of the character based on where the mouse is.  
 * 
 * Logic derived from:  
 * (x-h)^2 + (y-k)^2 = r^2    the circle with center at (h, k)  
 * y = mx + b                 the slope of mouse to center point  
 * 
 * x^2-2hx+h^2 + y^2-2ky+k^2 = r^2
 * x^2-2hx+h^2 + (mx+b)^2-2k(mx+b)+k^2 = r^2
 * x^2-2hx+h^2 + m^2(x^2)+2bmx+b^2 - 2kmx-2kb + k^2 = r^2
 * 
 * a = m^2+1
 * b = 2bm-2h-2km
 * c = h^2+b^2+k^2-2kb-r^2
 * 
 * quadratic equation:  
 * x = (-b ± √(b^2 - 4ac))/2a
 * 
 * then use y = mx + b to get the y for the two roots 
 * 
 * @param {number} x    the mouse x position 
 * @param {number} y    the mouse y position
 */
Character.prototype.updatePosition = function(x, y) {
  const m = (y - this.centerPoint.y)/(x - this.centerPoint.x);
  const b = y - m*x;
  const lineF = (x) => m*x + b;
  
  const h = this.circleBorder.x;
  const k = this.circleBorder.y;
  const r = this.circleBorder.radius;

  const qa = square(m)+1;
  const qb = 2*m*b-2*h-2*k*m;
  const qc = square(h)+square(b)+square(k)-2*k*b-square(r);

  const x1 = (-qb + Math.sqrt(square(qb) - 4*qa*qc)) / (2*qa);
  const x2 = (-qb - Math.sqrt(square(qb) - 4*qa*qc)) / (2*qa);

  const y1 = lineF(x1);
  const y2 = lineF(x2);

  if (   (y > this.centerPoint.y && y1 > this.centerPoint.y) 
      || (y < this.centerPoint.y && y1 < this.centerPoint.y)) {
    this.x = x1;
    this.y = y1;
  } else {
    this.x = x2;
    this.y = y2;
  }
}

Character.prototype.draw = function() {
  fill(240, 155, 65);
  ellipse(this.x, this.y, 20, 20);
}


Character.prototype.emitProjectile = function() {
  const speed = 2;
  const dividingFactor = this.circleBorder.radius / speed;
  const velocity = {
    x: -(this.x - this.centerPoint.x) / dividingFactor,
    y: -(this.y - this.centerPoint.y) / dividingFactor,
  };
  projectiles.push(new Projectile(this.x, this.y, velocity));
}


/**
 * Creates a projectile.
 * @param {number} x           the initial x position
 * @param {number} y           the initial y position
 * @param {object} velocity    the constant velocity
 */
function Projectile(x, y, velocity) {
  this.x = x;
  this.y = y;
  this.velocity = velocity;
  this.size = 10;
}

Projectile.prototype.move = function() {
  this.x += this.velocity.x;
  this.y += this.velocity.y;
}

Projectile.prototype.draw = function() {
  fill(230, 186, 115);
  ellipse(this.x, this.y, this.size, this.size);
}


const drawScore = () => {
  fill(255);
  textAlign(CENTER, CENTER);
  text(score, 200, 200);
};

const drawCircleBorder = () => {
  noFill();
  stroke(255);
  strokeWeight(2);
  ellipse(circleBorder.x, circleBorder.y, circleBorder.radius*2, circleBorder.radius*2);
  noStroke();
};

const emitter = new AsteroidEmitter(200, 200, 50);
const character = new Character(circleBorder, {x: 200, y: 200});


function mouseClicked() {
  character.emitProjectile();
}

function keyPressed() {
  if (keyCode === 32) {
    character.emitProjectile();
  }
}

function draw() {
  background(57, 8, 89);

  if (gameOver) {
    textAlign(CENTER, CENTER);
    textSize(100);
    fill(255);
    text('GAME\nOVER', 200, 200);
    return;
  }
  score++;

  emitter.draw();
  drawScore();
  drawCircleBorder();
  if (asteroids.length < 5) {
    emitter.emitAsteroid();
  }

  asteroids.forEach(asteroid => {
    asteroid.draw();
    asteroid.move();
    if (asteroid.isBorderCollide()) {
      gameOver = true;
    }
  });

  projectiles.forEach((projectile, pIdx) => {
    projectile.move();
    projectile.draw();
    asteroids.forEach((asteroid, aIdx) => {
      if (isCollide(projectile, asteroid)) {

        asteroids.splice(aIdx, 1);
        projectiles.splice(pIdx, 1);
      }
    });
    
  });

  character.draw();
  character.updatePosition(mouseX, mouseY);

}
