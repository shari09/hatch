def isValid(board, row, col):
  for i in range(len(board)):
    for j in range(len(board)):
      if board[i][j] == 1:
        if i == row or j == col or abs(row-i) == abs(col-i):
          return False
  return True

def display(board):
  for row in board:
    for col in row:
      print(col, end=' ')
    print()

def solve(board, row, col):
  

def main():
  
  size = int(input('Size of the board: '))

  board = [[]] * size
  for i in range(size):
    board[i] = [0] * size

  display(board)

if __name__ == '__main__':
  main()

  