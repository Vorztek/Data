import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



df = pd.read_csv(r'C:\Users\vion1\Ele\Engie\Exercices\ML\tetris\dataset.csv')

y = df['Score']
x = df['timing']


#pd.DataFrame({"A": [x], "B": [y]}).to_numpy()

plt.scatter(x, y)
plt.show()
