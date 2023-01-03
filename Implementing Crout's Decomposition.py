# PROJECT - 9

## Importing Libraries
import numpy as np

## Crout's Decomposition
def crouts_decomposition(A,n):
    for i in range(0,n):
        for j in range(i,n):                    #overwrites the column of A with the column of L
            for k in range(0,i):
                A[j,i]=A[j,i]-A[j,k]*A[k,i]
        for j in range(i+1,n):                  #overwrites the row of A with the row of U
            for k in range(0,i):
                A[i,j]=A[i,j]-A[i,k]*A[k,j]
        if A[i,i]==0:
            for j in range(i+1,n):
                if A[i,j]!=0:
                    return i
        else:
            for j in range(i+1,n):
                A[i,j]=A[i,j]/A[i,i]
        
    return A

## Solving the System of Equations
def solve(A,B,n):
    for i in range(0,n):                        #computes X' where X' = UX
        for k in range(0,i):
            B[i]=B[i]-B[k]*A[i,k]
        if A[i,i]==0:
            if B[i]!=0:
                return 0                        #returns 0 if division of non-zero number by zero is encountered
            else:
                B[i]=0                          #puts zero in place of B[i] if division of zero by zero is encountered
        else:
            B[i]=B[i]/A[i,i]

    for i in range(n-1,-1,-1):                  #computes X
        for k in range(n-1,i,-1):
            B[i]=B[i]-B[k]*A[i,k]
    return B


## Taking the matrix input from the user
n=int(input("Enter the order of coefficient matrix "))
print("Enter the values of the coefficient matrix (row-wise and separated by space)")
A=np.matrix(list(map(float,input().split()))).reshape(n,n)
print("Enter the constants (separated by space)")
B=np.array(list(map(float,input().split())))

## Computing Crout's Decomposition and Solving the system of Equations
print("\nOBJECTIVE : To solve the system of linear equations Ax=B using LU Decomposition Method")
print("where A is the coefficient matrix = ")
print(A)
print("and B is the rhs vector = ", B, "\n") 
A = crouts_decomposition(A,n)
if type(A)==int:
    print("ERROR\nCrout's Decomposition does not exist")
else:
    print("A after efficient implementation = ")
    print(A)
    print("(with the part above diagonal being U and the rest being L such that A = LU)\n")
    B = solve(A,B,n)
    if type(B)==int:
        print("System is Inconsistent")
    else:
        print("System is Consistent\nSolution to above system = ",B)
