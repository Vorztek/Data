import matplotlib.pyplot as plt
import numpy as np

class nb_premiers_verif():

    def __init__(self, compte, valeur, compteur):
        self.compte = compte  #= 0
        self.valeur = valeur #= 300 #int(input("Veuillez saisir le nombre maximal de l'intervalle où seront cherchés les nombre premiers : "))
        self.compteur = compteur #= []
        
class calcul_pourcentage(nb_premiers_verif()):

    def verif_premier(p):
        if p < 2:
            return False
        for j in range(2, p):
            if p % j == 0:
                return False
        else:
            return True

    def nombre_premier(self, verif_premier):

        self.compteur = [i for i in range(1, self.valeur +1)]
        self.compteur = 3
        if self.verif_premier(self.compteur) == True:
            print("True")
        else:
            print("False")

        self.compte += (1 for p in self.compteur)
        #print("Entre 1 et {} il y a {} nombres premier".format(valeur, compte))
        pourcent = ((self.compte / self.valeur) *100)
        return pourcent

    def courbe(self, nombre_premier):
        for i in range(1, self.valeur):
            nombre_premier[i]

    print("fnbsld")

calcul_pourcentage()