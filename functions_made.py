

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

