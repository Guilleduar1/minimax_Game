import random

class Rat:
    def __init__(self, pos):
        self.pos = pos

    def random_move(self, board):
        moves = [(0,1),(0,-1),(1,0),(-1,0)]
        dx, dy = random.choice(moves)
        new_pos = (self.pos[0]+dx, self.pos[1]+dy)
        if board.in_bounds(new_pos):
            self.pos = new_pos

class Cat:
    def __init__(self, pos):
        self.pos = pos

    def possible_moves(self, board):
        moves = [(0,1),(0,-1),(1,0),(-1,0)]
        valid = []
        for dx, dy in moves:
            new_pos = (self.pos[0]+dx, self.pos[1]+dy)
            if board.in_bounds(new_pos):
                valid.append(new_pos)
        return valid
