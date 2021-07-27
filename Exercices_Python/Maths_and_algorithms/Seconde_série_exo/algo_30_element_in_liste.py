liste1 = [1, 2, 3, 5, 9, 45]
liste2 = [1, 6, 3, 8, 9, 41, 42, 1]
liste3 = []

for i in liste1:
    for j in liste2:
        if i == j:
            liste3.append(i)
    
liste3 = set(liste3)
liste3 = list(liste3)
print(liste3, type(liste3))