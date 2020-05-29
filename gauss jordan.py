import numpy as np 
def gj(a,b):
    a = np.array(a,float)
    b = np.array(b,float)
    n = len(b)
    for k in range(n):
        if np.fabs(a[k,k])<1.0e-12:
            for i in range(k+1,n):
                if np.fabs(a[i,k])>np.fabs(a[k,k]):
                    for j in range(k,n):
                        a[k,j],a[i,j]=a[i,j], a[k,j]
                    b[k],b[i]=b[i],b[k]
                    break
            pivot = a[k,k]
            for j in range(k,n):
                a[k,j]=a[k,j]/pivot
            b[k]=b[k]/pivot
            for i in range(n):
                if i == k or a[i,k]==0:
                    continue
                factor = a[i,k]
                for j in range(k,n):
                    a[i,j]=a[i,j]-factor*a[k,j]
                b[i]=b[i]-factor*b[k]

    return b,a

a=[[0,2,0,1],[2,2,3,2],[4,-3,0,1],[6,1,-6,-5]]
b=[0,-2,-7,6]

X,A = gj(a,b)

print("Solusi Persamaan:")
print(X)
print("Matriks A yang baru:")
print(A)