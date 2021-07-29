def leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 == 0:
        if year % 400 != 0:
            return False
        else:
            return True
    elif year % 100 != 0:
        return True


def liste_leap_year(year):
    liste = []
    compteur = 0
    for i in range(0, year + 1):
        if leap_year(i) is True:
            liste.append(i)
            compteur += 1
    print(compteur)
    print(liste[-1])

liste_leap_year(100000)