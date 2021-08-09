import numpy as np
import random
import pandas as pd

""" print(np.array([1, 10]))
print(np.arange(10))
print("------------")
print(np.arange(8).reshape(2,4))
print("------------")
print(np.arange(8).reshape(4,2))
print(np.ones([100,50]))
print(np.random.rand(3,3)) """


""" my_array = np.random.rand(10, 50, 30)
print(my_array.size)
#print(my_array)
compteur = 0
for i in my_array:
    for j in i:
        for k in j:
            compteur += 1
print(compteur)


new = np.arange(8).reshape(4,2)
print(new)
print(new.shape)
 """
""" myArray_multidimension = np.random.rand(6).reshape(3,2)
print(myArray_multidimension)
print("------------")
print("------------")
print(myArray_multidimension[:,0]) # récupérer la ligne
print(myArray_multidimension[0,:]) # récupérer la colonne
print(myArray_multidimension[:,:]) # récupérer tout """
#         0       1
#0 [[0.90056645 0.46348188]
#1 [0.02078507 0.05621447]
#2 [0.92655352 0.11037336]]

""" A = np.arange(16).reshape(4,4)
B = np.arange(16).reshape(4,4)
print(A-B)
print(A*B) """

#print(pd.Series(np.array([1,2])))

print(pd.DataFrame({
    "colonne 1":[1,2,3],
    "colonne 2":[1,2,3],
    "colonne 3":[1,2,3],
    "colonne 4":[1,2,3]
                        }))