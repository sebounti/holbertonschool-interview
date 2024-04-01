#!/usr/bin/python3

import sys


def print_usage():
    print("Usage: nqueens N")
    sys.exit(1)


def print_erreur(message):
    print(message)
    sys.exit(1)


def position_valide(echiquier, ligne, colonne, N):
    # Vérifie cette ligne sur le côté gauche
    for i in range(colonne):
        if echiquier[ligne][i] == 1:
            return False

    # Vérifie la diagonale supérieure sur le côté gauche
    for i, j in zip(range(ligne, -1, -1), range(colonne, -1, -1)):
        if echiquier[i][j] == 1:
            return False

    # Vérifie la diagonale inférieure sur le côté gauche
    for i, j in zip(range(ligne, N, 1), range(colonne, -1, -1)):
        if echiquier[i][j] == 1:
            return False

    return True


def resoudre_nqueens(echiquier, colonne, N):
    # Cas de base : si toutes les reines sont placées
    if colonne >= N:
        solution = []
        for i in range(N):
            for j in range(N):
                if echiquier[i][j] == 1:
                    solution.append([i, j])
        print(solution)
        return

    # essayer de placer cette reine dans toutes les lignes une par une
    for i in range(N):
        if position_valide(echiquier, i, colonne, N):
            echiquier[i][colonne] = 1
            resoudre_nqueens(echiquier, colonne + 1, N)
            echiquier[i][colonne] = 0  # retour en arrière (backtrack)


def main():
    if len(sys.argv) != 2:
        print_usage()

    try:
        N = int(sys.argv[1])
    except ValueError:
        print_erreur("N must be a number")

    if N < 4:
        print_erreur("N must be at least 4")

    echiquier = [[0 for _ in range(N)] for _ in range(N)]
    resoudre_nqueens(echiquier, 0, N)


if __name__ == "__main__":
    main()
