class Cell:
    def __init__(self, stat):
        self.stat = stat

    def status(self):
        return self.stat


class Checkers:
    def __init__(self):
        self.field = {}

        for row in "87654321":
            for line in "ABCDEFGH":

                if (row in "13" and line in "ACEG") or (row == '2' and line in "BDFH"):
                    self.field[line + row] = 'W'    
                elif (row in "68" and line in "BDFH") or (row == '7' and line in "ACEG"):
                    self.field[line + row] = 'B'
                else:
                    self.field[line + row] = 'X'

    def get_cell(self, p):
        return Cell(self.field[p])

    def move(self, f, t):
        self.field[t], self.field[f] = self.field[f], 'X'

    def field(self):
        return self.field
