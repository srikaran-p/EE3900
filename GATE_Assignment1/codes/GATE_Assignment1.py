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
x_fourier = np.array([20*np.mean(x_t * np.exp(-1j * 2 * np.pi * f * x)) for f in x])
h_fourier = np.array([20*np.mean(h_t * np.exp(-1j * 2 * np.pi * f * x)) for f in x])
y_fourier = x_fourier * h_fourier

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
plt.xlabel("$f$")
plt.legend()
plt.grid()
plt.show()

fig1, ax1 = plt.subplots(2,1)
ax1[0].plot(x, np.absolute(h_fourier), label="$H(f)$")
ax1[0].set_ylabel("$A$")
ax1[0].legend()
ax1[0].grid()

ax1[1].plot(x, np.angle(h_fourier), label="$H(f)$")
plt.xlabel("$f$")
ax1[1].set_ylabel("$\phi$")
ax1[1].legend()
ax1[1].grid()
plt.show()

fig, ax = plt.subplots(2,1)
#Plotting the signals of amplitude
ax[0].plot(x, np.absolute(y_fourier), label="$Y(f)$")
ax[0].set_ylabel("$A$")
ax[0].legend()
ax[0].grid()

for i in range(len(y_fourier)):
    if abs(np.imag(y_fourier[i])) < 0.01:
        y_fourier[i] = 0
    else:
        if np.imag(y_fourier[i]) < 0:
            y_fourier[i] = -1j
        elif np.imag(y_fourier[i]) > 0:
            y_fourier[i] = 1j
    y_fourier[i] = 0 + (1j * np.imag(y_fourier[i]))

#Plotting the phase
ax[1].plot(x, np.angle(y_fourier), label="$Y(f)$")
plt.xlabel("$f$")
ax[1].set_ylabel("$\phi$")
ax[1].legend()
ax[1].grid()
plt.show()
