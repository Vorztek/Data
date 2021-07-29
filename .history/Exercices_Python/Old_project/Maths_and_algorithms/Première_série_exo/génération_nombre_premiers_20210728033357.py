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
    valeur = 300 #l'input à add un jour
    compte = 0
    compteur = []
    a = []
    compteur = [i for i in range(1, valeur +1)]
    for i in compteur: 
        if verif_premier(i) is True:
            a.append(i)
            compte += 1
    
    print(a)
    if a is True:
        print("True")
    else:
        print("False")

    #print("Entre 1 et {} il y a {} nombres premier".format(valeur, compte))
    pourcent = ((compte / valeur) *100)
    return pourcent

def courbe(self, nombre_premier):
    for i in range(1, self.valeur):
        nombre_premier[i]

print(nombre_premier())
