#!/usr/bin/env python3
import sys

#
# Pseudocode of Depth-first Search
#    Set all nodes to "not visited";
#    s = new Stack();    // get a stack
#    s.push(initial node);    // push the root node into the stack
#
#    while ( s is not EMPTY ) do {
#       x = s.pop();         // remove the top node from the stack and start exploring its branches
#       if ( x has not been visited ) {    // if you are visiting the node first time
#          visited[x] = true;		       // mark it as visited so that you do not visit it again
#          for ( every edge (x, y))        // all adjacent nodes of x will have an edge with x
#             if ( y has not been visited )// check if adjacent node is not already visited
# 	             s.push(y);      
#       }
#    }
#
# Pseudocode of Recursive Depth-first Search
# DFS(adjacent[][], vertex, visited[]) {
#    visited[vertex] = True
#   
#    FOR node in adjacent[vertex]:
#        IF visited[node] == False:
#           DFS(adjacent, node, visited)
#        END of IF
#    END of FOR
# }
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Implementation of DFS in python:
#
def dfs(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex)
    for node in graph[vertex] :
        if node not in visited:
        	dfs(graph, node, visited)

graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0', '4']),
         '3': set(['1', '4']),
         '4': set(['1', '2', '3'])}

dfs(graph, '0')