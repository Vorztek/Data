def somme(n, k):
    total = 0
    for i in range(k+1):
        total += n**i
    return total

print(somme(4, 9))