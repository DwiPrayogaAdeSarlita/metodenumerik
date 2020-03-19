from pprint import pprint
from numpy import array,zeros,diag,diagflat,dot

def jacobi(A,b,N=25,x=None):
    if x is None:
        x=zeros(len(A[0]))
    D=diag(A)
    R=A-diagflat(D)
    for A in range(N):
        x=(b-dot(R,x))/D
    return x

A=array([[3,-0.1,-0.2],[0.1,7,-0.3],[0.3,-0.2,10]])
b=array([7.85,-19.3,71.4])
quess=array([1.0,1.0,1.0])
sol=jacobi(A,b,N=25,x=quess)
print("A:")
pprint(A)
print("b:")
pprint(b)
print("x:")
pprint(sol)