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
    global valeur
    valeur = 300 #l'input à add un jour
    compte = 0
    # Pour chaque élement compris dans la liste de chaque élement de l'intervalle
    for i in [j for j in range(1, valeur +1)]: 
        if verif_premier(i) is True:
            compte += 1

    # Print("Entre 1 et {} il y a {} nombres premier".format(valeur, compte))
    pourcent = ((compte / valeur) *100)
    return int(pourcent)

def courbe():
    liste1 = []
    for i in range(1, valeur):
        liste1.append(nombre_premier[i])
    return liste1

nombre_premier()
print(courbe())
