import math
def f(x):
    return math.exp(x)-5*x**2

a = int(input("Masukkan nilai batas bawah = "))
b = int(input("Masukkan nilai batas atas = "))
e = float(input("Masukkan nilai toleransi = "))
N = int(input("Masukkan jumlah iterasi = "))
iterasi = 0

print('________________________________')
print('c                       f(c)')
print('________________________________')
while True:
    iterasi += 1
    c = (a+b)/2
    if f(a)*f(c)<0:
        b = c
    else:
        a = c
    print('{:7.5f} \t {:+15.10f}'.format(c, f(c)))
    if abs(f(c)) < e or iterasi >= N:
        break
print('________________________________')