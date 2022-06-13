
from queue import PriorityQueue, Queue
from random import random
from tkinter.tix import ROW

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

from src import BFS, Build_Span_Tree, Find_Graph_Diameter, find_max_submatrix
from src.create_nx_graph_from_DiGraph import create_nx_graph
from src.DiGraph import DiGraph
from src.Dijkstras_Shortest_Path_Algorithm import dijkstra
from src.Find_Graph_Diameter import best, diameter_dp
from src.Floyd_Warshall_Algo import Floyd_Warshall
from src.GraphElements import EdgeData, NodeData

G = DiGraph()
n0 = NodeData(0, (0, -100, 0))
n1 = NodeData(1, (100, 0, 0))
n2 = NodeData(2, (50, 100, 0))
n3 = NodeData(3, (-100, 0, 0))

G.add_node(n0.key, n0.location)
G.add_node(n1.key, n1.location)
G.add_node(n2.key, n2.location)
G.add_node(n3.key, n3.location)

G.add_edge(0, 1, 1)
G.add_edge(1, 2, 3)
G.add_edge(2, 3, 4)
G.add_edge(3, 0, 1)
G.add_edge(3, 1, 2)
#print(dijkstra(0, 3, G))
#create_nx_graph(G)
# a=(1,2,-3,4,-7,9)
# d=Find_Graph_Diameter.cicle_best(a)
#print(mat)
# print (d)
#print(seq)
# maxb,seqb= best(a)
# print(maxb,seqb)
# nodes=(1,2,1,3,1,2)
# sol=Build_Span_Tree.buildTree(nodes)
# print(sol)
# a=[[2,1,-3,-4,5],[0,6,3,4,1],[2,-2,-1,4,-5],[-3,3,1,0,3]]
# print('\n'.join(['\t'.join([str(cell)for cell in row])for row in a]))

# sol,ind=find_max_submatrix.dynamic_sub_matrix(a)
# print (sol)
# print (ind)    



BFS.bfs(G,0)
for v in G.get_all_v():
    print(G.get_node(v).info)
G.reset_color()   
for v in G.get_all_v():
    print(G.get_node(v).info)