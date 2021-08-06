import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
import pandas as pd

iris = pd.read_csv(r'C:\Users\vion1\Ele\Engie\Exercices\ML\iris\iris.csv')
print(iris.head())

""" 
#avec scatter, graphique 2D
print(plt.scatter(x[:, 0], x[:, 1], c = y, alpha = 0.7, s = 200))
""" 

# Graphique 3D
ax = plt.axes(projection = '3d')
print(ax.scatter(x[:, 0], x[:, 1], x[:, 2], c = y, alpha = 0.7, s = 50)) 



#sns.pairplot(iris, hue = 'variety')