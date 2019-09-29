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

def bfs_brady(graph, startnode):
# Track distance from source to each node.  Get Parent as well.
        color = {}
        d = {}
        PI = {}
        for u in graph:
            color[u] = 'white'
            d[u] = 1000
            PI[u] = ''
        color[startnode] = 'gray'
        d[startnode] = 0

        seen, queue = set([startnode]), collections.deque([startnode])

        while queue:
            vertex = queue.popleft()
            print(vertex)
            for v in graph[vertex]:
                if color[v] == 'white':        #checking if not visited
                    color[v] = 'gray'
                    d[v] = d[vertex] + 1
                    PI[v] = vertex
                    queue.append(v)
            color[vertex] = 'black'

        print("Graph Color:    {}".format(color))
        print("Graph Distance: {}".format(d))
        print("Graph Parent:   {}".format(PI))

def Dijkstra(graph, source):
# Track distance from source to each node.  Get Parent as well.
        d = {}
        PI = {}
        Q = set()
        for u, weights in enumerate(graph):
            d[u] = 10000
            PI[u] = ''
            Q.add(u)
        d[source] = 0
        d_keys = list(d.keys()) # List to track records d[node] processed

        while Q:  # while Q not empty
            u = min(d_keys, key=(lambda k: d[k]))
            Q.remove(u)
            d_keys.remove(u)
            for v, w in enumerate(graph[u]):
                dis_u_v = d[u] + graph[u][v] if graph[u][v] != -1 else d[v]
                if dis_u_v < d[v]:
                    d[v] = dis_u_v
                    PI[v] = u

        return list(d.values())

if __name__ == '__main__':

  # The graph dictionary
  adjacency = { 
            "a" : set(["b", "c"]),
            "b" : set(["a", "d"]),
            "c" : set(["a", "d"]),
            "d" : set(["e"]),
            "e" : set(["a"])
          }
  #bfs(adjacency, "a")
  #bfs_brady(adjacency, "a")

  g = [[-1, 3, 2],
      [2, -1, 0],
      [-1, 0, -1]]
  print(Dijkstra(g, 0))

  g = [[-1,1,2], 
      [0,-1,3], 
      [0,0,-1]]
  print(Dijkstra(g, source=1))

  g = [[-1,0,0,0], 
      [-1,-1,-1,30], 
      [1,1,-1,1], 
      [2,2,0,-1]]
  print(Dijkstra(g, source=3))

  g = [[-1,-1,2], 
      [1,-1,0], 
      [-1,1,-1]]
  print(Dijkstra(g, source=0))

  g = [[-1,1,4], 
      [1,-1,4], 
      [4,4,-1]]
  print(Dijkstra(g, source=0))

  g = [[-1,3,2,-1], 
      [3,-1,-1,1], 
      [2,-1,-1,3], 
      [-1,1,3,-1]]
  print(Dijkstra(g, source=3))

  g = [[-1,5,20], 
      [21,-1,10], 
      [-1,1,-1]]
  print(Dijkstra(g, source=0))

  g = [[-1,5,2,15], 
      [2,-1,0,3], 
      [1,-1,-1,9], 
      [0,0,0,-1]]
  print(Dijkstra(g, source=2))