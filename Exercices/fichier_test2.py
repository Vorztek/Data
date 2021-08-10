import numpy as np
from sklearn.datasets import make_regression
import matplotlib.pyplot as plt


x, y = make_regression(n_samples = 100, n_features= 2, noise = 10)
plt.scatter(x[:,0], y)
plt.show()
