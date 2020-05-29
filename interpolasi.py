import numpy as np 
n = int(input('Input jumlah pasangan nilai = '))
SM = np.zeros((n, n))
x = np.zeros((n))
y = np.zeros((n))
for k in range(0, n):
    print('Input x [{}] = '.format(k), end=" ")
    x[k] = float(input())
    print('Input y [{}] = '.format(k), end=" ")
    y[k] = float(input())
    SM[k, 0] = y[k]

X = float(input('Input nilai X yang ingin dicari pasangannya = '))

def faktorial(i):
    fak = 1 
    for k in range(2, i+1, 1):
        fak *= k
    return fak

for k in range(1, n):
    for i in range(0, n-k):
        SM[i, k] = SM[i+1, k-1] - SM[i, k-1]
h = x[1] - x[0]
p = (X - x[0])/h 
jumlah = SM[0, 0]
for i in range(1, n):
    suku = SM[0, i]
    for k in range(0, i):
        suku = suku*(p-k)
    suku = suku/faktorial(i)
    jumlah = jumlah+suku

print('Hasilnya =',jumlah)