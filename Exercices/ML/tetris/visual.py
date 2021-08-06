import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



df = pd.read_csv(r'C:\Users\vion1\Ele\Engie\Exercices\ML\tetris\dataset.csv')

y = df['Score']
x = df['timing']
plt.xlabel('Temps en secondes')
plt.ylabel('Score atteint')

plt.scatter(x, y, c = x)
plt.show()