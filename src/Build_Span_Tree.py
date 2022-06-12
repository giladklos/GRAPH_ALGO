import numpy as np

def buildTree (nodes):
    N= len(nodes)
    if not(np.sum(nodes)==2*(N-1)):
        print("cannot be reprensnted as a tree! ")
        return
    nodes=np.sort(nodes)
    tree=np.zeros(N)
    
    for k in range(len(nodes)):
        if nodes[k]>1:
            j=k
            break
    
    for i in range(N-2):
        tree[i]=j
        nodes[j]-=1
        nodes[i]-=1
        if nodes[j] == 1:
            j+=1
    tree[N-2]=tree[N-3]
    
    return tree
