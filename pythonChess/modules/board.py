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
        for k, v in self.board.items():
            if k == '""':
                print(k, v)
            else:
                newV = v[1 : len(v) + 1]
                print(k, '[%s]' % '  '.join(map(str, newV)))
