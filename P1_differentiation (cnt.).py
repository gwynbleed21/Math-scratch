import numpy as np
import matplotlib.pyplot as plt

def min3(f, df, x_0, x_e=1, eps=0.03125):
    a = (x_0 - x_e) / (df(x_0) - df(x_e))
    x_k = x_0 - a * df(x_0)
    if abs(df(x_k)) <= eps:
        return [x_k, f(x_k), df(x_k)]
    else:
        return min3(f, df, x_k, x_e=x_0, eps=eps)

def min4(f, df, d2f, x_0, eps=0.03125):
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
    return min3(f, df, x_k, x_e=x_0, eps=eps)

def der(f, h=0.03125):
    """
    Defined this way this returns a function and so is compatible with other algorithms that require functions as inputs
    such as min() or root().
    :param f: input function
    :param h: step size, determines accuracy
    :return: approxiamation to the derivative of f
    """
    df = lambda x: (f(x + h) - f(x)) / h
    return df
#----------------------------------------------------------------------------------------------------------------------

def min5(f,x_0, eps=0.03125, h = 0.03125):
    """
    Algorithm to find the minimum of functions, based on min4(), min3() and der(). Internally approxiamates derivatives.
    :param f: the input function
    :param x_0: inital point
    :param eps: tolerance interval
    :param h: stepsize for derivative aproxiamation
    :return: [x_min, f(x_min) , f'(x_min)]              --------f'(x_min) should be zero, way to check how well it works
    the output is a list such that each element may be easily accessed.
    """
    df = der(f,h=h)
    d2f = der(df,h=h)  # already uses the approx as per question 4
    return min4(f,df,d2f, x_0,eps=eps)


z = lambda x: np.exp(x*x)

#print(min5(z,-1)) # IT works!!!!!!
#print(min5(z,-1, eps = 0.00000001,h = 0.0000001))






"""
-------------------Question---------------------------------------------------------------------------------------------
"""
g = lambda x: (np.tanh(x)*np.cos(np.exp(x*x)))/((np.log(x*x+1)*np.exp(-x)+4)**(1/3))
MIN = min5(g,0.9, eps = 0.00000001,h = 0.0000001)
# if we start at 0.6 the algorith goes left and gets traped at the maximum, x = 0.3999. The alg could be bounded.
print(MIN)

X = np.linspace(0,3,1000)
plt.plot(X,g(X))
plt.scatter(MIN[0],MIN[1], c ="red")
plt.show()

# could use the roots() function on the approxiamation to the derivative

