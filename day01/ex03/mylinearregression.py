import numpy as np

class MyLinearRegression(object):
	def __init__(self, theta):
		self.theta = np.array(theta)
	#	return self
	def cost_elem_(self, X, Y):
		y_hat = self.predict_(X)
		if len(y_hat) == 0 or Y.shape[0] != X.shape[0] or Y.shape[1] != 1:
			print("dimensions incompatibles")
			return None
		array = []
		m = X.shape[0]
		n = X.shape[1]
		for i in range(0, m):
			array.append((y_hat[i] - Y[i])**2)
		for i in range(0,m):
			array[i] = array[i] / (2 * m)
		return np.array(array)

	def cost_(self, X, Y):
			return float(np.sum(self.cost_elem_(X, Y)))
			#res = 0
			#for el in cost_elem:
			#	res += el
			#return float(res)

	def predict_(self, X):
		m = X.shape[0]
		n = X.shape[1]
		if self.theta.shape[1] != 1 or self.theta.shape[0] != n + 1:
			print("dimensions incompatibles")
			return None
		array = []
		for i in range(0, m):
			array.append(self.theta[0])
			for j in range(1, n + 1):
				array[i] = array[i] + self.theta[j] * X[i][j - 1]
		return np.array(array)

	def fit_(self, X, Y, alpha = 0.01, n_cycle = 2000):
		#previous_cost = 0
		for i in range(0, n_cycle):
		#	cost = self.cost_(X, Y)
			pred = self.predict_(X)
			D_theta1 = 1 / X.shape[0] * (alpha * np.sum((pred - Y) * X))
			D_theta0 = 1 / X.shape[0] * (np.sum(pred - Y))
			self.theta[1] = self.theta[1] - D_theta1
			self.theta[0] = self.theta[0] - D_theta0
		return self.theta

X = np.array([[1., 1., 2., 3.], [5., 8., 13., 21.], [34., 55., 89.,
144.]])
Y = np.array([[23.], [48.], [218.]])
richard = MyLinearRegression([[1.], [1.], [1.], [1.], [1]])
print(type(richard))
mylr = MyLinearRegression([[1.], [1.], [1.], [1.], [1]])
print(mylr.predict_(X))
print(mylr.fit_(X, Y, alpha = 1.6e-4, n_cycle=200000))
print(mylr.theta)
print(mylr.predict_(X))
print(mylr.cost_elem_(X, Y))
