import matplotlib.pyplot as plt

def is_prime(p):
    if p < 2:
        return False
    for j in range(2, p):
        if p % j == 0:
            return False
    else:
        return True

meoisation = []
def number_of_prime(n):
    compte = 0
    # Pour chaque élement compris dans la liste de chaque élement de l'intervalle
    if n in meoisation:
        print("NEZOFLIUC")
        compte += 1
        pourcent = ((compte / n) *100)
        return pourcent
    else:
        for i in range(2, n): 
            if is_prime(i) is True:
                compte += 1
                if i not in meoisation:
                    meoisation.append(i)
        pourcent = ((compte / n) *100)
        print(meoisation)
        return pourcent

    # Print("Entre 1 et {} il y a {} nombres premier".format(valeur, compte))

def courbe():
    #valeur = int(input("Quelle est la valeur maximale souhaitée : "))
    liste1 = [number_of_prime(n) for n in range(5, 100)]
    return liste1

plt.plot(courbe())
plt.show()




