import numpy as np

#inialisasi matriks argument
A = np.array([[0,2,0,1,0],[2,2,3,2,-2],[4,-3,0,1,-7],[6,1,-6,-5,6]])
print(A)

#metode eliminasi gauss
n = len(A)
for k in range(0,n-1):
    if A[k,k]==0:
        for s in range(0,n+1):
            v=A[k,s]
            u=A[k+1,s]
            A[k,s]=u
            A[k+1,s]=v
    for i in range(k+1,n):
        m=A[i,k]/A[k,k]
        for j in range(0,n+1):
            A[i,j]=A[i,j]-m*A[k,j]

X = np.zeros((n,1))
X[n-1,0]=A[n-1,n]/A[n-1,n-1]

for i in range(n-2,-1,-1):
    S=0
    for j in range(i+1,n):
        S=S+A[i,j]*X[j,0]
    X[i,0]=(A[i,n]-S)/A[i,i]

print(X)