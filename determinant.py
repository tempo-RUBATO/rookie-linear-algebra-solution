import numpy as np
from cofactor import cofac,algebra_cofac
def det(A:np.array):
    dim=np.size(A,axis=1)
    determinant_A=0
    if (dim == 1):
        determinant_A = A[0,0]
    else:
        for i in range(0,dim,1):
            determinant_A=determinant_A+(-1)**(i+1)*A[0,i]*det(cofac(A,0,i))
    return determinant_A