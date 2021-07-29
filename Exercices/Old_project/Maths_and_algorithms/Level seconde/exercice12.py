def calcul_montant(nb_km):
    prix_location = 50
    nb_km_more = nb_km - 100
    if nb_km < 100:
        montant1 = prix_location + 0.25 * nb_km
        print(int(montant1))
    else:
        montant2 = (prix_location + 0.25 * nb_km) + (0.33 * nb_km_more)
        print(int(montant2))

nb_km = int(input("Combien de km avez-vous parcouru :  "))
calcul_montant(nb_km)