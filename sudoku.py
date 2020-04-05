
# PROJET : écrire un code Python permettant de résoudre des grilles de Sudoku de taille quelconque (pas seulement de taille 9)

# Constantes et import
import math as m
import copy

# 0 - Pour les tests

# Une grille est représenté par une liste de n**2 listes de longueur n**3.

# Exemple avec n = 3 (donc grilles de taille 9)

# Cette grille a un problème
A = [[1,2,3,4,5,6,7,8,9]]*9

# Grilles ayant des solutions, par ordre croissant de difficulté
B = [[5,0,8,6,0,0,0,9,0],[0,0,9,0,0,0,2,0,6],[3,4,0,9,0,0,5,8,0],[0,0,5,0,0,9,3,0,0],[6,1,7,3,0,4,9,5,2],[0,0,2,5,0,0,7,0,0],[0,6,3,0,0,7,0,1,9],[2,0,1,0,0,0,6,0,0],[0,9,0,0,0,6,8,0,5]]

C = [[0,5,4,0,3,0,0,7,0],[7,6,0,4,5,0,1,0,0],[0,1,0,0,6,7,0,0,9],[0,0,0,0,4,0,0,9,8],[8,4,0,0,0,0,0,6,5],[5,3,0,0,9,0,0,0,0],[4,0,0,1,2,0,0,8,0],[0,0,2,0,8,4,0,5,1],[0,8,0,0,7,0,2,3,0]]

D = [[6,2,0,0,9,0,0,0,5],[0,0,0,6,0,0,8,0,3],[1,0,0,4,0,0,2,5,0],[0,0,6,0,0,0,3,0,0],[0,7,2,0,0,9,0,0,4],[0,0,0,9,0,1,0,3,0],[9,0,7,0,0,4,0,0,0],[8,0,0,0,2,0,0,1,9]]

E = [[6,1,0,0,9,3,0,0,0],[0,0,0,1,0,0,0,3,9],[0,9,0,8,0,0,1,0,6],[0,0,8,0,0,0,0,1,7],[0,0,0,0,0,0,0,0,0],[9,4,0,0,0,0,2,0,0],[8,0,7,0,0,1,0,4,0],[5,2,0,0,0,6,0,0,0],[0,0,0,7,5,0,0,2,3]]

# Un grille de taille 4**2 = 16

F = [[0,0,11,0,10,0,12,4,8,5,0,15,0,7,0,0],[8,0,0,10,7,0,2,0,0,13,0,16,1,0,0,5],[0,0,0,2,0,0,5,0,0,12,0,0,13,0,0,0],[0,13,9,0,0,0,0,0,0,0,0,0,0,12,16,0],[5,0,0,3,0,11,13,2,7,4,16,0,14,0,0,9],[0,0,12,7,0,4,0,16,1,0,13,0,6,2,0,0],[11,10,4,0,0,5,0,0,0,0,14,0,0,16,7,13],[16,0,14,0,9,7,6,0,0,15,5,8,0,3,0,11],[13,0,3,0,8,16,10,0,0,2,12,4,0,11,0,7],[7,4,2,0,0,14,0,0,0,0,3,0,0,1,15,10],[0,0,5,15,0,2,0,12,13,0,8,0,16,6,0,0],[1,0,0,9,0,15,7,3,11,6,10,0,2,0,0,4],[0,7,6,0,0,0,0,0,0,0,0,0,0,5,2,0],[0,0,0,8,0,0,16,0,0,10,0,0,15,0,0,0],[9,0,0,4,2,0,3,0,0,15,0,12,7,0,0,1],[0,0,16,0,15,0,4,14,2,9,0,5,0,10,0,0]]

def affiche(G):
    # Celle-là, elle est offerte !
    """ Affiche joliment une grille de Sudoku. Fonctionne correctement jusqu'à la taille 81. """
    n = int(m.sqrt(len(G)))
    ligne_de_tirets = "-"*(3*len(G)+n+1)
    for i in range(len(G)):
        for j in range(len(G)):
            if j==0 and i%n == 0:
                print( ligne_de_tirets)
            if j%n == 0:
                print("|",end='')
            if G[i][j] != 0:
                print("{:3d}".format(G[i][j]),end='')
            else:
                print("   ",end='')
        print("|")
    print(ligne_de_tirets)


# À vous d'écrire les codes suivants. La consigne est 
#  - pour chaque fonction d'effacer la commande pass et de la remplacer par le code de la fonction   
#  - penser à vérifier chaque fonction avec des exemples simples
#  - utiliser au maximum les autres fonctions du fichier  
#  - la difficulté est indiquée, mais elle est (c) Pichaureau, donc pas forcément fiable...

def vérifie_ligne(L):
    # Niveau II
    """ Prend en paramètre une liste L et renvoie False si un élément non nul est présent plusieurs fois """
    pass

def grille_vide(n):
    # Niveau I
    """ Renvoie une grille remplie de 0, de taille n x n """
    pass

def transpose(G):
    # Niveau I
    pass

def petit_carré(G, k):
    # Niveau III
    """ Prend en paramètre une grille G et un entier k et renvoie le k-ième petit carré sous forme d'une liste.
    Pour un grille de taille 9, les petits carrés sont numérotés dans l'ordre : 
    0 1 2
    3 4 5
    6 7 8
    """
    pass

def est_correcte(G):
    # Niveau I 
    """ En utilisant les fonctions précédentes, vérifie que la grille G passée par paramètre est correcte. Renvoie True ou False selon.
    
    Une grille correcte est une grille où un numéro n'est pas présent deux fois sur une ligne, une colonne ou un petit carré. Mais cette grille peut encore contenir des 0.
    """
    pass


def ligne_complète(L):
    # Niveau I 
    """ Renvoie True si la liste L passée par paramètre ne contient aucun 0 et False si elle en contient au moins un """
    pass

def grille_complète(G):
    # Niveau I 
    """ Renvoie True si la grille G passée par paramètre ne contient aucun 0 et False si elle en contient au moins un """
    pass

def grille_terminée(G):
    # Niveau I
    """ En utilisant les fonctions précédentes, renvoie True si la grille G est terminée et False sinon """
    pass

def complète(G):
    # Niveau II
    """ Prend en paramètre une grille G, 
    - cherche une case contenant un 0 
    - si il n'y en a pas, renvoie une liste vide
    - s'il y en a un remplace ce 0 par chaque chiffre non présent dans la ligne
    - renvoie la liste des grilles ainsi fabriquées 

    Bien penser à faire des copies de listes ! 
    Par exemple :
    A = copy.deepcopy(G)
    
    """
    pass


def resoud(G):
    # Niveau Master of the BCPST
    """ Résoud une grille de Sudoku par la méthode du back-tracking """
    pass




    


