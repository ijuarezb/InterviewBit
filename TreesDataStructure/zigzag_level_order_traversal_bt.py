#!/usr/bin/env python3
import sys
from BST import TreeNode
from BST import insertNode
  
# ZigZag Level Order Traversal BT
# https://www.interviewbit.com/problems/zigzag-level-order-traversal-bt/
#
# Given a binary tree, return the zigzag level order traversal of its nodes’ values. (ie, from
# left to right, then right to left for the next level and alternate between).
#
#
# Example :
# Given binary tree
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return
#
# [
#          [3],
#          [20, 9],
#          [15, 7]
# ]
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
            if lvl % 2 == 0:
            	lst[lvl].append(el)
            else:
            	lst[lvl].insert(0, el)


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

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Alt_Solution:
    def _zigzagLevelOrder(self, A, i, result):
        if not A:
            return

        if i == len(result):
            result.append([])

        self._zigzagLevelOrder(A.left, i + 1, result)
        result[i].append(A.val)
        self._zigzagLevelOrder(A.right, i + 1, result)

    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, A):
        result = []
        self._zigzagLevelOrder(A, 0, result)

        for i in range(1, len(result), 2):
            result[i] = list(reversed(result[i]))
        return result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == '__main__':
	# Input DATA to practice: 11 2 9 13 57 25 17 1 90 3
    r = TreeNode(int(sys.argv[1]))
    for arg in range(2, len(sys.argv), 1):
    	insertNode(r, TreeNode(int(sys.argv[arg])))

    # Print inoder traversal of the BST 
    s = Solution()
    print(s.levelOrder(r))