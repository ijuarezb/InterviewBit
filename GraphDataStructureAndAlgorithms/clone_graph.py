#!/usr/bin/env python3
import sys
  
# Clone Graph
# https://www.interviewbit.com/problems/clone-graph/
#
# Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node: return node 

        from collections import deque
        D, Q = {}, deque()

        cloned = UndirectedGraphNode(node.label)
        D[node] = cloned
        Q.append(node)
        
        while Q:
            u = Q.popleft()
            for v in u.neighbors:
                if v not in D:
                    D[v] = UndirectedGraphNode(v.label)
                    Q.append(v)
                D[u].neighbors.append(D[v])
                    
        return cloned

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
