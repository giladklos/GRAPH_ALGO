# this module implements DFS method of iteration over a graph

import numpy as np

def dfs(G,s):
    G.reset_color()
    for n in G.get_all_v():
        G.get_node(n).parent=None
        G.get_node(n).tag=0
    
    time=0
    for v in G.get_all_v():
        dfs_visit(G,v,time)

def dfs_visit(G,u,t):
    t+=1
    G.get_node(u).tag=t
    G.get_node(u).info="grey"

    for  v,w in G.all_out_edges_of_node(u).items():
        if G.get_node(v).info=="white":
            G.get_node(v).parent=u
            dfs_visit(G,v,t)
    G.get_node(u).info="black"
    t+=1
    G.get_node(u).tag=t