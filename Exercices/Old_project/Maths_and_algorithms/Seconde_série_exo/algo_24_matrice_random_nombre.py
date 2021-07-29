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

def afficher_matrice(matrice):
    for line in matrice:
        print(line)

print(afficher_matrice(matrice))

