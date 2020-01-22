import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.cm as cm
#from sklearn.metrics import mean_squared_error
from mylinearregression import MyLinearRegression as MyLR

def frange(start, stop=None, step=None):

    if stop == None:
        stop = start + 0.0
        start = 0.0

    if step == None:
        step = 1.0

    while True:
        if step > 0 and start >= stop:
            break
        elif step < 0 and start <= stop:
            break
        yield ("%g" % start) # return float number
        start = start + step

data = pd.read_csv("are_blue_pills_magics.csv")
Xpill = np.array(data['Micrograms']).reshape(-1,1)
Yscore = np.array(data['Score']).reshape(-1,1)
linear_model1 = MyLR(np.array([[89.0], [-12]]))
linear_model2 = MyLR(np.array([[89.0], [-6]]))
linear_model3 = MyLR(np.array([[89.0], [-8]]))
Y_model1 = linear_model1.predict_(Xpill)
#print(Y_model1)
Y_model2 = linear_model2.predict_(Xpill)
#print(Y_model2)
linear_model3.fit_(Xpill, Yscore, 0.001, 2000)
fit_model = linear_model3.predict_(Xpill)
print(fit_model)

#courbe de prediction
plt.scatter(Xpill, Yscore)
plt.plot(Xpill, fit_model, color = "green")
plt.title("Predictions ")
plt.xlabel("Micrograms")
plt.ylabel("Score")
#plt.subplot(131)
plt.show()

#cost function
linear4 = MyLR(np.array([[89.0], [-14]]))
theta0 = 89.0
fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8])
plt.title("Cost for different theta0")
plt.xlabel("theta1")
plt.ylabel("cost (j(theta0, theta1))")
#plt.axis([-14, 20, -3, 140])
n_samples = 6
colors = cm.rainbow(np.linspace(0, 1, n_samples))

for j in range(0, n_samples):
	costs = []
	for theta1 in range(-13, -2): #every curve
		costs.append(linear4.cost_(Xpill, Yscore))
		linear4.theta = np.array([[theta0], [theta1]])
	theta0 += 1
	print(costs)
	plt.plot(range(-13, -2), costs, color = colors[j])
#	print("------")
#plt.margins(0)

axes.set_xlim([-14, -4])
axes.set_ylim([20,140])
plt.show()


#for i in range(-4, -14):
#	plt.scatter(i, )
