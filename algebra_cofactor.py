import numpy as np
from cofactor import cofac
def algebra_cofac(A:np.array,i:int,j:int):
    alge_cofac_A=(-1)**(i+j)*cofac(A,i,j)
    return alge_cofac_A
    


    