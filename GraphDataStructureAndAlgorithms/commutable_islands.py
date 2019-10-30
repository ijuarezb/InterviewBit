#!/usr/bin/env python3
import sys

# Commutable Islands
#
# There are n islands and there are many bridges connecting them. Each bridge has
# some cost attached to it.
#
# We need to find bridges with minimal cost such that all islands are connected.
#
# It is guaranteed that input data will contain at least one possible scenario in which
# all islands are connected with each other.
#
# Example :
# Input
#
#          Number of islands ( n ) = 4
#          1 2 1
#          2 3 4
#          1 4 3
#          4 3 2
#          1 3 10
#
# In this example, we have number of islands(n) = 4 . Each row then represents a bridge
# configuration. In each row first two numbers represent the islands number which are connected
# by this bridge and the third integer is the cost associated with this bridge.
#
# In the above example, we can select bridges 1(connecting islands 1 and 2 with cost 1),
# 3(connecting islands 1 and 4 with cost 3), 4(connecting islands 4 and 3 with cost 2). Thus we
# will have all islands connected with the minimum possible cost(1+3+2 = 6).
# In any other case, cost incurred will be more.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class Solution:

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Kruskal modified, to get MSP (the minimun PATH(tree) that connects all vertices)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    class Edges(list):
        def __lt__(self, other):
            for i in [2, 0, 1]:
                if self[i] == other[i]:
                    continue
                return self[i] < other[i]


    class DisjoinSet:
        def __init__(self, i):
            self.parent = i
            self.lvl = 0

        def __repr__(self):
            return "{}<{}>".format(self.parent, self.lvl)

    @staticmethod
    def findSet(x, S):
        if S[x].parent == x:
            return x
        S[x].parent = Solution.findSet(S[x].parent, S)
        return S[x].parent

    @staticmethod
    def unionSet(a, b, S):
        set_a = Solution.findSet(a, S)
        set_b = Solution.findSet(b, S)

        if S[set_a].lvl < S[set_b].lvl:
            S[set_a].parent = set_b
        elif S[set_a].lvl > S[set_b].lvl:
            S[set_b].parent = set_a
        else:
            S[set_b].parent = set_a
            S[set_a].lvl += 1

    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        B.sort(key=Solution.Edges)
        S = [None] + [Solution.DisjoinSet(i + 1) for i in range(A)]
        components, weigth = A - 1, 0

        for edge in B:
            if components == 0:
                break

            start = Solution.findSet(edge[0], S)
            end = Solution.findSet(edge[1], S)

            if start == end:
                continue

            Solution.unionSet(start, end, S)
            components -= 1
            weigth += edge[2]

        return weigth

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Dijkstra: to get the shortest PATH from Source to any other indiviual Vertex/Node
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # Track distance from source to each node.  Get Parent as well.
    def Dijkstra(self, graph, source):
        Q = set()

        d, PI = {}, {}
        for u, weights in enumerate(graph):
            d[u] = 10000
            PI[u] = ''
            Q.add(u)
        d[source] = 0

        d_keys = list(d.keys()) # List to track d[] processed
        while Q:  # while Q not empty
            # Getting Vertex with minimun distance:
            u = min(d_keys, key=(lambda k: d[k]))
            d_keys.remove(u)
            
            Q.remove(u)
            
            for v, w in enumerate(graph[u]):
                dis_u_v = d[u] + graph[u][v] if graph[u][v] != -1 else d[v]
                if dis_u_v < d[v]:
                    d[v] = dis_u_v
                    PI[v] = u

        return list(d.values())

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Prim, similar to Kruskal, but less efficient due space complexity. To get MSP.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def Prim2(self, graph, source):
        Q, Key = set(), {}
        for u, weights in enumerate(graph):
            Key[u] = 10000
            Q.add(u)
        Key[source] = 0

        while Q:  # while Q not empty
            u = min(Key.keys(), key=(lambda k: Key[k]))
            Key.pop(u)
            Q.remove(u)
            
            for v, w in enumerate(graph[u]):
                if v in Q and w < Key[v] and w != -1:
                    Key[v] = w
                    graph[v][v] = w

        return [graph[i][i] if graph[i][i] != -1 else 0 for i in range(len(graph))]

    def Prim(self, graph, source):
        Q = set()

        Key, PI, mark = {}, {}, {}
        for u, weights in enumerate(graph):
            Key[u] = 10000
            PI[u] = ''
            mark[u] = 0
            Q.add(u)
        Key[source] = 0
        mark[source] = 1

        d_keys = list(Key.keys()) # List to track d[] processed
        while Q:  # while Q not empty
            # Getting Vertex with minimun distance:
            u = min(d_keys, key=(lambda k: Key[k]))
            print(Key, u)
            d_keys.remove(u)
            Q.remove(u)
            mark[u] = 1
            
            for v, w in enumerate(graph[u]):
                mark[v] = 0
                if v in Q and w < Key[v] and w != -1:
                    Key[v] = w
                    PI[v] = u

        return list(Key.values())

    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        graph = [[-1] * A for _ in range(A)]
        for edge in B:
            graph[edge[0]-1][edge[1]-1] = edge[2]
            graph[edge[1]-1][edge[0]-1] = edge[2]

        for edge in graph:
            print(edge)
        return sum(self.Prim2(graph, 0))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Driver code
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == '__main__':
    s = Solution()
    n = 4
    B = [[1, 2, 1],
         [2, 3, 4],
         [1, 4, 3],
         [4, 3, 2],
         [1, 3, 10]]
    print(s.solve(n, B))

    A = 3
    B = [[1, 2, 10],
          [2, 3, 5],
          [1, 3, 9]]
    print(s.solve(A, B))

    A = 4
    B = [[1, 2, 1],
          [2, 3, 2],
          [3, 4, 4],
          [1, 4, 3]]
    print(s.solve(A, B))
