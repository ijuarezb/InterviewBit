#!/usr/bin/env python3
import sys
import collections

# Largest Distance between nodes of a Tree
# https://www.interviewbit.com/problems/largest-distance-between-nodes-of-a-tree/
#
# Find largest distance
#
# Given an arbitrary unweighted rooted tree which consists of N (2 <= N <= 40000) nodes. 
# The goal of the problem is to find largest distance between two nodes in a tree. 
# Distance between two nodes is a number of edges on a path between the nodes 
# (there will be a unique path between any pair of nodes since it is a tree). The nodes
# will be numbered 0 through N - 1.
#
# The tree is given as an array P, there is an edge between nodes P[i] and i (0 <= i < N). 
# Exactly one of the i’s will have P[i] equal to -1, it will be root node.
#
#     Example:
#     If given P is [-1, 0, 0, 0, 3], then node 0 is the root and the whole tree looks like this:
#
#           0
#        /  |  \
#       1   2   3
#                \
#                 4
#
# One of the longest path is 1 -> 0 -> 3 -> 4 and its length is 3, thus the answer is 3. Note that
# there are other paths with maximal distance.
#
# NOTE:
# same approach as in: Max Sum Path in Binary Tree ==> Getting MAX distance between any two nodes
# https://www.interviewbit.com/problems/max-sum-path-in-binary-tree/
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import sys
sys.setrecursionlimit(100000)

class Solution:

    @staticmethod
    def _max_2nd_max(max1, max2, new_item):
        if new_item > max1:
            return new_item, max1
        elif new_item > max2:
            return max1, new_item
        else:
            return max1, max2

    def _bfs(self, idx, conn):

        if idx not in conn:
            return 0, 1

        max1 = max2 = maxW = 0
        for child in conn[idx]:
            w, h = self._bfs(child, conn)
            max1, max2 = Solution._max_2nd_max(max1, max2, h)
            maxW = max(maxW, w)

        return (max(maxW, max1 + max2), max1 + 1) if idx != -1 else (maxW, max1 + 1)


    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        from collections import defaultdict
        conn = defaultdict(list)
        for i, e in enumerate(A):
            conn[e].append(i)
        return self._bfs(-1, conn)[0] if len(A) > 1 else 0

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# BFS modified:  Gets D from root to leaf & additionally D from leaf_max1 to leaf_max2
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def bfs_modified(self, A, startnode=0):
        if len(A) <= 1: return 0
        color = {}
        d = {}
        PI = {}
        graph = collections.defaultdict(list)
        for i, e in enumerate(A):
        	graph[e].append(i)
        	if i not in graph:
        		graph[i] = []
        graph.pop(-1)

        for u in graph:
            color[u] = 'white'
            d[u] = 1000
            PI[u] = ''
        color[startnode] = 'gray'
        d[startnode] = 0

        seen, queue = set([startnode]), collections.deque([startnode])

        
        b = {i:i for i in graph[0]}
        b[0] = 0
        max_branch = {i:0 for i in graph[0]}
        max_branch[0] = 0

        while queue:
            vertex = queue.popleft()

            for v in graph[vertex]:
                if color[v] == 'white':        #checking if not visited
                    color[v] = 'gray'
                    d[v] = d[vertex] + 1
                    PI[v] = vertex
                    b[v] = b[vertex] if vertex not in graph[0] else vertex
                    max_branch[b[v]] = max(max_branch[b[v]], d[v])
                    queue.append(v)
                    
            color[vertex] = 'black'

        D = sorted(max_branch.values(), reverse=True)
        return D[0] + D[1]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == '__main__':
	P = [-1, 0, 0, 0, 3]
	s = Solution()
	print(s.bfs_modified(P, 0))
	print(s.solve(P))
	P = [-1, 0]
	print(s.bfs_modified(P, 0))
	P = [ -1, 0, 1, 1, 2, 0, 5, 0, 3, 0, 0, 2, 3, 1, 12, 14, 0, 5, 9, 6, 16, 0, 13, 4, 17, 2, 1, 22, 14, 20, 10, 17, 0, 32, 15, 34, 10, 19, 3, 22, 29, 2, 36, 16, 15, 37, 38, 27, 31, 12, 24, 29, 17, 29, 32, 45, 40, 15, 35, 13, 25, 57, 20, 4, 44, 41, 52, 9, 53, 57, 18, 5, 44, 29, 30, 9, 29, 30, 8, 57, 8, 59, 59, 64, 37, 6, 54, 32, 40, 26, 15, 87, 49, 90, 6, 81, 73, 10, 8, 16 ]
	print(s.bfs_modified(P,0))
	print(s.solve(P))
	P = [ -1, 0, 1, 1, 3, 0, 4, 0, 2, 8, 9, 0, 4, 6, 12, 14, 7, 9, 6, 4, 14, 13, 1, 9, 16, 17, 17, 0, 21, 10, 13, 14, 25, 28, 27, 0, 35, 20, 34, 23, 37, 3, 6, 25, 30, 22, 15, 37, 8, 6, 11, 22, 50, 12, 4, 2, 54, 23, 18, 52, 34, 49, 61, 8, 15, 63, 31, 51, 48, 41, 26, 37, 30, 15, 59, 12, 0, 40, 37, 73, 32, 19, 70, 29, 8, 21, 83, 33, 7, 13, 12, 82, 43, 86, 38, 31, 1, 84, 62, 83 ]
	print(s.bfs_modified(P,0))
	print(s.solve(P))