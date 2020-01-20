import numpy as np

def mean(x):
	if x.size == 0 or isinstance(x, (np.ndarray, np.generic)) == False:
		return None
	#sumed = sum_(x)
	res = 0
	for el in x:
		res += el
	return res / x.size

#X = np.array([0, 15, -9, 7, 12, 3, -21])
#print(mean(X**2))
