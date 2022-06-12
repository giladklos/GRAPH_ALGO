#this module finds the largest submatrix of a given matrix with 
# different methods which includes dynamic programing and best method
# also Bar is Gay
import numpy as np
def dynamic_sub_matrix(mat):
    sum=0
    N=len(mat)
    M=len(mat[0])
    H=np.zeros([N,M])
    H[0][0]=mat[0][0]
    d=-1
    ind=[[0,0],[0,0]]
    for i in range(1,N):
        H[i][0]=mat[i][0]+H[i-1][0]
    for i in range(1,M):
        H[0][i]=mat[0][i]+H[0][i-1]
    
    for i in range(1,N):
        for j in range(1,M):
            H[i][j]=mat[i][j]+H[i-1][j]+H[i][j-1]-H[i-1][j-1]
    
    for i in range(1,N):
        for j in range(1,M):
            for k in range(i,N):
                for t in range(j,M):
                    sum=H[k][t]-H[k][j-1]-H[i-1][t]+H[i-1][j-1]
                    if sum>d:
                        d=sum
                        ind=[[i,j],[k,t]] 
               
    return d,ind