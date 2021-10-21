#Quiz 2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import lcapy as lc
from lcapy.discretetime import z

#Computing Inverse Z Transform
Hz = (4*(z**2))/((4*z**2) - 1)
xn = Hz.IZT()
print(xn)

#Plotting h[n]
n = np.arange(10)
posn = 0.5 * (-1/2)**n
negn = 0.5 * (1/2)**n

#Plotting the ROC
fig, ax = plt.subplots(figsize = (6,6))

ax.set_xlim([-3,3])
ax.set_ylim([-3,3])

pole1, = plt.plot(1/2,0, 'rx',label = 'Poles')
pole2, = plt.plot(-1/2,0, 'rx',label = 'Poles')
zero, = plt.plot(0,0, 'ro',label = 'Zeros')

legend = plt.legend(handles =[pole,zero], loc = 'lower right')
fig.gca().add_artist(legend)

circle1 = plt.Circle([0,0],1/2,color = 'w')
fig.gca().add_artist(circle1)

circle2 = plt.Circle([0,0],1,edgecolor = 'black',fill = 0,linestyle = '--')
fig.gca().add_artist(circle2)

patches = mpatches.Patch(color="green", label="ROC")
dotted_line = mlines.Line2D([],[],color = 'black',label='Unit circle')
dotted_line.set_linestyle('--')
plt.legend(handles=[patches,dotted_line], loc = 'upper right')
ax.set_facecolor('xkcd:green')

plt.grid()
plt.xlabel("Re")
plt.ylabel("Im")
plt.show()

plt.stem(np.arange(10), posn+negn, use_line_collection=True)
plt.xlabel('$n$')
plt.ylabel('$h(n)$')
plt.show()
