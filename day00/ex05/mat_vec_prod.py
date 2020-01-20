import numpy as np
from dot import dot

def mat_vec_prod(x, y):
#	if x.size == 0 or y.size == 0:
#		return None
#	if x.shape[1] != y.shape[0]:
#		return None

#	res_n = np.zeros((x.shape[0], 1))
#	for i in range(0,x.shape[0]):
#		res_n[i] = dot(x[i], y.reshape(y.shape[0]))
#	return res_n

	array = []
		#print("here")
		#res_n = np.zeros((x.shape[0], 1))
	for i in range(0,x.shape[0]):
		array2 = []
		array2.append(dot(x[i], y.reshape(y.shape[0])))
		array.append(array2)
	return np.array(array)


W = np.array([
    [ -8, 8, -6, 14, 14, -9, -4],
    [ 2, -11, -2, -11, 14, -2, 14],
    [-13, -2, -5, 3, -8, -4, 13],
    [ 2, 13, -14, -15, -14, -15, 13],
    [ 2, -1, 12, 3, -7, -3, -6]])

WN = np.array([[[1, 2], [1, 2]], [[1,2],[1,2]]])
Y = np.array([2, 14, -13, 5, 12, 4, -19]).reshape((7,1))
X = np.array([0, 15, -9, 7, 12, 3, -21])
print(mat_vec_prod(W, X))
print(mat_vec_prod(W, Y))
