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
		array.append(theta[0])
		for j in range(1, n + 1):
			array[i] = array[i] + theta[j] * X[i][j - 1]
	return np.array(array)
