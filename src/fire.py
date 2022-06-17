# this module implements the fire algorithms to find 
# radius, diameter and center/s of a graph
import queue
import numpy as np
from queue import Queue,LifoQueue
def fire(G):
    count=0
    center=0
    q=queue.Queue
    while G.v_size>=2:
        for i in G.get_all_V():
            n=G.get_node(i)
            if n.tag==1:
                q.put(i)
        while not q.empty():
            G.remove_node(q.get())
        update_degs(G)
    if G.v_size()==2:
        return count*2+1
    return count*2


def update_degs():
    for i in G.get_all_v():
        n=G.get_node(i)
        n.tag=len(n.neighbors)+len(n.guests)        

