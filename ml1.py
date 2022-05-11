import numpy as np
import matplotlib.pyplot as plt

x = np.array([10,9,2,15,10,16,11,16])
y = np.array([95,80,10,50,45,98,38,93])

plt.scatter(x, y)
plt.plot(x, y)
plt.show()

n = np.size(x)

mx = np.mean(x)
my = np.mean(y)

Sxy = np.sum(x*y) - n*mx*my
Sxx = np.sum(x*x) - n*mx*mx

b1 = Sxy/Sxx
b0 = my - b1*mx

print(f"Equation of line is: y = {b0} + {b1}x", end='')

y_pred = b0 + b1*x
plt.scatter(x, y)
plt.plot(x, y_pred)

plt.xlabel('x')
plt.ylabel('y_pred')

plt.show()