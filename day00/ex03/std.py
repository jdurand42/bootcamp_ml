import numpy as np
from variance import variance
import math

def std(x):
	if x.size == 0 or isinstance(x, (np.ndarray, np.generic)) == False:
		return None
	return math.sqrt(variance(x))

X = np.array([0, 15, -9, 7, 12, 3, -21])
print(std(X))
