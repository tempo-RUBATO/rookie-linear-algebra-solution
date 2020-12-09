import numpy as np
def cofac(A:np.array,i:int,j:int):
    dim=np.size(A,axis=1)
    if(dim  == 1):
        print("A 0-dimensional matrix has no cofactor!")
    else:
        cofac_A=A
        if (i==0):
            cofac_A=cofac_A[1:dim]
        else:
            cofac_A1=cofac_A[0:i]
            cofac_A2=cofac_A[i+1:dim]  
            cofac_A=np.r_[cofac_A1,cofac_A2]
        if(j==0):
            cofac_A=cofac_A[:,1:dim]
        else:
            cofac_B1=cofac_A[:,0:j]
            cofac_B2=cofac_A[:,j+1:dim]
            
            cofac_A=np.c_[cofac_B1,cofac_B2]
    return cofac_A

def algebra_cofac(A:np.array,i:int,j:int):
    alge_cofac_A=(-1)**(i+j)*cofac(A,i,j)
    return alge_cofac_A




        
      

