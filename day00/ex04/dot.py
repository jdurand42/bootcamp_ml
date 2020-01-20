import numpy as np

def dot(x, y):
	if x.size == 0 or isinstance(x, (np.ndarray, np.generic)) == False:
		return None
	if y.size == 0 or isinstance(y, (np.ndarray, np.generic)) == False:
		return None
	if y.size != x.size:
		return None
#	doted = x * y

	res = 0
	for el in x * y:
		res +=  el
	return(float(res))

X = np.array([0, 15, -9, 7, 12, 3, -21])
Y = np.array([2, 14, -13, 5, 12, 4, -19])
print(dot(X, Y))
