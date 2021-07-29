prix1 = 0.15
prix2 = 0.10

nb_copies = int(input("Entrer N : "))
prix_total = 0

if nb_copies < 50:
     prix_total = nb_copies * prix1
else:
    prix_total = (prix1 * 50) + (prix2 * (nb_copies - 50)) 

print("Le prix total est de : {}€".format(prix_total))
