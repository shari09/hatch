from modules.empty import *
from modules.functions import *

invalidMsg = "Invalid move"

displayPieces = {
    "black" : {
            "pawn" : "♙",
            "rook" : "♖",
            "knight" : "♘",
            "bishop" : "♗",
            "king" : "♔",
            "queen" : "♕"
    },
    "white" : {
            "pawn" : "♟",
            "rook" : "♜",
            "knight" : "♞",
            "bishop" : "♝",
            "king" : "♚",
            "queen" : "♛"
    }
}

class Piece:
    def __init__(self, pos, colour, value, pGameBoard):
        self.y = pos[0]
        self.x = int(pos[1])
        self.value = value
        self.colour = colour
        self.moved = False
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
        self.moved = True
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
        #return False

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
