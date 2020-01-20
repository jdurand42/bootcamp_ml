import numpy as np

def variance(x):
	def mean(x):
		if x.size == 0 or isinstance(x, (np.ndarray, np.generic)) == False:
			return None
		#sumed = sum_(x)
		res = 0
		for el in x:
			res += el
		return res / x.size

	if x.size == 0 or isinstance(x, (np.ndarray, np.generic)) == False:
		return None
	return mean((x - mean(x))**2)


X = np.array([0, 15, -9, 7, 12, 3, -21])
print(variance(X))
print(np.var(X))
print(variance(X/2))
print(np.var(X/2))
