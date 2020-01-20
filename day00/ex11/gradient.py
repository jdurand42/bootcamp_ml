import numpy as np
from dot import dot

def gradient(x, y, theta):
	nabla_j = []

	for j in range(0, x.shape[1]):
		res = 0
		dot_l = []
		for i in range(x.shape[0]):
			res += dot(theta, x[i]) - y[i] * x[i]
		nabla_j.append(res[j] / x.shape[0])
	print(np.array(nabla_j))
			#res += (dot(dot(theta, x[i]) - y[i], x[i]))
		#nabla_j.append(res / x.shape[0])
	#return np.array(nabla_j)

# mean -> sum(dot(dot(theta, xi) - y[i], x[i])**j)
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
gradient(X, Y, Z)
