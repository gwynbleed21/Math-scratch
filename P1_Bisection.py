import matplotlib.pyplot as plt
import numpy as np
h = lambda x: x*x-2

X = np.linspace(-10,10,1000)

plt.plot(X,h(X))
plt.grid()
plt.axhline(color = 'black')
#plt.show()

def root(a,b,g,eps=0.03125): #Q1  2^(-5)=0.03125
    """
    This solves for a root between a and b. For this one must have a rough idea of where the root is,
     initial interval(a,b) should contain only one root. Else it may  not work or give only one solution.
      Only for explicit functions. Avoid intervals on which division by 0 is possible.
     """
    m = (a+b)/2
    #print(m,g(m))
    #print(abs(g(m)))
    if abs(g(m)) <= eps: # number of iterations, TO Do
        return m, g(m)
    elif g(a)*(-g(m))<0: # same sign
        return root(m,b,g, eps = eps)
    elif g(a)*(-g(m))>0: # opposite signs
        return root(a, m, g, eps = eps)



z = lambda x: (x-1)/(x+1)
print(root(0,3,z,eps=0.001))

f = lambda x: 2*x*np.exp(x*x) # Q2 ____ run sever times with different a, b, eps
print(root(-4,1,f,eps = 0.001))
