##########
##Sep 16, 2019 - Sep 20, 2019
###By MEEEEEE :DDDD - Shari
######
##Enter coordinates
##Ex. if you want to move the piece at G2 to E2
##you input "G2 E2" with one space in between
################################
from modules import *


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
if __name__ == "__main__":
    main()
