#!/usr/bin/env python
import sys
from BST import TreeNode
from BST import insertNode

# Sorted Array To Balanced BST
# https://www.interviewbit.com/problems/sorted-array-to-balanced-bst/
#
# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
#
#  Balanced tree : a height-balanced binary tree is defined as a binary tree in which the depth of
# the two subtrees of every node never differ by more than 1.
# Example :
#
#
# Given A : [1, 2, 3]
# A height balanced BST  :
#
#       2
#     /   \
#    1     3
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree
    def sortedArrayToBST(self, A):
        if not A:
            return None

        root_index = len(A) // 2

        root = TreeNode(A[root_index])
        root.left = self.sortedArrayToBST(A[:root_index])
        root.right = self.sortedArrayToBST(A[root_index + 1:])

        return root

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == '__main__':
	A = [1, 2, 3]
	#A = [11, 2, 9, 13, 57, 25, 17, 1, 90, 3]
	A = [1, 2, 3, 9, 11, 13, 17, 25, 57, 90]

	s = Solution()
	r = s.sortedArrayToBST(sorted(A))
	print(r.val)
	print(r.left.val)
	print(r.left.left.val)
	print(r.left.right.val)
	print(r.right.val)
	print(r.right.left.val)
	print(r.right.right.val)