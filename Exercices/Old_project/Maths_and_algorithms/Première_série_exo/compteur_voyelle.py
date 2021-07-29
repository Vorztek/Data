
def compteur_voyelle():
    voyelle = ['a','e', 'i', 'o', 'u', 'y']
    compteur = 0 
    phrase = input("Quelle phrase voulez-vous étudiez ? : ")
    for i in phrase:
        if i in voyelle:
            compteur += 1
    print(compteur)

compteur_voyelle()

new = input("Voulez-vous tester une nouvelle phrase ? yes/no ")

if new == "yes":
    compteur_voyelle()
else:
    exit()



