import matplotlib.pyplot as plt
from numpy.core.fromnumeric import shape
from mpl_toolkits.mplot3d import Axes3D
import timeit

memoisation = [0]
liste1 = []
new_list = [0]
most_prime = []
def is_prime(p):
    if p < 2:
        return False 

    for j in range(2, p):
        if p % j == 0:
            return False
    else:
        memoisation.append(p)
        return True, memoisation

def number_of_prime(n):
    compte = 0
    for i in range(2, n):
        if i not in memoisation:
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

""" plt.plot(courbe())
plt.show() """

#L'objectif est d'avoir une fonction du temps
def time_calcul(n):
    i = 0
    stop = [0]
    #Tant que trouver le nouveau nombre premier plus haut ne te prend pas plus de X temps, lance la recherche
    while int(stop[-1]) < n:
        i += 1
        timeit.default_timer()
        if i not in memoisation:
            if is_prime(i):
                new_list.append(i)
        #if timeit.default_timer() not in stop: > rajoute du temps, on atteint que 20 000
                stop.append(timeit.default_timer())
    return new_list, stop #On return la nouvelle liste obtenu de nombre entier, puis le temps nécessaire 


y, x = time_calcul(10)
plt.plot(x, y) #rajouter y si on veut le temps 
plt.show() 
#ax = plt.axes(projection = "3d")
#print(ax.scatter(x, y))

#from scipy.interpolate import inter1d

