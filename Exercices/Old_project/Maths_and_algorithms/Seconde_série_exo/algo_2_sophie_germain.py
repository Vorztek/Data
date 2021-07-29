def is_prime(nb):
    if nb < 2:
        return False

    for i in range(2, nb):
        if nb % i == 0:
            return False

    return True

def SG_prime(nb):
    if is_prime(nb):
        if 2 * nb + 1:
            return True
    else: 
        return False

def intervalle(inf, sup):
    list_intervalle = []
    for i in range(inf, sup +1):
        if SG_prime(i):
            list_intervalle.append(i)
    print(len(list_intervalle), list_intervalle )

intervalle(99900, 100000)