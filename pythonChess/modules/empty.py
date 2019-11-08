def emptySpace(pGameBoard, y, x):
    if pGameBoard.board[y][x] == 0:
        return True
    return False

def validKingMove(pYIndex, y1, x1, y2, x2):
    initYIndex = pYIndex.index(y1)
    newYIndex = pYIndex.index(y2)

    if abs(initYIndex - newYIndex) == 1 or abs(x1 - x2) == 1:
        return True

def validKnightMove(pYIndex, y1, x1, y2, x2):
    initYIndex = pYIndex.index(y1)
    newYIndex = pYIndex.index(y2)

    if abs(initYIndex - newYIndex) == 2 and abs(x1 - x2) == 1 or\
        abs(x1 - x2) == 2 and abs(initYIndex - newYIndex) == 1:
        return True



def validEmptyDiagonal(pGameBoard, pYIndex, y1, x1, y2, x2):

    initYIndex = pYIndex.index(y1)
    newYIndex = pYIndex.index(y2)

    if abs(initYIndex - newYIndex) == abs(x1 - x2) and x1 != x2:
        stepX = -1 if x1 > x2 else 1
        stepY = -1 if initYIndex > newYIndex else 1

        initYIndex += stepY
        newYIndex += stepY
        x1 += stepX
        x2 += stepX

        while x1 != x2:
            if not emptySpace(pGameBoard, pYIndex[initYIndex], x1):
                return False
            x1 += stepX
            initYIndex += stepY
        return True


def validEmptyLine(pGameBoard, pYIndex, y1, x1, y2, x2):
    initYIndex = pYIndex.index(y1)
    newYIndex = pYIndex.index(y2)

    #negative depending on which direction it is
    stepX = -1 if x1 > x2 else 1
    stepY = -1 if initYIndex > newYIndex else 1

    if y1 == y2:
        for i in range(x1 + stepX, x2 + stepX, stepX):
            if not emptySpace(pGameBoard, y1, i):
                return False
        return True
    elif x1 == x2:
        for i in range(initYIndex + stepY, newYIndex + stepY, stepY):
            if not emptySpace(pGameBoard, pYIndex[i], x1):
                return False
        return True

    return False #not in a line


#returns the [y, x] of the rook that is being castled
def validCastleMove(pGameBoard, pYIndex, y1, x1, y2, x2):
    dir = "right" if x2 > x1 else "left"

    if y1 == y2 and abs(x1 - x2) == 2:
        if dir == "right":
            if validEmptyLine(pGameBoard, pYIndex, y1, x1, y2, x2):
                return [y2, x2 + 1]
        else:
            if validEmptyLine(pGameBoard, pYIndex, y1, x1, y2, x2 - 1):
                return [y2, x2 - 2]

    return [None, None]
