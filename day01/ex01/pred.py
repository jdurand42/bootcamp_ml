import numpy as np

# sum dot(theta[j], x[j])
def predict_(theta, X):
	"""
    Description:
        Prediction of output using the hypothesis function (linear model).
    Args:
        theta: has to be a numpy.ndarray, a vector of dimension (number of
features + 1, 1).
        X: has to be a numpy.ndarray, a matrix of dimension (number of
training examples, number of features).
    Returns:
        pred: numpy.ndarray, a vector of dimension (number of the training
examples,1).
        None if X does not match the dimension of theta.
    Raises:
        This function should not raise any Exception.
    """
#	print(X.shape)
#	print(theta.shape)
	m = X.shape[0]
	n = X.shape[1]
	if theta.shape[1] != 1 or theta.shape[0] != n + 1:
		print("dimensions incompatibles")
		return None
	array = []
	for i in range(0, m): # grosse boucle
		#print(theta[0])
		array.append(theta[0])
		for j in range(1, n + 1):
			#print(j)
	#		print(theta[j] * X[i][j - 1])
			array[i] = array[i] + theta[j] * X[i][j - 1]
	return np.array(array)


#X1 = np.array([[0.], [1.], [2.], [3.], [4.]])
#theta1 = np.array([[2.], [4.]])
#print(predict_(theta1, X1))
#X2 = np.array([[1], [2], [3], [5], [8]])
#theta2 = np.array([[2.]])
#print(predict_(theta2, X2))
#X3 = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8.,
#80.]])
#theta3 = np.array([[0.05], [1.], [1.], [1.]])
#print(predict_(theta3, X3))
# X-> 	[0] theta ->	[2] (2, 1)
#		[1]				[4]
#		[2]
#		[3]		[0 * 4 + 2][1 * 4 + 2][2 * 4 + 2][3 * 4 + 2][4 * 4 + 2]
#				2 6 10 14 18
#		[4]		[4][16]
#(5, 1) N     -->[0][2][4][6][8]
#		N + 1 -->[0][4][8][12][16]
