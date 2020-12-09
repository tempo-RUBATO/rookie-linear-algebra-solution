import numpy as np
#can only solve full-rank matrix :(
def rank(A:np.array):
    rank=0
    AT=A
    if(np.size(A,axis=0)>np.size(A,axis=1)):
        AT=A.T
    height=np.size(AT,axis=0)
    for i in range(0,height,1):
        AT[i]=AT[i]/AT[i,i]
        for j in range(i+1,height,1):
            AT[j]=AT[j]-AT[i]*AT[j,i]
    for i in range(0,height,1):
        if(AT[i,i]!=0):
            rank = rank +1

    return rank


