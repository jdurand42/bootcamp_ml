import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
#from sklearn.metrics import mean_squared_error
from mylinearregression import MyLinearRegression as MyLR

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

plt.scatter(Xpill, Yscore)
plt.plot(Xpill, fit_model)
plt.title("Predictions ")
plt.xlabel("Micrograms")
plt.ylabel("Score")
plt.show()

for i in range(-4, -14):
	plt.scatter(i, ) 
