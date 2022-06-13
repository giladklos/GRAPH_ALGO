import numpy as np
class Node():
    def __init__(self) -> None:
        key=None
        info="white"
        neighbors={}

class Graph():
    def __init__(self):
        self.graph={}
        self.Nnodes=None
        self.Nedges=None

    def get_node(self,n)->Node:
        return self.graph[n]
    
    def get_all_nodes(self)->list(Node):
        #git is shit
        