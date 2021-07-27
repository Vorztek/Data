def identite_positive(a, b):
    x = a ** 2
    y = 2 * a * b
    z = b ** 2
    valeur = (x)+(y)+(z)
    print("(",a,"+",b,")² =",x,"+",y,"+",z,"=",valeur)
    
    
identite_positive(2, 5)

def identite_negative(a, b):
    x = a ** 2
    y = -1 * 2 * a * b
    z = b ** 2
    valeur = (x)+(y)+(z)
    print("(",a,"+",b,")² =",x,"+",y,"+",z,"=",valeur)
    
    
identite_negative(2, 5)

def identite_troisieme(a, b):
    x = a - b
    y = a + b
    
    valeur = (x)*(y)
    print("(",a,"+",b,")² =",valeur)
    
    
identite_troisieme(3, 2)