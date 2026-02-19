class Board:
    def __init__(self, size=5):
        self.size = size

    def in_bounds(self, pos):
        x, y = pos
        return 0 <= x < self.size and 0 <= y < self.size

    def print_board(self, rat, cat):
        for i in range(self.size):
            row = ""
            for j in range(self.size):
                if (i, j) == rat:
                    row += "R "
                elif (i, j) == cat:
                    row += "C "
                else:
                    row += ". "
            print(row)
        print()
