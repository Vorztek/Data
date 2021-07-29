from math import *

liste = [1, 5, 2, 56]

sum_liste = 0
N = len(liste)
for i in liste:
    while sum_liste == 0:
        sum_liste += i
    else:
        sum_liste *= i

racine = sum_liste ** 1/len(liste)

print(racine)

#ou geometric_mean