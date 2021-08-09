import random 
liste4 = []

def gen_number(o,p):
    for i in range(0,o):
        n = random.randint(0,p)
        liste4.append(n)
    return liste4 