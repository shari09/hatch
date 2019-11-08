def isValid(board, row, col):
  for i in range(len(board)):
    for j in range(len(board)):
      if board[i][j] == 1:
        if i == row or j == col or abs(row-i) == abs(col-j):
          return False
  return True

def display(board):
  for row in board:
    for col in row:
      print(col, end=' ')
    print()
  print()

def solve(board, row, col, n):
  if n == 0:
    display(board)
    return 1
  if col == len(board):
    return 0

  numSolutions = 0
  for i in range(len(board)):
    if isValid(board, row, i):
      board[row][i] = 1
      numSolutions += solve(board, row+1, 0, n-1)
      board[row][i] = 0
  return numSolutions

def main():
  
  size = int(input('Size of the board: '))

  board = [[]] * size
  for i in range(size):
    board[i] = [0] * size

  numSolutions = solve(board, 0, 0, size)
  print('Number of solutions:', numSolutions)

if __name__ == '__main__':
  main()

  