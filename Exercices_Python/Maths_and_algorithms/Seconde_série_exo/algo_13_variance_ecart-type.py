from math import *
from statistics import *

liste = [0, 10, 20, 15, 5, 13, 7, 0, 20, 18, 16, 4, 2]

sum_liste = 0
moyenne = (sum(liste)/len(liste))

def variance_type(liste):
    var = 0
    for i in liste:
        global moyenne
        
        var += (i - moyenne)**2
    
    variance = (1 / len(liste)) * var
    return variance

print(moyenne)
print(variance_type(liste))
print(pvariance(liste))

#calcul ecart-type

print((variance_type(liste))** 0.5)