import turtle
import random
chessboard = turtle.Turtle()
chessboard.speed(0)
screen = turtle.Screen()
turtle.tracer(0, 0)

XSHIFT = -400
YSHIFT = 400


whiteImagesUrl = ["whitePawn.gif",
                  "whiteRook.gif",
                  "whiteKnight.gif",
                  "whiteBishop.gif",
                  "whiteKing.gif",
                  "whiteQueen.gif"]
whiteImages = []

blackImagesUrl = ["blackPawn.gif",
                  "blackRook.gif",
                  "blackKnight.gif",
                  "blackBishop.gif",
                  "blackKing.gif",
                  "blackQueen.gif"]

blackImages = []

for i in whiteImagesUrl:
    screen.register_shape(i);
    whiteImages.append(turtle.Turtle(shape=i))

for i in blackImagesUrl:
    screen.register_shape(i);
    blackImages.append(turtle.Turtle(shape=i))

def drawPieces(self):
    for k, row in self.board.items():
        if k != '""':
            y = ord(k)-65
            for x in range(len(row)-1):
                col = row[1:][x]
                if 0 < col < 7:
                    whiteImages[col-1].goto(50+(100*x) + XSHIFT, -40-(100*y) + YSHIFT)
                    whiteImages[col-1].stamp()
                elif col > 6:
                    blackImages[col%6-1].goto(50+(100*x) + XSHIFT, -40-(100*y) + YSHIFT)
                    blackImages[col%6-1].stamp()




def resetBoard():
    chessboard.reset()

    for i in range(4):
        chessboard.penup()
        chessboard.goto(XSHIFT, YSHIFT)
        chessboard.forward(800)
        chessboard.right(90)

    brown = True
    for i in range(8):
        brown = not brown

        for j in range(8):

            chessboard.penup()
            chessboard.goto(j*100 + XSHIFT, i*-100 + YSHIFT)
            if brown:
                chessboard.fillcolor("brown")
            else:
                chessboard.fillcolor("tan")
            brown = not brown
            chessboard.begin_fill()
            for k in range(4):
                chessboard.forward(100)
                chessboard.right(90)
            chessboard.end_fill()

    turtle.update()


class Board:
    def __init__(self, pYIndex):
        self.board = {}
        self.new(pYIndex)

    def new(self, pYIndex):
        firstY = '""'

        for y in range(9):
            self.board[pYIndex[y]] = []
            for x in range(9):
                if y == 0:
                    self.board[pYIndex[y]].append(str(x))
                else:
                    self.board[pYIndex[y]].append(0)
        self.board[firstY].pop(0)
        self.board[firstY] = ", ".join(self.board[firstY])


    def display(self):
        resetBoard()
        drawPieces(self)




#######################################3
invalidMsg = "Invalid move"


class Piece:
    def __init__(self, pos, colour, value, pGameBoard):
        self.y = pos[0]
        self.x = int(pos[1])
        self.value = value
        self.colour = colour
        self.update(pGameBoard)

    def update(self, pGameBoard):
        pGameBoard.board[self.y][self.x] = self.value

    def eatPiece(self, pGameBoard, pAllPieces, pYIndex, newPos):
        if self.ediblePiece(pGameBoard, pAllPieces, pYIndex, newPos):
            [y, x] = convertPos(newPos)
            [i, piece] = findPiece(pAllPieces, newPos)
            pAllPieces[i].pop(piece)

            pGameBoard.board[self.y][self.x] = 0
            self.y = y
            self.x = x
            self.update(pGameBoard)
            return True

    def moveAround(self, pGameBoard, pYIndex, newPos):
        [y, x] = convertPos(newPos)

        if self.validEmptyMove(pGameBoard, pYIndex, newPos):
            pGameBoard.board[self.y][self.x] = 0
            self.y = y
            self.x = x
            self.update(pGameBoard)

            return True

    def configSpace(self, pGameBoard, pAllPieces, pYIndex, newPos): ######FOR STRAIGHT/DIAGONAL LINES
        [y, x] = convertPos(newPos)
        initYIndex = pYIndex.index(self.y)
        newYIndex = pYIndex.index(y)

        if not emptySpace(pGameBoard, y, x):
            stepX = 0
            stepY = 0
            if self.x < x:
                stepX = -1
            elif self.x > x:
                stepX = 1

            if initYIndex < newYIndex:
                stepY = -1
            elif initYIndex > newYIndex:
                stepY = 1

            x = x + stepX
            y = pYIndex[newYIndex + stepY]

            [i, piece] = findPiece(pAllPieces, newPos)
            if pAllPieces[i][piece].colour != self.colour:
                return [y, x]
        return [None, None]

    def move(self, pGameBoard, pAllPieces, pYIndex, newPos):
        if not self.moveAround(pGameBoard, pYIndex, newPos) and \
        not self.eatPiece(pGameBoard, pAllPieces, pYIndex, newPos):
            print(invalidMsg)
            return False
        return True #returns whether it moved or not



class Rook(Piece):


    def validEmptyMove(self, pGameBoard, pYIndex, newPos):
        [y, x] = convertPos(newPos)
        initYIndex = pYIndex.index(self.y)
        newYIndex = pYIndex.index(y)
        if validEmptyLine(pGameBoard, pYIndex, self.y, self.x, y, x):
            return True

    def ediblePiece(self, pGameBoard, pAllPieces, pYIndex, newPos):
        [y, x] = self.configSpace(pGameBoard, pAllPieces, pYIndex, newPos)
        if x != None:
            if validEmptyLine(pGameBoard, pYIndex, self.y, self.x, y, x):
                return True

class Bishop(Piece):

    def validEmptyMove(self, pGameBoard, pYIndex, newPos):
        [y, x] = convertPos(newPos)
        if emptySpace(pGameBoard, y, x):
            if validEmptyDiagonal(pGameBoard, pYIndex, self.y, self.x, y, x):
                return True

    def ediblePiece(self, pGameBoard, pAllPieces, pYIndex, newPos):
        initYIndex = pYIndex.index(self.y)
        newYIndex = pYIndex.index(newPos[0])

        [y, x] = self.configSpace(pGameBoard, pAllPieces, pYIndex, newPos)
        if x != None:
            if validEmptyDiagonal(pGameBoard, pYIndex, self.y, self.x, y, x):
                return True
            elif y == self.y and x == self.x and \
                abs(newYIndex - initYIndex) == 1 and \
                abs(self.x - int(newPos[1])) == 1:
                return True

class Knight(Piece):

    def validEmptyMove(self, pGameBoard, pYIndex, newPos):
        [y, x] = convertPos(newPos)
        if emptySpace(pGameBoard, y, x):
            if validKnightMove(pYIndex, self.y, self.x, y, x):
                return True

    def ediblePiece(self, pGameBoard, pAllPieces, pYIndex, newPos):
        [y, x] = convertPos(newPos)
        if not emptySpace(pGameBoard, y, x):
            if validKnightMove(pYIndex, self.y, self.x, y, x):
                [i, piece] = findPiece(pAllPieces, newPos)
                if pAllPieces[i][piece].colour != self.colour:
                    return True

class Queen(Piece):

    def validEmptyMove(self, pGameBoard, pYIndex, newPos):
        [y, x] = convertPos(newPos)
        if validEmptyLine(pGameBoard, pYIndex, self.y, self.x, y, x) or\
            validEmptyDiagonal(pGameBoard, pYIndex, self.y, self.x, y, x):
            return True

    def ediblePiece(self, pGameBoard, pAllPieces, pYIndex, newPos):
        [y, x] = self.configSpace(pGameBoard, pAllPieces, pYIndex, newPos)
        if x != None:
            if validEmptyLine(pGameBoard, pYIndex, self.y, self.x, y, x) or\
                validEmptyDiagonal(pGameBoard, pYIndex, self.y, self.x, y, x):
                return True


class King(Piece):

    def validEmptyMove(self, pGameBoard, pYIndex, newPos):
        [y, x] = convertPos(newPos)
        if emptySpace(pGameBoard, y, x):
            if validKingMove(pYIndex, self.y, self.x, y, x):
                return True

    def ediblePiece(self, pGameBoard, pAllPieces, pYIndex, newPos):
        [y, x] = convertPos(newPos)
        if not emptySpace(pGameBoard, y, x):
            if validKingMove(pYIndex, self.y, self.x, y, x):
                [i, piece] = findPiece(pAllPieces, newPos)
                if pAllPieces[i][piece].colour != self.colour:
                    return True

    def allowCastle(self, pGameBoard, pAllPieces, pYIndex, newPos):
        [y, x] = convertPos(newPos)
        [rookY, rookX] = validCastleMove(pGameBoard, pYIndex, self.y, self.x, y, x)
        if rookY != None:
            [i, piece] = findPiece(pAllPieces, rookY + str(rookX))
            if not self.moved and not pAllPieces[i][piece].moved:
                return [True, i, piece]

        return[None, None, None]


    def castle(self, pGameBoard,  pAllPieces, pYIndex, newPos):

        [allowedCastle, i, piece] = self.allowCastle(pGameBoard, pAllPieces, pYIndex, newPos)
        if allowedCastle:

            [y, x] = convertPos(newPos)

            pGameBoard.board[self.y][self.x] = 0
            self.x = x
            self.update(pGameBoard)

            rook = pAllPieces[i][piece]
            pGameBoard.board[rook.y][rook.x] = 0

            rook.x = rook.x + 3 if rook.x < self.x else rook.x - 2
            rook.update(pGameBoard)

            return True

    def move(self, pGameBoard, pAllPieces, pYIndex, newPos):
        if not self.moveAround(pGameBoard, pYIndex, newPos) and \
        not self.eatPiece(pGameBoard, pAllPieces, pYIndex, newPos) and \
        not self.castle(pGameBoard, pAllPieces, pYIndex, newPos):
            print(invalidMsg)
            return False

        return True #returns whether it moved or not


class Pawn(Piece): #add the changePiece method later

    def validEmptyMove(self, pGameBoard, pYIndex, newPos):
        [y, x] = convertPos(newPos)

        if emptySpace(pGameBoard, y, x):
            firstBlack = self.y == "B" and self.colour == "black"
            firstWhite = self.y == "G" and self.colour == "white"
            allowedSpace = [1, 2] if firstBlack or firstWhite else [1] #move two spaces on first move


            for i in allowedSpace:
                if self.colour == "white":
                    if pYIndex.index(self.y) - pYIndex.index(y) == i and x == self.x:
                        return True
                else:
                    if pYIndex.index(y) - pYIndex.index(self.y) == i and x == self.x:
                        return True
        return False

    def ediblePiece(self, pGameBoard, pAllPieces, pYIndex, newPos):
        [y, x] = convertPos(newPos)
        if not emptySpace(pGameBoard, y, x):
            if abs(self.x - x) == 1:
                [i, piece] = findPiece(pAllPieces, newPos)
                if self.colour == "white" and \
                    pYIndex.index(self.y) - pYIndex.index(y) == 1 and \
                    pAllPieces[i][piece].colour != "white":
                    return True
                elif self.colour == "black" and \
                    pYIndex.index(y) - pYIndex.index(self.y) == 1 and \
                    pAllPieces[i][piece].colour != "black":
                    return True

    def changePieceValid(self):
        if self.colour == "white" and self.y == "A":
            return True
        elif self.colour == "black" and self.y == "H":
            return True

    def changePiece(self, pGameBoard, pAllPieces):
        if self.changePieceValid():
            newPiece = input("Enter your new piece: ").lower()

            while newPiece not in pawnChangeList:
                print("Invalid piece")
                newPiece = input("Enter your new piece: ").lower()

            pos = self.y + str(self.x)
            [i, piece] = findPiece(pAllPieces, pos)
            pAllPieces[i][piece] = pawnChangeList[newPiece][0](
                pos,
                self.colour,
                displayPieces[self.colour][newPiece],
                pGameBoard
            )

    def move(self, pGameBoard, pAllPieces, pYIndex, newPos):
        if not self.moveAround(pGameBoard, pYIndex, newPos) and \
        not self.eatPiece(pGameBoard, pAllPieces, pYIndex, newPos):
            print(invalidMsg)
            return False

        self.changePiece(pGameBoard, pAllPieces)
        return True #returns whether it moved or not

pawnChangeList = {
    "rook" : [Rook, 2],
    "queen" : [Queen, 5],
    "knight" : [Knight, 4],
    "bishop" : [Bishop, 3]
}




########################
displayPieces = {
    "black" : {
            "pawn" : 1,
            "rook" : 2,
            "knight" : 3,
            "bishop" : 4,
            "king" : 5,
            "queen" : 6
    },
    "white" : {
            "pawn" : 7,
            "rook" : 8,
            "knight" : 9,
            "bishop" : 10,
            "king" : 11,
            "queen" : 12
    }
}


def makePiece(pGameBoard, colour, piece, val, *pos):
    pieceList = []
    for i in range(len(pos)):
        pieceList.append(piece(pos[i], colour, val, pGameBoard))

    return pieceList


def generatePieces(pGameBoard):
    whitePawns = makePiece(pGameBoard, "white", Pawn,
        displayPieces["white"]["pawn"],
        "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8")

    blackPawns = makePiece(pGameBoard, "black", Pawn,
        displayPieces["black"]["pawn"],
        "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8")

    whiteRooks = makePiece(pGameBoard, "white", Rook,
        displayPieces["white"]["rook"],
        "H1", "H8")

    blackRooks = makePiece(pGameBoard, "black", Rook,
        displayPieces["black"]["rook"],
        "A1", "A8")

    whiteBishops = makePiece(pGameBoard, "white", Bishop,
        displayPieces["white"]["bishop"],
        "H3", "H6")

    blackBishops = makePiece(pGameBoard, "black", Bishop,
        displayPieces["black"]["bishop"],
        "A3", "A6")

    whiteKnights = makePiece(pGameBoard, "white", Knight,
        displayPieces["white"]["knight"],
        "H2", "H7")

    blackKnights = makePiece(pGameBoard, "black", Knight,
        displayPieces["black"]["knight"],
        "A2", "A7")

    whiteQueens = makePiece(pGameBoard, "white", Queen,
        displayPieces["white"]["queen"], "H5")

    blackQueens = makePiece(pGameBoard, "black", Queen,
        displayPieces["black"]["queen"], "A5")

    whiteKing = makePiece(pGameBoard, "white", King,
        displayPieces["white"]["king"], "H4")

    blackKing = makePiece(pGameBoard, "black", King,
        displayPieces["black"]["king"], "A4")

    changedPawns = []

    pieces = [
        whitePawns,
        blackPawns,
        whiteRooks,
        blackRooks,
        whiteBishops,
        blackBishops,
        whiteKnights,
        blackKnights,
        whiteQueens,
        blackQueens,
        whiteKing,
        blackKing
    ]

    return pieces

###################

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


#####################
def convertPos(pos):
    y = pos[0]
    x = int(pos[1])
    return [y, x]


def findPiece(pAllPieces, pos):
    y = pos[0]
    x = int(pos[1])
    for i in range(len(pAllPieces)):
        pieceType = pAllPieces[i]
        for piece in range(len(pieceType)):
            if pieceType[piece].y == y and \
            pieceType[piece].x == x:
                return [i, piece]
    return [None, None]

def correctTurn(pAllPieces, initPos, pTurn, cTurn):
    [i, piece] = findPiece(pAllPieces, initPos)
    if pAllPieces[i][piece].colour == cTurn:
        return True


def askForMove(pGameBoard, pAllPieces, pYIndex, pTurn, cTurn):
    error = True

    while error:
        userInput = input("Enter your move (ex. G3 E3): \n")
        if (len(userInput) == 5) and \
            (userInput[0] in pYIndex) and (userInput[3] in pYIndex) and \
            (0 < int(userInput[1]) < 9) and (0 < int(userInput[4]) < 9):
            error = False
        else:
            print("Invalid input")

    initPos = userInput[:2]
    endPos = userInput[3:]

    [i, piece] = findPiece(pAllPieces, initPos)

    if i != None:

        if correctTurn(pAllPieces, initPos, pTurn, cTurn):
            if pAllPieces[i][piece].move(pGameBoard, pAllPieces, pYIndex, endPos):
                [pTurn, cTurn] = [cTurn, pTurn]
        else:
            print("It's not your turn!")
    else:
        print("There's no piece there!")

    return [pTurn, cTurn]


def checkWin(pAllPieces):
    whiteKingAlive = False
    blackKingAlive = False
    for pieceType in pAllPieces:
        for piece in pieceType:
            if isinstance(piece, King):
                if piece.colour == "white":
                    whiteKingAlive = True
                else:
                    blackKingAlive = True

    return [whiteKingAlive, blackKingAlive]


#####################
def main():
    yIndex = '"" A B C D E F G H'.split()
    gameBoard = Board(yIndex)
    pTurn = "black"
    cTurn = "white"
    gameOver = False

    whiteAlive = True
    blackAlive = True

    allPieces = generatePieces(gameBoard)

    while not gameOver:
        gameBoard.display()
        [pTurn, cTurn] = askForMove(gameBoard, allPieces, yIndex, pTurn, cTurn)
        [whiteAlive, blackAlive] = checkWin(allPieces)
        if not whiteAlive:
            gameOver = True
            print("Black Won")
        elif not blackAlive:
            print("White Won")
            gameOver = True


#############################
############
###################

main()
