#!/usr/bin/env python
import sys
from BST import TreeNode

# Inorder Traversal of Cartesian Tree
# https://www.interviewbit.com/problems/inorder-traversal-of-cartesian-tree/
#
# Given an inorder traversal of a cartesian tree, construct the tree.
#
#  Cartesian tree : is a heap ordered binary tree, where the root is greater than all the elements 
# in the subtree.
#  Note: You may assume that duplicates do not exist in the tree.
# Example :
#
# Input : [1 2 3]
#
# Return :
#           3
#          /
#         2
#        /
#       1
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : list of integers
    # @return the root node in the tree
    def buildTree(self, A):

        if not A:
            return None

        import operator
        max_index, max_value = max(enumerate(A), key=operator.itemgetter(1))
        #d_keys = list(d.keys())
        #u = min(d_keys, key=(lambda k: d[k]))

        root = TreeNode(max_value)
        root.left = self.buildTree(A[:max_index])
        root.right = self.buildTree(A[max_index + 1:])

        return root

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == '__main__':
    A = [-2, -1, 1, 2 ,3]
    s = Solution()
    r = s.buildTree(A)
    print(r.val)
    print(r.left.val)
    print(r.left.left.val)
    print(r.left.left.left.val)
    print(r.left.left.left.left.val)
