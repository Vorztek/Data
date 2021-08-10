import numpy as np
from sklearn.datasets import make_regression
import matplotlib.pyplot as plt


x, y = make_regression(n_samples = 100, n_features= 1, noise = 10)
y = y + abs(y / 2) # ajout du polynomiale
y = y.reshape(y.shape[0], 1)
X = np.hstack((x, np.ones(x.shape)))
X = np.hstack((x ** 2, X)) # ajout du polynomiale

theta = np.random.randn(2,1) # ajout du polynomiale
#print(theta.shape)

def model(X, theta):
    return X.dot(theta)

def cost_function(X, y, theta):
    m = len(y)
    return 1/(2* m) * np.sum((model(X, theta)- y) ** 2)

def grad(X, y, theta):
    m = len(y)
    return 1/m * X.T.dot(model(X, theta) -y)

def gradient_descent(X, y, theta, learning_rate, n_iterations):
    cost_history = np.zeros(n_iterations)
    theta_history = np.zeros((n_iterations, 2))
    for i in range(0, n_iterations):
        theta = theta - learning_rate * grad(X, y, theta)
        cost_history[i] = cost_function(X, y, theta)
        theta_history[i, :] = theta.T


    return theta, cost_history, theta_history

theta_final, cost_history, theta_history = gradient_descent(X, y, theta, learning_rate=0.01, n_iterations= 500)
predictions = model(X, theta_final)
#plt.scatter(x, y)
#plt.plot(x, predictions, c = "r")
#plt.plot(range(300), cost_history)
#plt.show()

# coefficient de determination = r², via la méthode" des moindrees carrés

def coef_determination(y, pred):
    u = ((y - pred)**2).sum()
    v = ((y - y.mean())**2).sum()
    return 1 - u/v

print(coef_determination(y, predictions))
#print(gradient_descent(X, y, theta, learning_rate, n_iterations))
#print(grad(X, y, theta))
#print(cost_function(X, y, theta))












""" plt.scatter(x, y)
plt.plot(x, model(X, theta), c = "orange")
plt.show()
 """
