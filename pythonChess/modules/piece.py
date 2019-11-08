from modules.pieceClass import *


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
        "H2", "H7")

    blackBishops = makePiece(pGameBoard, "black", Bishop,
        displayPieces["black"]["bishop"],
        "A2", "A7")

    whiteKnights = makePiece(pGameBoard, "white", Knight,
        displayPieces["white"]["knight"],
        "H3", "H6")

    blackKnights = makePiece(pGameBoard, "black", Knight,
        displayPieces["black"]["knight"],
        "A3", "A6")

    whiteQueens = makePiece(pGameBoard, "white", Queen,
        displayPieces["white"]["queen"], "H4")

    blackQueens = makePiece(pGameBoard, "black", Queen,
        displayPieces["black"]["queen"], "A4")

    whiteKing = makePiece(pGameBoard, "white", King,
        displayPieces["white"]["king"], "H5")

    blackKing = makePiece(pGameBoard, "black", King,
        displayPieces["black"]["king"], "A5")

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
