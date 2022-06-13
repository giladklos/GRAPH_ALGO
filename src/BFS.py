# this module implements a bfs search on a given graph(G) 
# with a starting node(s)

#import GraphElements as GE
from src import DiGraph as DG
import numpy as np
from queue import Queue,PriorityQueue
def bfs(G,s,d):
    NG=G
    NG.get_node(s).info="grey"
    #NG.reset_color()
    #d= np.zeros(NG.v_size())
    f=np.zeros(NG.v_size())
    for g in NG.get_all_v():
        f[NG.get_node(g).key]=-1
        d[NG.get_node(g).key]=np.inf
    f[NG.get_node(s).key]=-1
    d[NG.get_node(s).key]=0
    q=PriorityQueue()
    q.put(s)
    
    while not q.empty():
        u=q.get()
        for v,w in NG.all_out_edges_of_node(u).items():
            if NG.get_node(v).info=="white":
                NG.get_node(v).info="grey"
                d[NG.get_node(v).key]=1+d[NG.get_node(u).key]
                f[NG.get_node(v).key]=NG.get_node(u).key
                q.put(NG.get_node(v).key)
        NG.get_node(u).info="black"
    return d
 # this method find the connection components of a graph
 # using a BFS search. prints the colors and the cc at the end   
def cc_find(G,s):
    d=np.zeros(G.v_size())
    count=1
    d=bfs(G,s,d)
    cc=np.zeros(G.v_size())
    for i in range(len(cc)):
        if not d[i]==np.inf and cc[i]==0:
            cc[i]=count
    
    
    for i in range(len(d)):
        if d[i]==np.inf:
            count+=1
            d=bfs(G,i,d)
            for i in range(len(cc)):
                if not d[i]==np.inf and cc[i]==0:
                     cc[i]=count
           
    G.reset_color()   
    print(count) 
    for i in range(len(cc)):
        print({i:cc[i]})
    
def bfs_diam(G,s):
    d=np.zeros(G.v_size())
    dmax=0
    j=0
    d=bfs(G,s,d)
    for i,dat in enumerate(d):
        if dat>dmax and dat<np.inf:
            dmax=dat
            j=i
    d=bfs(G,j,d)
    for i,dat in enumerate(d):
        if dat>dmax and dat<np.inf:
            dmax=dat
            j=i
    print (dmax)