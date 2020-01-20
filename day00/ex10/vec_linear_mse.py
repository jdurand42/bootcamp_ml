import numpy as np
from dot import dot

def vec_linear_mse(x, y, theta):
	def checks(x, y, theta):
		if y.size == 0 or isinstance(y, (np.ndarray, np.generic)) == False:
			return None
		if x.size == 0 or isinstance(x, (np.ndarray, np.generic)) == False:
			return None
		if theta.size == 0:
			return None
		if y.shape[0] != x.shape[0] or x.shape[1] != theta.shape[0]:
			return None
		return "GOOD"
	if checks(x, y, theta) == None:
		return None
		
	m = x.shape[0]
	return dot(x.dot(theta) - y, x.dot(theta) - y) / m

X = np.array([
    [ -6, -7, -9],
        [ 13, -2, 14],
        [ -7, 14, -1],
        [ -8, -4, 6],
        [ -5, -9, 6],
        [ 1, -5, 11],
        [ 9, -11, 8]])
Y = np.array([2, 14, -13, 5, 12, 4, -19])
Z = np.array([3,0.5,-6])
print(vec_linear_mse(X, Y, Z))
W = np.array([0,0,0])
print(vec_linear_mse(X, Y, W))
