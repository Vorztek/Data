from math import *

rayon, hauteur, = input("Entrer les valeurs de rayon r et la hauteur h : ").split()
rayon = int(rayon)
hauteur = int(hauteur)

aire = rayon * hauteur * pi * 2
volume = int(rayon ** 2 * hauteur * pi)

print("Le volume est de {} cm cube".format(volume))