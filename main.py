from board import Board
from agents import Rat, Cat
from minimax import minimax

def game_loop():
    board = Board(size=5)
    rat = Rat((0,0))
    cat = Cat((4,4))
    turns = 0

    while rat.pos != cat.pos and turns < 20:
        print(f"Turno {turns}")
        board.print_board(rat.pos, cat.pos)

        # Movimiento del ratón (aleatorio al inicio)
        rat.random_move(board)

        # Movimiento del gato usando minimax
        best_move = None
        best_value = float('inf')
        for move in cat.possible_moves(board):
            value = minimax(rat.pos, move, 3, True, board)
            if value < best_value:
                best_value = value
                best_move = move
        cat.pos = best_move

        turns += 1

    board.print_board(rat.pos, cat.pos)
    if rat.pos == cat.pos:
        print("El gato atrapó al ratón 🐱🧀")
    else:
        print("El ratón escapó tras 20 turnos 🐭✨")

if __name__ == "__main__":
    print("Iniciando juego...")

    game_loop()
