from génération_nombre_premiers import is_prime
import timeit
import matplotlib.pyplot as plt

new_list = [0]
liste1 = []

def time_calcul():

    i = 0
    stop = [0]
    #Tant que trouver le nouveau nombre premier plus haut ne te prend pas plus de X temps, lance la recherche
    while int(stop[-1]) < 5:
        i += 1
        timeit.default_timer()
        if i not in new_list:
            if is_prime(i):
                new_list.append(i)
        stop.append(timeit.default_timer())
        liste1.append(int(stop[-1]))
    return liste1

time_calcul
plt.plot(time_calcul())
plt.show()

