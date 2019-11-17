#!/usr/bin/env python3
import sys
from BST import TreeNode
from BST import insertNode
from BST import inOrderTraversal
from BST import preOrderTraversal

# Level Order
# https://www.interviewbit.com/problems/level-order/
#
# Given a binary tree, return the level order traversal of its nodes’ values. (ie, from left to right, level by level).
#
# Example :
# Given binary tree
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# return its level order traversal as:
#
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
#
# Also think about a version of the question where you are asked to do a level order traversal of
# the tree when depth of the tree is much greater than number of nodes on a level.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def levelOrder(self, A):
        from collections import deque

        def insert(el, lvl, lst):
            if len(ans) == lvl:
                lst.append([])
            lst[lvl].append(el)

        queue, ans = deque(), list()

        if A:
            queue.append((0, A))

        while len(queue) > 0:
            lvl, node = queue.popleft()
            insert(node.val, lvl, ans)

            for child in [node.left, node.right]:
                if child:
                    queue.append((lvl + 1, child))

        return ans

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

    def preorderTraversal(self, A):
        stack, ans = list(), list()

        if A:
            stack.append(A)

        while stack:
            node = stack[-1]
            ans.append(stack.pop().val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return ans

if __name__ == '__main__':
	# Input DATA to practice: 11 2 9 13 57 25 17 1 90 3
    r = TreeNode(int(sys.argv[1]))
    for arg in range(2, len(sys.argv), 1):
    	insertNode(r, TreeNode(int(sys.argv[arg])))

    # Print inoder traversal of the BST 
    s = Solution()
    print(s.levelOrder(r))