#python program to find transmission coefficiant in quantum tunnelling
import numpy as np
from scipy.integrate import quad
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon  



#parameters and costants
eq = 1.6E-19
E = 2.5E-20  #joule
L = 1E-7
h = 1.0545E-34   #h/2pi
m = 9.1E-31
#potential width
a= L/2-0.2E-7
b= L/2+0.2E-7


#solving the equation to find transmission coefficient
def f(x):
    v = (((x - (L / 2)) ** 2) * (2 / L) ** 2) * eq
    if E < v:
        return math.sqrt(2 * m * (v - E))
    else :
        return 0

y = quad(f,a,b)
T = math.exp((-2 / h) * y[0])
print(f"Transmission coefficient is: {T}")

#potential graph
fig, ax = plt.subplots(figsize=(5,5))
g = np.linspace(-L, 2*L, 1000)
v = (((g - (L / 2)) ** 2) * (2 / L) ** 2) * eq
ax.set_xlim(-1.2 * L, 3 * L)
ax.set_ylim(0,3.2E-19)
ax.plot(g, v, 'b', label="potential V(x)")
plt.title(label= f"Transmission coefficient: {T}",fontsize=10, color="black")
ax.set_xlabel("Distance",fontsize=13)
ax.set_ylabel("Energy",fontsize=13)


#potential integration grph
gg = np.linspace(a, b, 1000)
vv = (((gg - (L / 2)) ** 2) * (2 / L) ** 2) * eq
verts = [(a, 0), *zip(gg, vv), (b, 0)]
poly = Polygon(verts, facecolor='0.8', edgecolor='0.8')
ax.add_patch(poly)


#energy line plot graph
j = np.linspace(-1.2 * L, 3 * L, 1000)
k= np.array([E] * 1000)
ax.plot(j,k,'--', lw=1,label="Energy E")
ax.legend(loc='upper right', fontsize=12)


plt.show()

