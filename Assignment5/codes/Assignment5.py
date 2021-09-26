#Assignment 5_2
import numpy as np
import math
import matplotlib.pyplot as plt
from numpy import linalg

x = np.linspace(-10,10, n)
#Equation: 4x^2 + 3x + 5

V = np.array(([4, 0],[0, 0]))
u = np.array(([3,-3]))
f = 5

#Finding the eigenvalues and eigenvectors
D_vec,P = linalg.eig(V)
D = np.diag(D_vec)

#Computing the value of eta
eta = u @ P[:,1]
foc = -(2 * eta)/D_vec[0]

#Generating the points for the parabola
x_para = (x**2/foc)/4

cA = np.block([[u+eta*p],[V]])
cb = np.block([[-f],[(eta*p-u).reshape(-1,1)]])
c = linalg.lstsq(cA,cb,rcond=None)[0]
c = c.flatten()

xStandardparab = np.vstack((x,x_para))
xActualparab = P@xStandardparab + c[:,np.newaxis]

#Plotting the standard and actual parabola
plt.plot(xStandardparab[0,:],xStandardparab[1,:],label='Standard Parabola',color='b')
plt.plot(xActualparab[0,:],xActualparab[1,:],label='$4x^2 + 3x + 5$',color='r')
plt.plot([i for i in range(-10,10)] , [0 for i in range(-10,10)] , 'k-',label = "x-axis" )

plt.legend(loc='best')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid()
plt.show()
