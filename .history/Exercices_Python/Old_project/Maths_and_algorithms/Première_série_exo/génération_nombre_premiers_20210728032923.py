import matplotlib.pyplot as plt
import numpy as np

def verif_premier(p):
    if p < 2:
        return False
    for j in range(2, p):
        if p % j == 0:
            return False
    else:
        return True

def nombre_premier():
    valeur = 300
    compte = 0
    compteur = []
    compteur = [i for i in range(1, valeur +1)]
    compteur = 3
    a = verif_premier(3)

    if a is True:
        print("True")
    else:
        print("False")

    compte += (1 for p in compteur)
    #print("Entre 1 et {} il y a {} nombres premier".format(valeur, compte))
    pourcent = ((compte / valeur) *100)
    return pourcent

def courbe(self, nombre_premier):
    for i in range(1, self.valeur):
        nombre_premier[i]

print(nombre_premier())
