import numpy as np

users = np.array([[25, 5, 3], [30, 2, 5], [22, 6, 1], [40, 1, 10]])

weights = np.array([[0.2, 0.4], [0.5, 0.1], [1.0, 0.3]])

bias = np.array([0.5, -0.2])

Z = users @ weights + bias


def ReLU(x):
    hasil = np.maximum(0, x)
    return hasil


print(Z)
print(ReLU(Z))
