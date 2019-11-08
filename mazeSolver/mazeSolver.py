def isValid(maze, row, col, path, pastDir, currentDir):
  if (0 < row < len(maze)
        and 0 < col < len(maze[0])
        and maze[row][col] != '#'
        and currentDir != -pastDir
        and [row, col] not in path):
      return True
  return False

def nextSpace(maze, row, col, endRow, endCol, path, step, pastDir, currentDir):
  if isValid(maze, row, col, path, pastDir, currentDir):
    path.append([row, col])
    findPath(maze, row, col, endRow, endCol, path, step+1, currentDir)
    path.pop()

def findPath(maze, row, col, endRow, endCol, path, step, direction):
  if row == endRow and col == endCol:
    displayPath(maze, path)

  nextSpace(maze, row+1, col, endRow, endCol, path, step, direction, 1)
  nextSpace(maze, row-1, col, endRow, endCol, path, step, direction, -1)
  nextSpace(maze, row, col+1, endRow, endCol, path, step, direction, 2)
  nextSpace(maze, row, col-1, endRow, endCol, path, step, direction, -2)

def display(maze):
  for row in maze:
    for col in row:
      print(col, end=' ')
    print()

def displayPath(maze, path):
  for pos in path:
    if maze[pos[0]][pos[1]] == ' ':
      maze[pos[0]][pos[1]] = '.'
  display(maze)

def readFile(filename):
  maze = []
  rowNum = 0
  colNum = 0
  endRowNum = 0
  endColNum = 0
  mazeFile = open(filename, 'r')
  for line in mazeFile:
    row = []
    for char in line:
      if char != '\n':
        row.append(char)
        #finding starting and ending positions
        if char == 'S':
          rowNum = len(maze)
          colNum = len(row)-1
        elif char == 'F':
          endRowNum = len(maze)
          endColNum = len(row)-1
    maze.append(row)
  return [maze, rowNum, colNum, endRowNum, endColNum]

def main():
  #reading the maze file and converting it to 2d list
  [maze, row, col, endRow, endCol] = readFile('maze.txt')
  path = []
  findPath(maze, row, col, endRow, endCol, path, 0, 0)

if __name__ == '__main__':
  main()
