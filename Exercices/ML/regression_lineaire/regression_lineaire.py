import numpy as np
from sklearn.datasets import make_regression
import matplotlib.pyplot as plt

x, y = make_regression(n_samples = 100, n_features= 2, noise = 10)
#plt.scatter(x[:,0], y)
#plt.show()

y = y.reshape(y.shape[0], 1)
X = np.hstack((x, np.ones((x.shape[0], 1))))

theta = np.random.randn(3,1)
#print(theta.shape)

def model(X, theta):
    return X.dot(theta)

def cost_function(X, y, theta):
    m = len(y)
    return 1/(2* m) * np.sum((model(X, theta)- y) ** 2)

def grad(X, y, theta):
    m = len(y)
    return 1/m * X.T.dot(model(X, theta) -y)
    
n_iterations= 500
def gradient_descent(X, y, theta, learning_rate, n_iterations):
    cost_history = np.zeros(n_iterations)
    
    for i in range(0, 500):
        theta = theta - learning_rate * grad(X, y, theta)
        cost_history[i] = cost_function(X, y, theta)
        

    return theta, cost_history, 


theta_final, cost_history, theta_history = gradient_descent(X, y, theta, learning_rate=0.01, n_iterations= 500)
predictions = model(X, theta_final)

#plt.scatter(x[:,1], y)
#plt.scatter(x[:,1], predictions, c = "r")
plt.scatter(x, y)
for i in range(500):
    plt.plot(x, model(X, theta_history[i]))
    plt.show()
#plt.plot(range(n_iterations), cost_history) # pour le cost history ou courbe d'apprentissage
#plt.show()

# coefficient de determination = r², via la méthode" des moindrees carrés

def coef_determination(y, pred):
    u = ((y - pred)**2).sum()
    v = ((y - y.mean())**2).sum()
    return 1 - u/v

#print(coef_determination(y, predictions))
#print(gradient_descent(X, y, theta, learning_rate, n_iterations))
#print(grad(X, y, theta))
#print(cost_function(X, y, theta))












""" plt.scatter(x, y)
plt.plot(x, model(X, theta), c = "orange")
plt.show()
 """
