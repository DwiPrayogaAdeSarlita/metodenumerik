import numpy as np

def f(x):
    return(x/3)**2-np.sin(x)-3

err = 10**(-14)
x=np.zeros(20)
x[0]=1
x[1]=8

for n in range(1,18):
    x[n+1]=x[n]-f(x[n])*(x[n]-x[n-1])/(f(x[n])-f(x[n-1]))
    print(n+1,x[n+1],f(x[n+1]))
    if abs(f(x[n]))<err:
        break