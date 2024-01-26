import math
import Reversi
from Reversi import Board
import random

#Fonction d'implémentation de l'heuristique par bonus en fonction de la position sur le plateau
def heuristique(board, player=None):
    if player is None:
        player=board._nextPlayer
    bonus_mobilite = len(board.legal_moves())  # bonus pour la position qui offre plus de mobilité au joueur
    bonus_coin = sum([board._board[x][y] == player for x, y in [(0, 0), (0, 9), (9, 0), (9, 9)]]) * 10  # Bonus pour un coins
    bonus_bord = sum([board._board[x][y] == player for x in range(10) for y in [0, 9]]) * 2  # Bonus pour les bords du plateau
    score=bonus_mobilite+bonus_coin+bonus_bord
    return score

#Fonction qui implémente l'algorithme MinMax sans élagage alpha-beta
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

#Fonction qui implémente l'algorithme alpha_beta et retourne le meilleur coup
def alpha_beta(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.is_game_over():
        return board.heuristique(), None

    best_move = None

    if maximizing_player:
        max_eval = -math.inf
        for move in board.legal_moves():
            player, x, y = move
            board.push(move)
            eval, _ = alpha_beta(board, depth - 1, alpha, beta, not maximizing_player)
            board.pop()
            
            if eval > max_eval:
                max_eval = eval
                best_move = move

            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cut-off

        return max_eval, best_move
    else:
        min_eval = math.inf
        for move in board.legal_moves():
            player, x, y = move
            board.push(move)
            eval, _ = alpha_beta(board, depth - 1, alpha, beta, not maximizing_player)
            board.pop()

            if eval < min_eval:
                min_eval = eval
                best_move = move

            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cut-off

        return min_eval, best_move


#Fonction qui fait jouer Reversi
def play_Reversi():
    board = Reversi.Board(boardsize=10)
    depth = 4  
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
    play_Reversi()

    #Appel MinMax pour trouver le meilleur coup
    #best_score, best_move = MinMax(initial_board, depth=3, maximizing_player=True)
    #Appel alpha_beta pour trouver le meilleur coup
    best_score, best_move = alpha_beta(initial_board, depth=4, alpha = -math.inf, beta = math.inf, maximizing_player=True)

    print("Meilleur score:", best_score)
    print("Meilleur coup:", best_move)