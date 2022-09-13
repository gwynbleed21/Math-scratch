import numpy as np
import matplotlib.pyplot as plt
def min3(f, df, x_0, x_e = 1, eps = 0.03125):
    a = (x_0-x_e)/(df(x_0)-df(x_e))
    x_k = x_0 -a*df(x_0)
    if abs(df(x_k))<= eps:
        return x_k , f(x_k), df(x_k)
    else:
        return min3(f,df, x_k, x_e = x_0, eps=eps)
def min4(f, df,d2f, x_0, eps = 0.03125):
    """
    requires min3()
    :param f: input function to compute the minimum of.
    :param df: Derivative of f
    :param d2f: Second derivative of f-for initial condition. can be replaced with a number(change code line 1)
     initial step a = a/d2f(x_0)
    :param x_0: initial point from which approx starts.
    :param eps: the tolerance interval
    :return: x_min, f(x_min) , f'(x_min)              --------f'(x_min) should be zero, way to check how well it works
    """
    a = 1 / abs(d2f(x_0))  # compute the first step before iteration x_(k-1) is required i.e. x_e
    x_k = x_0 - a * df(x_0)
    return min3(f,df, x_k, x_e = x_0, eps=eps)

g = lambda x: x*x
def der(f,h=0.03125):
    """
    Defined this way this returns a function and so is compatible with other algorithms that require functions as inputs
    such as min() or root().
    :param f: input function
    :param h: step size, determines accuracy
    :return: approxiamation to the derivative of f
    """
    df = lambda x: (f(x+h)-f(x))/h
    return df

dg = der(g)

print(dg(4))

z = lambda x: np.exp(x*x)
dz = lambda x: 2*x*z(x)
"""
----------------------------------------PLOTS------------------------------------------------------------------------
"""
X = np.linspace(-1.5,1.5,10000) # this function grows exponentially to x^2 so thake small inteval
fig, ax1 = plt.subplots()
ax1.plot(X,der(z,h=0.1)(X), c = "blue" , label = "h=0.1")
ax1.plot(X,der(z,h=0.01)(X), c = "brown", label = "h=0.01")
ax1.plot(X,der(z,h=0.001)(X), c = "purple", label = "h=0.001")
ax1.plot(X,dz(X),c="black", label = "f'(x)")
ax1.plot(X,z(X), c= "purple", label = "f(x)")
ax1.legend()
#ax1.set_aspect("equal")
ax1.grid()
#plt.show()
"""
------------------------------------END of plotting---------------------------------------------------------------------
"""

for i in range(1,11):
    H = 0.1**i
    Dz = der(z,H)
    print(f" h = {H} --- f'(1)={Dz(1)} --- f'(2)={Dz(2)} \n Error1 = {abs(Dz(1)-dz(1))} \n Error2 = {abs(Dz(2)-dz(2))}")
    #the error can increase due to round uo errors for too small values of h. h= 1E(-8) gave the smallest error

