﻿# Recherche minimum d'une liste
la_liste = [1, 2, 3, -1, 1851, 8999, -151, 22, -5000]

def minimum_list():
    min_value = la_liste[0]
    for i in la_liste:
        if i < min_value:
            min_value = i
    return min_value

print(minimum_list())

