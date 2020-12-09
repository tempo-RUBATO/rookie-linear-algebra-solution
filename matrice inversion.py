import numpy as np
# N*N simple matrice inversion
def invert(A:np.array):
    width=np.size(A,1)
    height=np.size(A,0)
    n=height
    if width!=height:
        print("non-square!")
    else:
        determinant=1/np.linalg.det(A)
        if(determinant==0):
            print("uninvertible!")
        else:
            E=np.identity(n)
            AE=np.c_[A,E]
            for i in range(0,n,1):
                AE[i]=AE[i]/AE[i,i]
                for j in range(i+1,n,1):
                    AE[j]=AE[j]-AE[i]*AE[j,i]
            for i in range(0,n,1):
                AE[n-i-1]=AE[n-i-1]/AE[n-i-1,n-i-1]
                for j in range(i+1,n,1):
                    AE[n-j-1]=AE[n-j-1]-AE[n-i-1]*AE[n-j-1,n-i-1]
    return AE