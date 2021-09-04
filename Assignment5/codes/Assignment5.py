#Assignment 5
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,10,10000)
x_axis = np.zeros((10000,))
def f(x):
    return (4*(x**2)) + (3*x) + 5

plt.plot(x , f(x) , label = "$4x^2 + 3x + 5$")
plt.plot(x , x_axis , label ="$y = 0$")
plt.grid(True)
plt.legend()
plt.ylim(-5,20)
plt.show()
