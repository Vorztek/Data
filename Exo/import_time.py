def verif_premier(i):

    if i < 2:
        return False
    for j in (2, i):
        if i % j == 0:
            return False
    else:
        return True

print(verif_premier(12))