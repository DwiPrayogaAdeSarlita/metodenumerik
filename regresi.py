import numpy as np 

n = int(input('input jumlah pasangan nilai='))
SM = np.zeros((n,n))
x = np.zeros((n))
y = np.zeros((n))

for k in range(0,n):
    print('input x [{}]='.format(k),end="")
    x[k]=float(input())
    print('input y [{}]='.format(k),end="")
    y[k]=float(input())
    SM[k,0]=y[k]

X= float(input('input nilai X yang ingin dicari pasangannya='))

sx,sy,sxx,syx=0.,0.,0.,0.
for i in range(n):
    sx+=x[i]
    sxx+=x[i]**2
    sy+=y[i]
    syx+=y[i]*x[i]

s2x=sx**2
b=(syx-sx*sy)/(n*sxx-s2x)
a=(sy/n)-b*(sx/n)

Y=a+b*X
print("Hasilnya=",Y)