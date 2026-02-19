def evaluate(rat, cat):
    # Distancia Manhattan entre ratón y gato
    return abs(rat[0]-cat[0]) + abs(rat[1]-cat[1])

def minimax(rat, cat, depth, is_rat_turn, board):
    if depth == 0 or rat == cat:
        return evaluate(rat, cat)

    if is_rat_turn:
        best_value = float('-inf')
        moves = [(0,1),(0,-1),(1,0),(-1,0)]
        for dx, dy in moves:
            new_pos = (rat[0]+dx, rat[1]+dy)
            if board.in_bounds(new_pos):
                value = minimax(new_pos, cat, depth-1, False, board)
                best_value = max(best_value, value)
        return best_value
    else:
        best_value = float('inf')
        moves = [(0,1),(0,-1),(1,0),(-1,0)]
        for dx, dy in moves:
            new_pos = (cat[0]+dx, cat[1]+dy)
            if board.in_bounds(new_pos):
                value = minimax(rat, new_pos, depth-1, True, board)
                best_value = min(best_value, value)
        return best_value
