from random import random

nb_fois = int(input("Combien de fois voulez-vous effectuer la simulation : "))


def compte():
    compteur = 0
    liste_de_n = []
    while compteur < nb_fois:
        n = 0

        for i in range(1, 101):
            x = random()
            if x < 0.5:
                n = n+1

        compteur += 1
        liste_de_n.append(n)
        
    print(liste_de_n)

compte()

