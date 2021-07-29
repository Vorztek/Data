import matplotlib.pyplot as plt

meoisation = [0]
liste1 = []

def is_prime(p):
    for j in range(2, p):
        if p % j == 0:
            return False
    else:
        meoisation.append(p)
        return True, meoisation

def number_of_prime(n):
    compte = 0
    for i in range(2, n):
        if i not in meoisation:
            if is_prime(i) is True:
                compte += 1
        else:
            compte += 1
    pourcent = ((compte / n) *100)
    return pourcent

def courbe():
    for n in range(5, 500):
        liste1.append(number_of_prime(n))
    return liste1

plt.plot(courbe())
plt.show()




