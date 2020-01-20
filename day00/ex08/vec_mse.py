import numpy as np
from mean import mean
from dot import dot

def vec_mse(y, y_hat):
	if y.size == 0 or isinstance(y, (np.ndarray, np.generic)) == False:
		return None
	if y_hat.size == 0 or isinstance(y_hat, (np.ndarray, np.generic)) == False:
		return None
	if y.shape != y_hat.shape:
		return None

	return dot(y_hat - y, y_hat - y) / y.size

X = np.array([0, 15, -9, 7, 12, 3, -21])
Y = np.array([2, 14, -13, 5, 12, 4, -19])
print(vec_mse(X, Y))
print(vec_mse(X, X))
