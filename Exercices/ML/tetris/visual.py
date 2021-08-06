import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



df = pd.read_csv(r'C:\Users\vion1\Ele\Engie\Exercices\ML\tetris\dataset.csv')

y = df['Score']
x = df['timing']
plt.xlabel('Temps en secondes')
plt.ylabel('Score atteint')

#plot.plot(x, y, c = x)
plt.hist2d(x, y)
plt.show()