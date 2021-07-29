"""n = int(input("Entrer une valeur n : "))
"""

n = int(input("Combien de valeurs voulez-vous ? : "))

S = 0

compteur = 0
entrepot = []

for i in range(1, n + 1):
    S = S+2 * i
    print("S = ", S)
    entrepot.append(S)
    compteur += 1
    
print(entrepot)

# 