import numpy as np
from mat_vec_prod import mat_vec_prod
from dot import dot

#inverser entre x et y
# M[deb_ligne : fin_ligne , deb_col : fin_col]
def mat_mat_prod(x, y):
	if x.size == 0 or y.size == 0:
		return None
	if x.shape[1] != y.shape[0]:
		return None

	array = []

	buff = []
	for j in range(0,y.shape[0]):
		buff_x = []
		for i in range(0,x.shape[0]):
			buff_x.append(x[i][j])
		buff.append(buff_x)

	for i in range(0, y.shape[0]):
		array.append(mat_vec_prod(np.array(buff), y[i]))
		#print (el * y[i])
		#print (y)
	return (np.array(array))

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

print(mat_mat_prod(W, Z))
print(mat_mat_prod(Z,W))
#mat_mat_prod(Z,W)
# mat x[m] * y[i][p]
