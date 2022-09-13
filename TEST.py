from two_ext import Enc_ext
from translator import alphabet_ext
import time
import numpy as np
import matplotlib.pyplot as plt
Y=[]
for k in range(1,1000):
    X=[]
    for i in range(1000):
        a = np.random.choice(alphabet_ext,k)
        a = "".join(a)
        #print(a)
        start = time.time()
        Enc_ext(a)
        end = time.time()
        T = end-start
        X.append(T)
        print("CT = ", T)
    Y.append(X)
#print(Y)
for i in range(999):
    Y[i] = np.mean(Y[i])
print("Y = ",Y)
ls = [i for i in range(1,1000)]
#print(ls)
plt.scatter(ls,Y)
plt.grid()
plt.show()
# appears linear, O(n) computing time!
