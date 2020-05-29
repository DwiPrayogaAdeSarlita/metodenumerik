import numpy as np

n = int(input("input jumlah pasangan nilai:"))
x = np.zeros((n))
y = np.zeros((n))

for k in range(0,n):
    print("input x[{}]=".format(k),end="")
    x[k]=float(input())
    print('input y[{}]='.format(k),end="")
    y[k] = float(input())

h = x[1] - x[0]
jumlah = 0
for i in range(1,n-1):
    jumlah +=2*y[i]

integrasi = (h/2)*(y[0]+jumlah+y[n-1])
print("Hasilnya =", integrasi)