import modules.pieceClass
import re

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
            if isinstance(piece, modules.pieceClass.King):
                if piece.colour == "white":
                    whiteKingAlive = True
                else:
                    blackKingAlive = True

    return [whiteKingAlive, blackKingAlive]
