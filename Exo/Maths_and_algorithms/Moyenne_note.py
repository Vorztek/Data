def moyenne():
    note = 0
    compteur = 0
    somme_notes = 0    
    while note != -1:
        note = int(input("Rentrez la note d'un nouvel élève : "))
        somme_notes += note
        compteur += 1
    else:
        print("La moyenne de la classe est de : {}".format(somme_notes / compteur))
    
moyenne()