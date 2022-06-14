import numpy as np

def placement_cellule(g, y, x):
    g[y - 1][x - 1] = 1
    return g


def addcase(g1, g2):
    for a in range(LG - 2):
        for b in range(LG - 2):
            x = g1[a][b] + g1[a][b + 1] + g1[a][b + 2] + g1[a + 1][b] + g1[a + 1][b + 2] + g1[a + 2][b] + g1[a + 2][b + 1] + g1[a + 2][b + 2]
            g2[a + 1][b + 1] = x
    return g2

def vie(g3, g4):
    addcase(g3, g4)
    for i in range(LG - 1):
        for j in range(LG - 1):
            if g3[i+1][j+1] == 1:
                if g4[i + 1][j + 1] == 2 or g4[i + 1][j + 1] == 3:
                    g3[i + 1][j + 1] = 1
                else :
                    g3[i + 1][j + 1] = 0
            elif g3[i+1][j+1] == 0:
                if g4[i + 1][j + 1] == 3:
                    g3[i + 1][j + 1] = 1
                else :
                    g3[i + 1][j + 1] = 0

    return g3




LG = int(input("Dimension du Jeu de La Vie :"))
NBF = int(input("Nombre de Frame:"))
grille = np.zeros((LG, LG))
grille2 = np.zeros((LG, LG))
NbCV = int(input("Nombre de Cellule Vivante:"))

init = 0
init2 = 0

while init < NbCV:
    init += 1
    print("Cellule:", init)
    CVX = int(input("Position en x de la cellule:"))
    CVY = int(input("Position en y de la cellule:"))
    placement_cellule(grille, CVY, CVX)

print(grille)

while init2 < NBF:
    init2 += 1
    print("Frame:", init2)
    print(vie(grille,grille2))