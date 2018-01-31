import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
from Duplex import Duplex
from Duplex import Loader



np.random.seed(12345678)

x = np.random.random(10)

y = np.random.random(10)

slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

print("r-squared:", r_value**2)

plt.plot(x, y, 'o', label='original data')
plt.plot(x, intercept + slope * x, 'r', label='fitted line')
plt.legend()
plt.show()


plt.cla()


StockLoader = Loader()

path = r"AAPL.csv"

StockDuplex = StockLoader.loadDuplexFromFile(path, 0, 5)
x = np.array(StockDuplex.index)
y = np.array(StockDuplex.second)


slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

print("r-squared:", r_value**2)

plt.plot(x, y, 'o', label='original data')
plt.plot(x, intercept + slope * x, 'r', label="fitted line")
plt.legend()
plt.show()




