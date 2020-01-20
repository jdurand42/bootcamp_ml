import numpy as np
from mean import mean

def mse(y, y_hat):
	if y.size == 0 or isinstance(y, (np.ndarray, np.generic)) == False:
		return None
	if y_hat.size == 0 or isinstance(y_hat, (np.ndarray, np.generic)) == False:
		return None
	if y.shape != y_hat.shape:
		return None

	res = 0
	res_n = np.zeros(y.shape)
	for i in range(y.size):
		res_n[i] += (y_hat[i] - y[i])**2
	return mean(res_n)

#X = np.array([0, 15, -9, 7, 12, 3, -21])
#Y = np.array([2, 14, -13, 5, 12, 4, -19])
#print(mse(X, Y))
#print(mse(X, X
#))
