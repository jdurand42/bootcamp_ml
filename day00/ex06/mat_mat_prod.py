import numpy as np
from mat_vec_prod import mat_vec_prod
from dot import dot


# M[deb_ligne : fin_ligne , deb_col : fin_col]
def mat_mat_prod(x, y):
	if x.size == 0 or y.size == 0:
		return None
	if x.shape[1] != y.shape[0]:
		return None
	#print(np.array(x[0:x.shape[1]], y[n][0:y.shape[1]]))
	res_n = np.zeros((x.shape[0], y.shape[1]))
	print(res_n)
	buff_mat = np.zeros((x.shape[0],))
	for i in range(0,x.shape[0]):
		buff_mat[i] = x[i][0]
		print(buff_mat)
		for j in range(0,y.shape[0]):
			print(y[j])
	#print(res_n)


# i = 0, j =

W = np.array([
    [ -8, 8, -6, 14, 14, -9, -4],
    [ 2, -11, -2, -11, 14, -2, 14], #x[1][0] * y[0][1]
    [-13, -2, -5, 3, -8, -4, 13],
    [ 2, 13, -14, -15, -14, -15, 13],
    [ 2, -1, 12, 3, -7, -3, -6]])

Z = np.array([
    [-6, -1, -8, 7, -8],
        [ 7, 4, 0, -10, -10],
        [ 7, -13, 2, 2, -11],
        [ 3, 14, 7, 7, -4],
        [ -1, -3, -8, -4, -14],
        [ 9, -14, 9, 12, -7],
        [ -9, -4, -10, -3, 6]])

# res[0][0] = (-8, 2, -13, 2, 2) dot (-6, -1, -8, 7, -8)

mat_mat_prod(W, Z)
#mat_mat_prod(Z,W)
# mat x[m] * y[i][p]
