#https://www.youtube.com/watch?v=O3yZZGIy9mQ&list=PL6JtJ0Q7T-YwoXY5PletTK9ITQ8YPDa-G&index=16

liste = [1, 800, -4]
print(sum(liste))

def somme(liste):
    total = 0
    for i in liste:
        total += i
    print(total)

somme(liste)