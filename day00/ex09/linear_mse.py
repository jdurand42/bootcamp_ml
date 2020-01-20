import numpy as np
from mean import mean
from dot import dot

def linear_mse(x, y, theta):
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

	res = 0
	for i in range(0, x.shape[0]):
		res += (dot(theta, x[i]) - y[i])**2
	return (res / x.shape[0]) #x.shape[0] --> m
	#mean(dot(theta, x[i]) - y[i])**2)

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
print(linear_mse(X, Y, Z))
W = np.array([0,0,0])
print(linear_mse(X, Y, W))
