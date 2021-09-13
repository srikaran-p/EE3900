#GATE Assignment 1
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert

n= 1000

x = np.linspace(-10,10, n)

#Implementing sinc(x)
x_t = 4*np.sin(2 * np.pi * x)/(2 * np.pi * x)

#Applying Hilbert transform to x(t)
y_t = hilbert(x_t)
h_t = 1/(np.pi * x)

#Computing the Fourier transform
x_fourier = [np.mean(x_t * np.exp(-1j * 2 * np.pi * f * x)) for f in x]
h_fourier = [np.mean(h_t * np.exp(-1j * 2 * np.pi * f * x)) for f in x]
y_fourier = [np.mean(y_t * np.exp(-1j * 2 * np.pi * f * x)) for f in x]

#Plotting the input and output signals
plt.plot(x,x_t, label="$x(t)$")
#np.imag(y_hilbert) returns the transformed signal, while, np.real(y_hilbert) returns the original signal
plt.plot(x,np.imag(y_t), label="$y(t)$")
plt.xlabel("$t$")
plt.legend()
plt.grid()
plt.show()

#Plotting the signals in frequency domain
plt.plot(x, np.real(x_fourier), label="$X(f)$")
plt.plot(x, np.imag(h_fourier), label="$H(f)$")
plt.plot(x, np.real(y_fourier), label="$Y(f)$")
plt.xlabel("$f$")
plt.legend()
plt.grid()
plt.show()
