#!/usr/bin/env python
import sys
from BST import TreeNode
from BST import insertNode
from BST import inOrderTraversal
from BST import preOrderTraversal
from BST import postOrderTraversal

# Construct Binary Tree From Inorder And Preorder
# https://www.interviewbit.com/problems/construct-binary-tree-from-inorder-and-preorder/
#
# Given preorder and inorder traversal of a tree, construct the binary tree.
#
#  Note: You may assume that duplicates do not exist in the tree.
# Example :
#
# Input :
#         Preorder : [1, 2, 3]
#         Inorder  : [2, 1, 3]
#
# Return :
#             1
#            / \
#           2   3

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return the root node in the tree
    def buildTree(self, preorder, inorder):

        if not preorder:
            return None

        root = TreeNode(preorder[0])
        idx = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:idx + 1], inorder[:idx])
        root.right = self.buildTree(preorder[idx + 1:], inorder[idx + 1:])

        return root

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == '__main__':
    s = Solution()
    t = s.buildTree(preorder=[1, 2, 4, 3, 5, 6], inorder=[4, 2, 1, 5, 3, 6])
    inOrderTraversal(t)
    print()
    preOrderTraversal(t)
    print()
    postOrderTraversal(t)
    print()
