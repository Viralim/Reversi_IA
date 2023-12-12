import math
import Reversi
from Reversi import Board
import random

def MinMax(board, depth, maximizing_player):
    if depth == 0 or board.is_game_over():
        return board.heuristique(), None

    best_score = -math.inf if maximizing_player else math.inf
    best_move = None

    for move in board.legal_moves():
        player, x, y = move
        board.push(move)
        score, _ = MinMax(board, depth - 1, not maximizing_player)
        board.pop()

        if maximizing_player and score > best_score:
            best_score = score
            best_move = move
        elif not maximizing_player and score < best_score:
            best_score = score
            best_move = move

    return best_score, best_move

# Function to play Reversi on a 10x10 board
def play_reversi():
    board = Reversi.Board(boardsize=10)
    depth = 4  # You can adjust the depth based on your desired level of difficulty

    while not board.is_game_over():
        print(board)
        if board._nextPlayer == Reversi.Board._BLACK:
            print("Tour de la pièce noire (X)")
        else:
            print("Tour de la pièce blanche (O)")

        if board._nextPlayer == Reversi.Board._BLACK:
            _, best_move = MinMax(board, depth, maximizing_player=True)
        else:
            _, best_move = MinMax(board, depth, maximizing_player=False)

        if best_move:
            print("Coup choisi:", best_move)
            board.push(best_move)
        else:
            print("Passe son tour")
            board.push([board._nextPlayer, -1, -1])

    print("Game Over")
    print("Plateau final:")
    print(board)
    print("Résultat:")
    nb_pieces = board.get_nb_pieces()
    print(f"Noir (X): {nb_pieces[1]} pièces")
    print(f"Blanc (O): {nb_pieces[0]} pièces")

# main program:
if __name__ == "__main__":
    initial_board = Reversi.Board()
    play_reversi()

    # Call MinMax to find the best move
    best_score, best_move = MinMax(initial_board, depth=3, maximizing_player=True)

    print("Meilleur score:", best_score)
    print("Meilleur coup:", best_move)