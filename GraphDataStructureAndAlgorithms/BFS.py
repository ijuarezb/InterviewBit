#!/usr/bin/env python3
import sys

#
# BFS implementation in python
#
# Set all nodes to "not visited";
#
#    q = new Queue();
#
#    q.enqueue(initial node);
#
#    while ( q ≠ empty ) do
#    {
#       x = q.dequeue();
#
#       if ( x has not been visited )
#       {
#          visited[x] = true;         // Visit node x !
#
#          for ( every edge (x, y)  /* we are using all edges ! */ )    
#             if ( y has not been visited )   
#          q.enqueue(y);       // Use the edge (x,y) !!!
#       }
#    }
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import collections
class graph:
    def __init__(self,adjacency=None):
        if adjacency is None:
            adjacency = {}
        self.adjacency = adjacency

def bfs(graph, startnode):
# Track the visited and unvisited nodes using queue
        seen, queue = set([startnode]), collections.deque([startnode])
        while queue:
            vertex = queue.popleft()
            print(vertex)
            for node in graph[vertex]:
                if node not in seen:        #checking if not visited
                    seen.add(node)
                    queue.append(node)

# BFS applied to a BST Java
# public void bfs() {
#             //BFS uses Queue data structure
#             Queue q = new LinkedList();
#             q.add(this.rootNode);
#             printNode(this.rootNode);
#             rootNode.visited = true;
#             while(!q.isEmpty()) {
#                 Node n = (Node)q.remove();
#                 Node child = null;
#                 while((child = getUnvisitedChildNode(n)) != null) {
#                     child.visited = true;
#                     printNode(child);
#                     q.add(child);
#                 }
#             }
#             //Clear visited property of nodes
#             clearNodes();
#         }

def bfs_bst(rootNode):
  queue = collections.deque([rootNode])
  ans = []
  rootNode.visited = True

  while queue:
    node = queue.popleft()
    child = None

    if node.left:
      queue.append(node.left)
    if node.right:
      queue.append(node.right)

# The graph dictionary
adjacency = { 
          "a" : set(["b","c"]),
          "b" : set(["a", "d"]),
          "c" : set(["a", "d"]),
          "d" : set(["e"]),
          "e" : set(["a"])
        }

bfs(adjacency, "a")