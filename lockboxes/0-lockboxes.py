#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Détermine si toutes les boîtes peuvent être déverrouillées en utilisant les clés fournies.

    Args :
    - boxes : Une liste de listes. Chaque sous-liste représente une boîte et contient les clés
              pour ouvrir d'autres boîtes.

    Returns :
    - True si toutes les boîtes peuvent être déverrouillées, sinon False.
    """

    '''Vérifie si la liste est vide ou nulle (aucune boîte à ouvrir)'''
    if not boxes or len(boxes) == 0:
        return False

    '''Initialise une liste pour suivre les boîtes que nous avons déjà déverrouillées,
    en commençant par la première boîte (indice 0)'''
    unlocked_boxes = [0]

    '''Itère à travers chaque boîte déjà déverrouillée pour trouver et utiliser les clés'''
    for box in unlocked_boxes:
        '''Itère à travers chaque clé dans la boîte actuellement ouverte'''
        for key in boxes[box]:
            ''' Ajoute la clé à la liste des boîtes déverrouillées si elle ouvre une nouvelle boîte'''
            ''' et si la clé n'est pas hors de la portée (indice valide)'''
            if key not in unlocked_boxes and key < len(boxes):
                unlocked_boxes.append(key)

    '''Compare le nombre de boîtes déverrouillées au nombre total de boîtes pour déterminer'''
    '''si toutes les boîtes ont été ouvertes'''
    return len(unlocked_boxes) == len(boxes)
