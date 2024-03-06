#!/usr/bin/python3
"""
Main file for testing
"""


def validUTF8(data):
    # Nombre de bytes dans le caractère UTF-8
    n_bytes = 0

    # Pour chaque entier dans les données
    for num in data:
        # Obtenez la représentation binaire.
        bin_rep = format(num, '#010b')[-8:]

        # Si c'est le début d'un nouveau caractère UTF-8
        if n_bytes == 0:
            # Comptez le nombre de 1 au début
            for bit in bin_rep:
                if bit == '0':
                    break
                n_bytes += 1

            # Caractères d'un byte
            if n_bytes == 0:
                continue

            # Scénarios invalides selon les règles de l'UTF-8
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # Pour un caractère de n bytes, les bytes suivants
            # doivent commencer par '10'
            if not (bin_rep[0] == '1' and bin_rep[1] == '0'):
                return False

        # Diminuez le nombre de bytes à traiter de 1 après chaque byte
        n_bytes -= 1

    # Ceci vérifie s'il reste des bytes qui n'ont pas été traités
    return n_bytes == 0
