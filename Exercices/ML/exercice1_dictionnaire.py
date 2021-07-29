classeur = {
    "positif" : [],
    "negatif" : [],
}

def function():
    
    for i in range((-100*2), 100):

        if i > 0 :
            classeur["positif"].append(i)
        if i < 0 :
            classeur["negatif"].append(i)  
        
    return classeur["positif"], classeur["negatif"]

print(function())