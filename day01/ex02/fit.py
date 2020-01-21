import numpy as np
from pred import predict_
from cost_function import cost_
from cost_function import cost_elem_

def fit_(theta, X, Y, alpha = 0.01, n_cycle = 2000):
#	pred = predict_(theta, X)
#	cost_elem = cost_elem_(theta, X, Y)
#	print(pred)
#	print(cost_elem)

	cost = cost_(theta, X, Y)
	previous_cost = 0
	#while cost > 0:
	for i in range(0, n_cycle):
		cost = cost_(theta, X, Y)
	#	if (abs(cost - previous_cost) <= 0.000001):
	#		break ;
		previous_cost = cost
		pred = predict_(theta, X)
		D_theta1 = 1 / X.shape[0] * (alpha * np.sum((pred - Y) * X))
		D_theta0 = 1 / X.shape[0] * (np.sum(pred - Y))
		theta[1] = theta[1] - D_theta1
		theta[0] = theta[0] - D_theta0

	print(cost_(theta, X, Y))
	print(theta)
	#print(D_theta0)
	#print(D_theta1)
	#print(cost_(theta, X, Y))
	# for n iter:
	# L = 0.0001 -> learning rate
	#pred = predict_(new_theta, X)
	#D_theta1 = (-2/m) * np.sum(X * (Y - Y_PRED))
	#D_theta0 = (-2/m) * sum(Y - Y_PRED)
	#Theta[1] = theta[1] - D_theta1
	#Theta[0] = theta[0] - D_theta0
	return theta


X1 = np.array([[0.], [1.], [2.], [3.], [4.]])
theta1 = np.array([[1.], [1.]])
Y1 = np.array([[2.], [6.], [10.], [14.], [18.]])

#X = np.array([[3], [4]])
#theta = np.array([[0], [0]])
#Y = np.array([[1000], [1000]])
#print(cost_(theta, X, Y))
theta1 = fit_(theta1, X1, Y1)
print(predict_(theta1, X1))

X2 = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8.,
80.]])
Y2 = np.array([[19.6], [-2.8], [-25.2], [-47.6]])
theta2 = np.array([[42.], [1.], [1.], [1.]])
theta2 = fit_(theta2, X2, Y2, alpha = 0.0005, n_cycle=42000)
print(predict_(theta2, X2))
