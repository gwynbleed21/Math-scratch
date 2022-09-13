import numpy as np

g = lambda x: x*x-5*x +13
dg = lambda x: 2*x-5
d2g = lambda x: 2

def min(f, df, x_0, L= 100, eps = 0.03125): # MARK 1 ------- requires input L
    a = 1/L
    #print(f"this is {L} and {a}") # checks
    x_k = x_0 -a*df(x_0)
    print(x_k , f(x_k), df(x_k))
    if abs(df(x_k))<= eps:
        return x_k , f(x_k), df(x_k)
    else:
        return min(f,df,x_k, L=L, eps=eps)
#print(min(g,dg,-10,L = 2))

def min2(f, df, d2f, x_0, eps = 0.03125): # MARK 2 ------- requires input d2f
    L2 = abs(d2f(x_0)) # d2f has to be positive, given the function is concave up. abs just incase
    return min(f,df,x_0, L=L2,eps=eps)
print(min2(g,dg,d2g,-100))    # explain explain explain, question

"""THis requires d2f to be bounded from above!!!"""
#TESTS
h = lambda x: np.exp(x*x)
dh = lambda x: 2*x*h(x)
d2h = lambda x: 2*h(x)*(1+2*x*x)  # excedes recursion limit, no bound on L
#print(min(h,dh,-3,L=100))

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

print(min4(g,dg,d2g,-10))
print(min4(h,dh,d2h,-10))   # IT WORKS!!!!!!!