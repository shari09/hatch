import numpy as np
class connectFour:
  def __init__(self):
    self.board = np.zeros((6,7))
    #assign a number between 1 and -1 for each player but not zero
    self.playerOne = 1
    self.playerTwo = -1
  #count the number of moves
  def moveCount(self):
    count = 0
    for c in range(7):
      for r in range(6):
        if (self.board[r][c] != 0):
          count += 1
    return count
  #check if a player has won
  def hasWon(self, player):
    #Check horizontal locations
    for c in range(4):
      for r in range(6):
        if self.board[r][c] == self.board[r][c+1] == self.board[r][c+2] == self.board[r][c+3] == player:
          return player
    #Check vertical locations
    for c in range(7):
      for r in range(3):
        if self.board[r][c] == self.board[r+1][c] == self.board[r+2][c] == self.board[r+3][c] == player:
          return player
    #Check positively sloped diagonal locations
    for c in range(4):
      for r in range(3):
        if self.board[r][c] == self.board[r+1][c+1] == self.board[r+2][c+2] == self.board[r+3][c+3] == player:
          return player
    #Check negatively sloped diagonal locations
    for c in range(4):
      for r in range(3, 6):
        if self.board[r][c] == self.board[r-1][c+1] == self.board[r-2][c+2] == self.board[r-3][c+3] == player:
          return player
    #if it's a tie return 0.5
    if (self.moveCount() == 42):
      return 0.5
    else:
      return 0
  #this function allows players to drop a tile
  def dropTile(self, columnNum, player):
    val = -1
    for rowNum in range(5, -1, -1):
      if (self.board[rowNum][columnNum] == 0):
        self.board[rowNum][columnNum] = player
        val = 1
        break
    self.render()
    return val
  #return number of possible states, in this case 6 x 7 becouse of the board size
  def stateSize(self):
    return 42
  #return number of possible actions, in this case 7 becouse their are 7 columns
  def actionSize(self):
    return 7
  #resets the board
  def reset(self):
    self.board = np.zeros((6,7))
  #draws the board to the screen
  def render(self):
    print(self.board)
    print("\n")
  #sets the board
  def set(self, newBoard):
    self.board = newBoard


def validMove(game, col, player):

  if 1 <= col <= 7 \
    and game.dropTile(col - 1, player) != -1:
    return False
  else:
    print("Invalid move")
    return True

def main():
  inGame = True
  game = connectFour()
  playerA = True
  invalidMove = True

  #game loop
  while (inGame):

    while invalidMove:
      if playerA:
        col = int(input("Player A: "))
        invalidMove = validMove(game, col, game.playerOne)
      else:
        col = int(input("Player B: "))
        invalidMove = validMove(game, col, game.playerTwo)

    invalidMove = True
    if game.hasWon(game.playerOne) == 1:
      print("Player A has won")
      inGame = False
    elif game.hasWon(game.playerTwo) == 1:
      print("Player B has won")
      inGame = False
    elif game.hasWon(game.playerOne) == 0.5:
      print("Tie")
      inGame = False
    
    playerA = not playerA

if __name__ == "__main__":
  print("Welcome to connect 4")
  play = True
  while play:
    main()
    playAgain = input("Do you wish to play again (Y/n): ")
    if playAgain[0].lower() == 'n':
      play = False
