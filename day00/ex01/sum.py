import numpy as np

def sum_(x ,f):
	if x.size == 0:
		return None
	res = 0
	for el in x:
		res += float(f(el))
	#print(res)
	return res

X = np.array([0, 15, -9, 7, 12, 3, -21])
sum_(X, lambda x:x**2)
