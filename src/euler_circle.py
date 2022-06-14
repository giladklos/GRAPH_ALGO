#this module contain the method to find euler circle 
from inspect import stack
import numpy as np
import random as rng
from queue import Queue,PriorityQueue,LifoQueue
def euler_cir(mat):
#choosing a random node to start
    s=rng.randint(0,len(mat)-1)
    #should check if the graph is strongly connected with BFS (github)

    #should check if the graph has un-even vertexes
    # vertexes with deg(1) should be deleted. then check with BFS again
    count=0
    for i in range (len(mat[s])):
        if mat[s][i]>0:
            count+=1
    if count%2==0:
        mat[s][:]=np.zeros(len(mat[s]))
        mat[:][s]=np.zeros(len(mat[s]))
    st=LifoQueue()
    st.put(s)
       
