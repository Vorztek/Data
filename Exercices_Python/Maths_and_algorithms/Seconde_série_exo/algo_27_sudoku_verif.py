from random import randint

def gen_matrice(M,N, inf, sup):
    matrice = []

    for i in range(M):
        line = []
        for j in range (N):
            line.append(randint(inf, sup))

        matrice.append(line)

    return matrice

matrice = gen_matrice(9, 9, 1, 9)
compteur = 0

def is_valid(grille):
  
    for line in grille: # test des lignes
        if not len(set(line)) == 9:
            return False
    
    for i in range(9): # test des colonnes
        column = []
        for j in range(9):
            column.append(grille([j][i]))
        if not len(set(column)) == 9: # ou if != de 9
            return False 

    for y0 in [0, 3, 6]:
        for x0 in [0, 3, 6]:
            subgrid = []
            for i in range(0, 3):
                for j in range(0, 3):
                    if grille[y0 + i][x0 + j] in subgrid:
                        return False
                    subgrid.append(grille[y0 + i][x0 + j])
    return True

while is_valid(matrice) is False:
    compteur += 1
    print(compteur)