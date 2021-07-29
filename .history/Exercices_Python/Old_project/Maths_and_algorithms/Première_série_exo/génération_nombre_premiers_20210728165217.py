import matplotlib.pyplot as plt
import time
start_time = time.time()

meoisation = []
def is_prime(p):
    if p < 2:
        return False
    for j in range(2, p):
        if p % j == 0:
            return False
    else:
        meoisation.append(p)
        return True

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
    liste1 = []
    #valeur = int(input("valeur maximale ? : "))
    for n in range(5, 3000, 100):
        liste1.append(number_of_prime(n))
    return liste1

plt.plot(courbe())
print("- %s seconds -" % int((time.time() - start_time)))
plt.show()




