#include <stdio.h>
#include <math.h>

/**
 * imprimer_caractere_menger - Vérifie si position est au centre d'un bloc 3x3
 * @x: position horizontale
 * @y: position verticale
 * @niveau: niveau de l'éponge de Menger
 *
 * Return: Void.
 */
void imprimer_caractere_menger(int x, int y, int niveau)
{
	int i;

	for (i = 0; i < niveau; ++i)
	{
		if (x % 3 == 1 && y % 3 == 1)
		{
			putchar(' ');
			return;
		}
		x /= 3;
		y /= 3;
	}
	putchar('#');
}

/**
 * menger - Dessine une éponge de Menger 2D de niveau donné
 * @niveau: niveau de l'éponge de Menger à dessiner
 *
 * Return: Void.
 */
void menger(int niveau)
{
	int taille, y, x;

	if (niveau < 0)
	{
		return;
	}

	taille = pow(3, niveau);

	for (y = 0; y < taille; ++y)
	{
		for (x = 0; x < taille; ++x)
		{
			imprimer_caractere_menger(x, y, niveau);
		}
		putchar('\n');
	}
}
