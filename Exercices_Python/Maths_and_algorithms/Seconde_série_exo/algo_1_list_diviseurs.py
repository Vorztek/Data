# Source : https://www.youtube.com/watch?v=68MswC7M8IU&list=PL6JtJ0Q7T-YwoXY5PletTK9ITQ8YPDa-G

#Liste des diviseurs d'un nombre entier

def get_divide(nb):
    list_diviseurs = []
    
    for i in range(1, nb +1):
        if nb % i == 0:
            list_diviseurs.append(i)
            
    print(list_diviseurs)

get_divide(924)