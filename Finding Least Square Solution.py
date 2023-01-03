# PROJECT - 6

## Importing Libraries
import numpy as np

## Efficient QR Decomposition        
def efficient_QR_decomposition(A):
    r,c=A.shape
    if r<c:
        return A,0
    else:
        p=[]
        for j in range(0,c):
            s=0
            for i in range(j,r):
                s = s + A[i,j]**2
            s=round(s,10)
            p.append(s**0.5)
            if s!=0:
                A[j,j] = A[j,j] - p[j]
                s=0
                for i in range(j,r):
                    s = s + A[i,j]**2
                s=s**0.5
                for i in range(j,r):
                    A[i,j] = A[i,j]/s

                for k in range(j+1,c):
                    s=0
                    for i in range(j,r):
                       s = s + A[i,j]*A[i,k]
                    for i in range(j,r):
                        A[i,k] = A[i,k] - 2*s*A[i,j]
        for i in range(0,r):
            for j in range(0,c):
                A[i,j]=round(A[i,j],10)
        
        return A,p

## Unique Least Square solution
def least_square_solution(A,p,B):
    r,c=A.shape
    X=np.array([])
    for j in range(0,c):
        s=0
        for i in range(j,r):
            s = s + A[i,j]*B[i]
        for i in range(j,r):
            B[i] = B[i] - 2*s*A[i,j]
        
    for i in range(0,c):
        X=np.append(X,[B[i]])

    for i in range(c-1,-1,-1):
        for k in range(c-1,i,-1):
            X[i] = X[i] - X[k]*A[i,k]
        X[i] = X[i]/p[i]
        
    return X

## Taking the matrix input from the user
r=int(input("Enter the number of rows of the coefficient matrix "))
c=int(input("Enter the number of columns of the coefficient matrix "))
print("Enter the values of the coefficient matrix (row-wise and separated by space)")
A=np.matrix(list(map(float,input().split()))).reshape(r,c)
print("Enter the rhs constants (separated by space)")
B=np.array(list(map(float,input().split())))

## Computing QR Decomposition and finding the least square solution
print("\nOBJECTIVE : To find the unique least square solution for system Ax=B using QR Decomposition Method")
print("where A is the coefficient matrix = ")
print(A)
print("and B is the rhs vector = ", B, "\n")

A,p=efficient_QR_decomposition(A)
if type(p)==int:
    print("ERROR\nQR Decomposition not possible")
else:
    print("A after efficient implementation = ")
    print(A)
    print("and the p vector (diagonal entries of R) = ",p)
    for i in range(0,c):
        if p[i]==0:
            break
    if p[i]==0:
        print("\nERROR\nA is not full column rank\nUnique least square solution does not exist")
    else:
        X=least_square_solution(A,p,B)
        print("\nUnique Least Square Solution = ",X)
