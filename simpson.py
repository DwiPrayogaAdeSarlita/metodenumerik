import numpy as np 
import math

n = int(input('input jumlah pasangan nilai:'))
x = np.zeros((n))
y = np.zeros((n))

for k in range(0,n):
    print('input x[{}]='.format(k),end="")
    x[k]=float(input())
    print('input y[{}]='.format(k),end="")
    y[k]=float(input())

h=x[1]-x[0]
integrasi=y[0]+y[n-1]
jumlah=0
for i in range(1,n-1):
    if(i%2==1):
        jumlah=jumlah+2*y[i]
    else:
        jumlah=jumlah+3*y[i]

integrasi=math.pi*(h/8)*(integrasi+jumlah)
print('hasilnya=',integrasi)