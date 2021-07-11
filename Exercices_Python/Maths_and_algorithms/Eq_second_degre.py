import fractions
import math 
from fractions import Fraction

print("Entrer les coefficients : ")

a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))

if a == 0:
    if b == 0:
        print("Aucune solution")
    else:
        print("Une solution : {}".format(-c/b))
else:
    delta = (b * b) - (4 * a * c)
    print("Le delta est de : {}".format(delta))
    if delta < 0:
        print ("Aucune solution dans R")
    else:
        if delta == 0:
            print("Une solution : {}".format(-b/(2 * a)))
        else:
            valeur1 = (-b - (delta ** 0.5) / (2 * a))
            valeur2 = (-b + (delta ** 0.5) / (2 * a))
            print("Deux solutions : {} et {}".format(valeur1, valeur2))
            