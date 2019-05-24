import numpy as np
import matplotlib.pyplot as plt
import math

def calcul_nb_voisins(Z):
    forme = len(Z), len(Z[0])
    N = [[0, ] * (forme[0]) for i in range(forme[1])]
    for x in range(1, forme[0] - 1):
        for y in range(1, forme[1] - 1):
            N[x][y] = Z[x-1][y-1]+Z[x][y-1]+Z[x+1][y-1] \
            + Z[x-1][y] + 0 +Z[x+1][y] \
            + Z[x-1][y+1]+Z[x][y+1]+Z[x+1][y+1]
    return N




def iteration_jeu(Z):
    """
    Fonction qui prend en argument l'état initial du jeu de la vie (sous forme de liste de liste).
    Fonction qui retourne l'état du jeu après 1 itération.
    
    La fonction fait appel à la fonction qui calcule le nombre de voisins puis modifie
    les cellules, qui sont représentées par des 0 ou des 1 dans la matrice Z,
    en appliquant la règle de décision expliquée ci dessus.
    
    """
    
    forme = len(Z), len(Z[0])
    N = calcul_nb_voisins(Z)
    for x in range(1,forme[0]-1):
        for y in range(1,forme[1]-1):
            if Z[x][y] == 1 and (N[x][y] < 2 or N[x][y] > 3):
                Z[x][y] = 0
            elif Z[x][y] == 0 and N[x][y] == 3:
                Z[x][y] = 1
    return Z


from numba import jit


@jit(nopython=True)
def calcul_nb_voisins_fast(Z):
    forme = len(Z), len(Z[0])
    N = [[0, ] * (forme[0]) for i in range(forme[1])]
    for x in range(1, forme[0] - 1):
        for y in range(1, forme[1] - 1):
            N[x][y] = Z[x-1][y-1]+Z[x][y-1]+Z[x+1][y-1] \
            + Z[x-1][y] + 0 +Z[x+1][y] \
            + Z[x-1][y+1]+Z[x][y+1]+Z[x+1][y+1]
    return N


@jit(nopython=True)
def iteration_jeu_fast(Z):
    """
    Fonction qui prend en argument l'état initial du jeu de la vie (sous forme de liste de liste).
    Fonction qui retourne l'état du jeu après 1 itération.
    
    La fonction fait appel à la fonction qui calcule le nombre de voisins puis modifie
    les cellules, qui sont représentées par des 0 ou des 1 dans la matrice Z,
    en appliquant la règle de décision expliquée ci dessus.
    
    """
    forme = len(Z), len(Z[0])
    N = calcul_nb_voisins_fast(Z)
    for x in range(1, forme[0] - 1):
        for y in range(1,forme[1]-1):
            if (Z[x][y] == 1) and (N[x][y] < 2 or N[x][y] > 3):
                Z[x][y] = 0
            elif (Z[x][y] == 0) and (N[x][y] == 3):
                Z[x][y] = 1
    return Z

def iteration(Z, nb_iter):
    plt.figure(figsize=(25,20))
    Zbis = np.copy(Z)
    for i in range(nb_iter):
        plt.subplot(math.ceil(nb_iter/5),5,i+1)
        plt.imshow(np.array(Zbis))
        Zbis = iteration_jeu(Zbis)
        
        
def fig_digit(x, w, alpha):
    """
    """
    plt.subplot(1,2,1)
    plt.imshow(x.reshape(28,28))
    xmod = x.reshape(784,1)-alpha/np.linalg.norm(w)**2 * np.dot(w.T,x) * w
    plt.subplot(1,2,2)
    plt.imshow(xmod.reshape(28,28))