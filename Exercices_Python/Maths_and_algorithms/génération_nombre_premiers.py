def verif_premier(i):
    if i < 2:
        return False
    for j in range(2, i):
        if i % j == 0:
            return False
    else:
        return True

def nombre_premier():
    compte = 0
    valeur = int(input("Veuillez saisir un nombre supérieur à 1 : "))
    compteur = []
    for i in range(1, valeur + 1):
        compteur.append(i)      
    for i in compteur:
        if verif_premier(i):
            compte += 1
            print(i)
    print("Entre 1 et {} il y a {} nombres premier".format(valeur, compte))
nombre_premier()