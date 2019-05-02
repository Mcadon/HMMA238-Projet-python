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