from math import *
from statistics import *

liste = [0, 10, 20, 15, 5, 13, 7, 0, 20, 18, 16, 4, 2]

#sum_liste = 0
#moyenne = (sum(liste)/len(liste))

def factorielle(i):
    valeur = 1
    for i in range(1, i +1):
        valeur = valeur *i
    return valeur
print(factorielle(7))
