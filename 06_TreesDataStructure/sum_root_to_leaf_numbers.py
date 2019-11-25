#!/usr/bin/env python3
import sys
from BST import TreeNode

# Sum Root to Leaf Numbers
# https://www.interviewbit.com/problems/sum-root-to-leaf-numbers/
#
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
#
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
#
# Find the total sum of all root-to-leaf numbers % 1003.
#
# Example :
#
#     1
#    / \
#   2   3
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
#
# Return the sum = (12 + 13) % 1003 = 25 % 1003 = 25.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Soution(object):
    # @param A : root node of tree
    # @param B : integer
    # @return a list of list of integers
    def _sumNumbers(self, node, tmp_sum):
        if node is None:
            return 0

        tmp_sum = tmp_sum * 10 + node.val

        if not node.left and not node.right:
            ans = tmp_sum
        else:
            ans = self._sumNumbers(node.left, tmp_sum) + self._sumNumbers(node.right, tmp_sum)

        return ans

    # @param A : root node of tree
    # @param B : integer
    # @return a list of list of integers
    def sumNumbers(self, A):
        return self._sumNumbers(A, 0) % 1003

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == '__main__':

	s = Soution()
	t = TreeNode(5)
	t.left = TreeNode(4)
	t.left.left = TreeNode(9)
	t.left.left.left = TreeNode(7)
	t.left.left.right = TreeNode(2)
	t.right = TreeNode(8)
	t.right.left = TreeNode(7)
	t.right.right = TreeNode(4)
	t.right.right.left = TreeNode(5)
	t.right.right.right = TreeNode(1)
	print(s.sumNumbers(t))
	print((5497+5492+587+5845+5841)%1003)

#               5
#              / \
#             4   8
#            /   / \
#           9   7   4
#          /  \    / \
#         7    2  5   1