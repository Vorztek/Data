valeur_positive = 0
valeur_négative = 0
nb_valeurs = int(input("Combien de valeur souhaitez-vous saisir ? : "))

while valeur_négative + valeur_positive < nb_valeurs:
    
    valeur = int(input("Nouvelle valeur : "))

    if valeur == 0:
        print("Valeur nulle, veuillez rentrez une autre valeur")

    elif valeur > 0:
        valeur_positive += 1
        
    else:
        valeur_négative +=1

print(
    "Nombre de valeur positive : {} \n"        
    "Nombre de valeur négative : {} "
    .format(valeur_positive, valeur_négative)
    )