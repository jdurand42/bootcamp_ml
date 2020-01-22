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
			res = 0
			for el in self.cost_elem_(X, Y):
				res += el
			return float(res)

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

	def fit_(self, X, Y, alpha = 0.01, n_cycle = 2000, theta0_constant = False):
		#previous_cost = 0
		for i in range(0, n_cycle):
		#	cost = self.cost_(X, Y)
			pred = self.predict_(X)
			D_theta1 = 1 / X.shape[0] * (alpha * np.sum((pred - Y) * X))
			self.theta[1] = self.theta[1] - D_theta1
			if theta0_constant == False:
				D_theta0 = 1 / X.shape[0] * (np.sum(pred - Y))
				self.theta[0] = self.theta[0] - D_theta0
		return self.theta

	def mean(self, x):
		if x.size == 0 or isinstance(x, (np.ndarray, np.generic)) == False:
			return None
		#sumed = sum_(x)
		res = 0
		for el in x:
			res += el
		return res / x.size

	def mse_(self, y, y_hat):
		if y.size == 0 or isinstance(y, (np.ndarray, np.generic)) == False:
			return None
		if y_hat.size == 0 or isinstance(y_hat, (np.ndarray, np.generic)) == False:
			return None
		if y.shape != y_hat.shape:
			return None
		res_n = np.zeros(y.shape)
		for i in range(y.size):
			res_n[i] += (y_hat[i] - y[i])**2
		return self.mean(res_n)
