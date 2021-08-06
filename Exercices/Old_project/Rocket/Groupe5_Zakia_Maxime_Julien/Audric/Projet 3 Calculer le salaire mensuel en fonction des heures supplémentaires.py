#Projet 3 Calculer le salaire mensuel en fonction des heures supplémentaires

print("quel est votre salaire de base ?")
salaire_base = input()
print("Veuillez renseigner le nombre H effectuees")
heures_effect = input()
print("renseignez le taux horaire")
taux_H = input()
#transformation en int
new_salaire_base = int(salaire_base)
new_heures_effect = int(heures_effect)
new_taux_H = int(taux_H)

if new_heures_effect >= 40:
        new_salaire = new_salaire_base + (12 * 1.5) * (new_heures_effect - 39) #c'est pas trop des float mais ça marche quand même ?
elif heures_effect >= 45:
        new_salaire = new_salaire_base + (12 * 1.75) * (new_heures_effect - 39)
else :
        new_heures_effect >= 50
        new_salaire = new_salaire_base + (12 * 2) * (new_heures_effect - 39)
print ("Votre salaire est de {}".format(new_salaire))
