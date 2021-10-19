#Quiz 1
import numpy as np
import matplotlib.pyplot as plt

n = np.arange(0,25,1)
exp = np.exp(1j * n)

fig1, ax1 = plt.subplots(2,1)
#Plotting the signals of amplitude
ax1[0].stem(n, np.absolute(exp), label="$x[n]$", use_line_collection=True)
ax1[0].set_ylabel("$A$")
ax1[0].legend(loc = "best")
ax1[0].grid()

#Plotting the phase
ax1[1].stem(n, np.angle(exp), label="$x[n]$", use_line_collection=True)
plt.xlabel("$n$")
ax1[1].set_ylabel("$\phi$")
ax1[1].legend(loc = "best")
ax1[1].grid()
plt.show()
