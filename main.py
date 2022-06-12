
from tkinter.tix import ROW
import networkx as nx
import matplotlib.pyplot as plt
from queue import Queue, PriorityQueue
import numpy as np
from src.Floyd_Warshall_Algo import Floyd_Warshall
from src.Dijkstras_Shortest_Path_Algorithm import dijkstra
from src.DiGraph import DiGraph
from src.GraphElements import EdgeData
from src.GraphElements import NodeData
from src.create_nx_graph_from_DiGraph import create_nx_graph
from src.Find_Graph_Diameter import diameter_dp, best
from src import Build_Span_Tree
from src import Find_Graph_Diameter
from src import find_max_submatrix
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
a=[[2,1,-3,-4,5],[0,6,3,4,1],[2,-2,-1,4,-5],[-3,3,1,0,3]]
print('\n'.join(['\t'.join([str(cell)for cell in row])for row in a]))

sol,ind=find_max_submatrix.dynamic_sub_matrix(a)
print (sol)
print (ind)    