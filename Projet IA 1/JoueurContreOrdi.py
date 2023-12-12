from Reversi import Board
import random

def print_board(board):
    for row in range(board.get_board_size()):
        for col in range(board.get_board_size()):
            piece = board._board[row][col]
            if piece == board._BLACK:
                print('X', end=' ')
            elif piece == board._WHITE:
                print('O', end=' ')
            else:
                print('.', end=' ')
        print()

def player_move(board):
    while True:
        try:
            print_board(board)
            print("Coups possibles pour le joueur :")
            print(all_possible_moves(board))
            x = int(input("Entrez la coordonnée x : "))
            y = int(input("Entrez la coordonnée y : "))
            
            if board.is_valid_move(board._nextPlayer, x, y):
                return [board._nextPlayer, x, y]
            else:
                print("Mouvement invalide, rééssayez :")
                
        except ValueError:
            print("Veuillez entrer des coordonnées valides")

def all_possible_moves(board):
    possible_moves = []

    for x in range(board._boardsize):
        for y in range(board._boardsize):
            if board.lazyTest_ValidMove(board._nextPlayer, x, y):
                possible_moves.append([board._nextPlayer, x, y])

    if not possible_moves:
        possible_moves = [[board._nextPlayer, -1, -1]]  # We shall pass

    return possible_moves

def main():
    board = Board()

    while not board.is_game_over():
        print_board(board)

        if board._nextPlayer == board._BLACK:
            move = player_move(board)
        else:
            print("L'ordinateur joue...")
            # Utilisez la fonction all_possible_moves pour obtenir les coups possibles pour l'ordinateur
            moves = all_possible_moves(board)

            # Choisissez aléatoirement un mouvement parmi les coups possibles pour l'ordinateur
            move = random.choice(moves)

        board.push(move)

    print_board(board)
    nb_white, nb_black = board.get_nb_pieces()

    if nb_white > nb_black:
        print("Le joueur blanc remporte la partie !")
    elif nb_black > nb_white:
        print("Le joueur noir remporte la partie !")
    else:
        print("Match nul !")

if __name__ == "__main__":
    main()