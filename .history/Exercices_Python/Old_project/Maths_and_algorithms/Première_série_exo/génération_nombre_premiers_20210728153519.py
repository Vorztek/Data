import matplotlib.pyplot as plt

def is_prime(p):
    if p < 2:
        return False
    for j in range(2, p):
        if p % j == 0:
            return False
    else:
        return True

def number_of_prime(n):
    compte = 0
    meoisation = []
    # Pour chaque élement compris dans la liste de chaque élement de l'intervalle
    if n not in meoisation:
        for i in range(2, n): 
            if is_prime(i) is True:
                compte += 1
                meoisation.append(i)
                print(meoisation)
    # Print("Entre 1 et {} il y a {} nombres premier".format(valeur, compte))
    pourcent = ((compte / n) *100)
    return pourcent

def courbe():
    #valeur = int(input("Quelle est la valeur maximale souhaitée : "))
    liste1 = [number_of_prime(n) for n in range(5, 100)]
    return liste1

plt.plot(courbe())
plt.show()




