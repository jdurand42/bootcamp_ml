import pandas as pd
import numpy as np
from mylinearregression import MyLinearRegression as MyLR
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.cm as cm

fig, axs = plt.subplots(3)

data = pd.read_csv("spacecraft_data.csv")
X = np.array(data['Age']).reshape(-1, 1)
print(X.shape)
Y_price = np.array(data['Sell_price']).reshape(-1, 1)
X_thrust = np.array(data['Thrust_power']).reshape(-1, 1)
X_meters = np.array(data['Terameters']).reshape(-1, 1)
myLR_age = MyLR([[1000.0], [-1.0]])
myLR_age.fit_(X, Y_price, alpha = 2.5e-5, n_cycle = 5000)

y_hat = myLR_age.predict_(X)
axs[0].scatter(X, Y_price, color = "purple")
axs[0].plot(X, y_hat, color = "pink")
axs[0].set_title("Sell_price with age")
axs[0].set(xlabel = ("Age"), ylabel = ("Sell_price"))

myLR_thrust = MyLR([[1000.0], [-1.0]])
y_hat_t = myLR_thrust.fit_(X_thrust, Y_price, alpha = 2.5e-5, n_cycle = 5000)
axs[1].scatter(X_thrust, Y_price, color = "purple")
axs[1].plot(X_thrust, y_hat_t, color = "pink")
axs[1].set_title("Sell_price with thrustpower")
axs[1].set(xlabel = ("Thrust_power"), ylabel = ("Sell_price"))
#plt.subplot(132)
myLR_meters = MyLR([[1000.0], [-1.0]])
y_hat_m = myLR_meters.fit_(X_meters, Y_price, alpha = 2.5e-10, n_cycle = 5000)
axs[2].scatter(X_meters, Y_price, color = "purple")
axs[2].plot(X_meters, y_hat_m, color = "pink")
axs[2].set_title("Sell_price with terameters")
axs[2].set(xlabel = ("Terameters"), ylabel = ("Sell_price"))

plt.show()

#print(myLR_age.mse_(X, Y_price))

# 2 part
