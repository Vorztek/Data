def recursion(a, b, i = 1):
    if i < b:
        a = recursion(a, b, i = i +1) + a
    return a

a, b = 1513, 599
resultat = recursion(a, b)
print(resultat)