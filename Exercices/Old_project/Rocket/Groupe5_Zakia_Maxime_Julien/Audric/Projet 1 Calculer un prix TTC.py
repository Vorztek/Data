# Projet 1 : Calculer un prix TTC
print("Renseigne un prix")
prix_ht = input()
new_prix_ht = int(prix_ht)

while new_prix_ht > 0:
    prixttc = new_prix_ht * 1.196
    print(prixttc)
    new_prix_ht = input()
    new_prix_ht = int(prix_ht)
    print("Au revoir")
    break

#Il faut retransformer en int à l'intérieur de la fonction while ?!!