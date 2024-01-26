Ce projet a été réalisé par Alice Gibier et Mila Cadix de M2 MIAGE.

L'ensemble du projet est disponible ici : https://filesender.renater.fr/?s=download&token=a1557fab-baae-4a59-900c-15134797d716

--------------------------
IAContreIA.py : 

Fonction heuristique : 
    Cette fonction évalue la qualité de la position des pièces en leur attribuants des scores. Les scores de chaque joueur sont ensuite additionnés pour créer un score global du joueur.
    Elle guide ainsi l'IA dans sa prise de décision.

    Les Paramètres : 
        board : L'objet de la classe Board représentant l'état actuel du jeu
        player : La pièce du joueur actuel, par défaut elle est déduite du joueur suivant.

    La fonction renvoie le score total du joueur.

Fonction MinMax : 
    Dans un premier temps nous avons fait le choix d'utiliser la méthode minmax afin de déterminer la meilleure stratégie possible pour un joueur, en prenant en compte les mouvements de l'adversaire.

    Les Paramètres :
        board: L'objet de la classe Board représentant l'état actuel du jeu
        depth: La profondeur maximale à laquelle l'algorithme minimax doit explorer
        maximizing_player: Un booléen indiquant si le joueur actuel cherche à maximiser ou minimiser le score
    La fonction renvoie le meilleur coup à jouer.

Fonction alpha_beta : 
    Dans un second temps nous avons choisi d'utiliser la méthode alpha beta afin de gagner en efficacité.
    Cette fonction implémente l'algorithme alpha beta en améliorant MinMax.

    Les paramètres : 
        board : L'objet de la classe Board représentant l'état actuel du jeu.
        depth : La profondeur maximale à laquelle on doit explorer
        alpha : Valeur actuelle de la meilleure valeur du joueur maximisant le score
        beta : Valeur actuelle de la meilleure valeure du joueur minimisant le score
        maximizing_player : Booléen indiquant si le joueur maximise ou minimise le score (True pour le joueur maximisant et False pour le joueur minimisant)
    La fonction retourne le meilleur score et le meilleur coup à jouer

Fonction play_eversi : 
    Cette fonction permet de jouer contre un adversaire avec alpha_beta. Elle crée le plateau de jeu (de 10x10 dans notre cas). Ensuite, la partie se déroule dans une boucle qui continue tant que le jeu n'est pas terminé suivant les règles de jeu. À chaque tour, le plateau est affiché, et montre le joueur actuel, que ce soit les pièces noires ou blanches. Une fois le jeu terminé, le plateau final et les résultats sont présentés pour que nous puissions voir comment la partie s'est déroulée en indiquant le meilleur coup, le meilleur score et le gagnant.



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
    Si c'est au tour du joueur, appelle la fonction player_move pour obtenir le mouvement du joueur. Sinon, l'ordinateur utilise alpha_beta pour jouer.
    Effectue le mouvement choisi en utilisant la méthode push de la classe Board.
    À la fin du jeu, affichons le plateau final et détermine le vainqueur en fonction du nombre de pièces de chaque joueur.


--------------------------
Nom de la meilleure IA : Alpha_Beta

Description de l'heuristique : 
    L'heuristique utilisée attribue des scores en fonction de la position des pièces sur le plateau.
        bonus_mobilité : des points sont attribués pour les positions offrants le plus de mouvements. Plus il y a de mouvements possibles, plus le score sera élevé.
        bonus_coin : 10 points sont attribués pour les positions des coins du plateau. Les points sont attribués pour la stratégie classique de Reversi des coins.
        bonus_board : 2 points sont attribués à chaque fois qu'un joueur à un piont sur le bord du plateau.

    A partir de cela, le score des joueurs est calculés en additionnant les différents bonus.

Techniques utilisées :
    Algorithme MinMax : il permet d'évaluer les coups possibles en prennant en compte les positions du joueur et de l'adversaire.
    Algorithme AlphaBeta : il permet d'amélirer l'efficacité de MinMax en élagant les branches qui sont sans conséquences sur l'évaluation d'un noeud. Ainsi, AlphaBeta est plus efficace et permet une recherche plus profonde.
    Intéraction avec un utilisateur : pour pouvoir s'assurer de l'efficacité de notre IA, nous avons implémenter une interraction humaine. Ainsi, on peut joueur contre notre IA.

Structure de données :
    Classe Reversi : fournit dans le sujet, elle donne l'ensemble des règles du jeu Reversi, l'état actuel, les positions des pièces, ...
                    Elle nous fournit notamment le plateau Board.
