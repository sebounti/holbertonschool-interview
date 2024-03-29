#include <stdio.h>
#include <math.h>

void imprimer_caractere_menger(int x, int y, int niveau) {
    for (int i = 0; i < niveau; ++i) {
        // Vérifier si la position courante est au centre d'un bloc 3x3
        if (x % 3 == 1 && y % 3 == 1) {
            putchar(' ');
            return;
        }
        x /= 3;
        y /= 3;
    }
    putchar('#');
}

void menger(int niveau) {
    if (niveau < 0) return; // Ne rien faire si le niveau est inférieur à 0

    int taille = pow(3, niveau); // Calculer la taille de l'éponge

    for (int y = 0; y < taille; ++y) {
        for (int x = 0; x < taille; ++x) {
            imprimer_caractere_menger(x, y, niveau);
        }
        putchar('\n'); // Nouvelle ligne à la fin de chaque rangée
    }
}
