#GATE Assignment 2
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

N = 500
x = np.linspace(-5,5, N)

def rectFunction(t):
    y = np.zeros(N)
    for i in range(N):
        if t[i] >= -0.5 and t[i] <= 0.5:
            y[i] = 1
    return y
#Computing the rectangular function
y = rectFunction((5*x)-3)
#Computing the fourier transform
y_fourier = [10*np.mean(y * np.exp(1j * 2 * np.pi * f * x)) for f in x]
#Comparing it with the theoretical result
sincTheoretical = 0.2 * np.exp(-1j * 0.6 * 2 * np.pi * x) * (np.sin((2 * np.pi * x)/10.)/((2 * np.pi * x)/10.))

plt.plot(x,y)
plt.xlabel('$t$')
plt.ylabel('$x(5t-3)$')
plt.grid()
plt.show()

plt.plot(x,np.real(y_fourier), label='Simulation',color='b')
plt.plot(x,np.real(sincTheoretical), label='Theoretical',color='r')
plt.xlim(-5,5)
plt.xlabel('$f$')
plt.ylabel('$X(f)$')
plt.grid()
plt.legend()
plt.show()
