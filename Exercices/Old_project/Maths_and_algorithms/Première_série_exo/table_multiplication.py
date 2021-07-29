valeur = int(input("Quelle table désirez-vous ? "))
table_max = int(input("Jusqu'à quelle valeur ? "))
valeur_incrémenté = 0

while valeur_incrémenté != table_max:
    valeur_incrémenté += 1
    print(' {} * {} = {}\n' .format(valeur, valeur_incrémenté, valeur_incrémenté * valeur))