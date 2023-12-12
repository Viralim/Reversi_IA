Ce projet a été réalisé par Alice Gibier et Mila Cadix de M2 MIAGE.

Reversi.py :

Optimisation des fonctions : 


--------------------------
IAContreIA.py : 

Fonction MinMax : 
    Dans un premier temps nous avons fait le choix d'utiliser la méthode minmax afin de déterminer la meilleure stratégie possible pour un joueur, en prenant en compte les mouvements de l'adversaire.

    Les Paramètres :
        board: L'objet de la classe Board représentant l'état actuel du jeu
        depth: La profondeur maximale à laquelle l'algorithme minimax doit explorer
        maximizing_player: Un booléen indiquant si le joueur actuel cherche à maximiser ou minimiser le score
    La fonction renvoie le meilleur coup à jouer.

Fonction play_reversi : 
    Cette fonction permet de jouer contre un adversaire avec l'algorithme MinMax. Elle crée le plateau de jeu (de 10x10 dans notre cas). Ensuite, la partie se déroule dans une boucle qui continue tant que le jeu n'est pas terminé suivant les règles de jeu. À chaque tour, le plateau est affiché, et montre le joueur actuel, que ce soit les pièces noires ou blanches. Une fois le jeu terminé, le plateau final et les résultats sont présentés pour que nous puissions voir comment la partie s'est déroulée en indiquant le meilleur coup, le meilleur score et le gagnant.

--------------------------
JoueurContreOrdi.py

Fonction print_board(board) :
    Affiche le plateau de jeu en utilisant des 'X' pour les pièces noires, des 'O' pour les pièces blanches, et des points '.' pour les cases vides.

Fonction player_move(board) :
    Permet au joueur de saisir ses mouvements en affichant le plateau actuel.
    Pour faciliter le jeu nous affichons les coups possibles pour le joueur en utilisant la fonction all_possible_moves.
    Demande au joueur de saisir les coordonnées x et y pour son mouvement. le jeu vérifie si le mouvement est valide à l'aide de la méthode is_valid_move de la classe Board.

Fonction all_possible_moves(board) :
    Génère et retourne la liste de tous les coups possibles pour le joueur actuel.
    Parcourt toutes les coordonnées du plateau et utilise la méthode lazyTest_ValidMove de la class Board pour déterminer si un mouvement est possible.
    Si aucun mouvement n'est possible, ajoute un mouvement spécial ([joueur, -1, -1]) indiquant que le joueur passe son tour.

Définition de la fonction main() :
    Initialise un objet Board. La boucle principale continue tant que le jeu n'est pas terminé. Ensuite nous affichons le plateau actuel.
    Si c'est au tour du joueur, appelle la fonction player_move pour obtenir le mouvement du joueur. Sinon, l'ordinateur choisit un mouvement aléatoire parmi les coups possibles.
    Effectue le mouvement choisi en utilisant la méthode push de la classe Board.
    À la fin du jeu, affichons le plateau final et détermine le vainqueur en fonction du nombre de pièces de chaque joueur.