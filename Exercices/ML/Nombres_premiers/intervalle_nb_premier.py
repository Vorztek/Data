nb_premier = 2000
liste1 = []
i = 2
def milaine():
    for i in range(2, nb_premier + 1):
        if i > 2:  
            for j in range(2,i):
                if j % i == 0:
                    break
            
                print(j)

                
print(milaine())