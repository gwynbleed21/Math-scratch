import numpy as np
import matplotlib.pyplot as plt
import functions_made as fm  # import the functions made in this project


B=  0.9 #beta
N= 17.3*(10**6)
g=   1/2 #gamma

DI = lambda I: (B*(1-I/N)-g)*I

#X = np.linspace(-10**7,10**7,10**8)
#plt.plot(X,DI(X))
#plt.show()
"""
this function is concave down thus to find it's maximum we find the minimum of -DI and the roots of DI.
One root is to the left of the vertex and one to the right thus find the vertex first.
"""

Y = lambda x: -1*DI(x)
V = fm.min5(Y,0,eps=0.000000001,h=0.00000001)
print(V)
Root1 = fm.root(V[0],V[0]*10,DI)
Root2 = fm.root(-10*6,V[0],DI)
print(Root1, Root2)