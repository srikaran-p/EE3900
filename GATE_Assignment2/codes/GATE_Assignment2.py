#GATE Assignment 2
import numpy as np
import matplotlib.pyplot as plt

N = 50000
x = np.linspace(-25,25, N)

def rectFunction(t):
    y = np.zeros(N)
    for i in range(N):
        if t[i] >= -0.5 and t[i] <= 0.5:
            y[i] = 1
    return y
#Computing the rectangular function
y = rectFunction((5*x)-3)
#Computing the fourier transform
y_fourier = [50*np.mean(y * np.exp(-1j * 2 * np.pi * f * x)) for f in x]
#Comparing it with the theoretical result
sincTheoretical = 0.2 * np.exp(-1j * 2 * np.pi * 0.6 * x) * (np.sin((2 * np.pi * x)/10.)/((2 * np.pi * x)/10.))

#Plotting rect(5t-3)
plt.plot(x,y)
plt.xlabel('$t$')
plt.ylabel('$x(5t-3)$')
plt.grid()
plt.xlim(-5,5)
plt.show()

fig1, ax1 = plt.subplots(2,1)
#Plotting the signals of amplitude
ax1[0].plot(x, np.absolute(y_fourier), label="Simulation")
ax1[0].plot(x, np.absolute(sincTheoretical), label="Theoretical")
ax1[0].set_ylabel("$A$")
ax1[0].legend(loc = "best")
ax1[0].grid()

#Plotting the phase
ax1[1].plot(x, np.angle(y_fourier), label="Simulation")
ax1[1].plot(x, np.angle(sincTheoretical), label="Theoretical")
plt.xlabel("$f$")
ax1[1].set_ylabel("$\phi$")
ax1[1].legend(loc = "best")
ax1[1].grid()
plt.show()
