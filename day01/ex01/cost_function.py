import numpy as np
from pred import predict_

def cost_elem_(theta, X, Y):
	"""
    Description:
        Calculates all the elements 0.5*M*(y_pred - y)^2 of the cost
function.
    Args:
        theta: has to be a numpy.ndarray, a vector of dimension (number of
features + 1, 1).
        X: has to be a numpy.ndarray, a matrix of dimension (number of
training examples, number of features).
    Returns:
        J_elem: numpy.ndarray, a vector of dimension (number of the training
examples,1).
        None if there is a dimension matching problem between X, Y or theta.
    Raises:
        This function should not raise any Exception.
	"""
	y_hat = predict_(theta, X)
	if len(y_hat) == 0 or Y.shape[0] != X.shape[0] or Y.shape[1] != 1:
		print("dimensions incompatibles")
		return None
	print(y_hat)
	array = []
	m = X.shape[0]
	n = X.shape[1]
	for i in range(0, m):
		array.append((y_hat[i] - Y[i])**2) # mean(predicted - real ^ 2)
	for i in range(0,m):
		array[i] = array[i] / (2 * m)
	return np.array(array)

def cost_(theta, X, Y):
		return np.sum(cost_elem_(theta, X, Y))


X1 = np.array([[0.], [1.], [2.], [3.], [4.]])
theta1 = np.array([[2.], [4.]])
Y1 = np.array([[2.], [7.], [12.], [17.], [22.]])
print(cost_elem_(theta1, X1, Y1))
print(cost_(theta1, X1, Y1))
# array([[0.], [0.1], [0.4], [0.9], [1.6]])
