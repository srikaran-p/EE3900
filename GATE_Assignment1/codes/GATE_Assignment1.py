#GATE Assignment 1
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert

x = np.arange(0.1, 10, 0.1)
#Implementing sinc(x)
y = 4*np.sin(2 * np.pi * x)/(2 * np.pi * x)

#Applying Hilbert transform to x(t)
y_hilbert = hilbert(y)

plt.plot(x,y, label="$x(t)$")
#np.imag(y_hilbert) returns the transformed signal, while, np.real(y_hilbert) returns the original signal
plt.plot(x,np.imag(y_hilbert), label="$y(t)$")
plt.xlabel("$t$")
plt.legend()
plt.show()
