`Molecule` (pass in: xPos, yPos, targetX, targetY):
  Set `this.xPos` to xPos
  Set `this.yPos` to yPos
  Set `this.size` to 4
  Set `this.targetX` to targetX
  Set `this.targetY` to targetY
  
  Set `this.display` to a function:
    Set stroke colour to black
    Set stroke weight to 1
    Set fill to gray
    Draw an ellipse at (this.xPos, this.yPos, this.size, this.size)

  Set `this.move` to a function:
    If the targetX is bigger than the xPos, increase the xPos, otherwise decrease the xPos
    If the targetY is bigger than the yPos, increase the yPos, otherwise decrease the yPos

  Set `this.end` to a function:
    If this.move() continues moving and it goes past the target:
      return true
    otherwise:
      return false

Create an array called `molecules`

Create a function called `generateMolecules`(pass in: no args):
  Reset `molecules` to an empty array
  Set `num` to a random number from 20 to 70
  Set `gap` to the size of the canvas divided by the square root of `num`
  for every gap along the x-axis:
    for every gap along the y-axis:
      push a new `Molecule` to `molecules` with a random x and y position

Create a function called `displayMolecules`(pass in: no args):
  for every molecule in `molecules`:
    call the display function fo the molecule
    call the move function of the molecule


Create the `draw` function():
  Change the background to (220)
  Call the `displayMolecules` function
  ```javascript
    if (molecules.every(function(molecule) {
      return molecule.end()
    }));
  ```
  if every molecule in `molecules` are .end():
    Call the `generateMolecules` function