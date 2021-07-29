def get_divide(nb):
    list_diviseurs = []
    
    for i in range(1, nb +1):
        if nb % i == 0:
            list_diviseurs.append(i)
    return list_diviseurs
            
    #print(list_diviseurs)

def perfect_number(nb):
    
    if get_divide(nb):
        if nb == sum(get_divide(nb)) / 2:
            return True
        else:
            return False

def get_perfect(n, p):
    perfect_list = []
    for i in range(n, p):
        if perfect_number(i):
            perfect_list.append(i)
    print(perfect_list)

get_perfect(0, 10000)