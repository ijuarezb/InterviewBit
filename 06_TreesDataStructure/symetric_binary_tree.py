#!/usr/bin/env python3
import sys
from BST import TreeNode
from BST import insertNode
from BST import inOrderTraversal
from BST import preOrderTraversal

# Symmetric Binary Tree
# https://www.interviewbit.com/problems/symmetric-binary-tree/
#
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# Example :
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# The above binary tree is symmetric.
# But the following is not:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for a  binary tree node
# class TreeNode:
#   def __init__(self, x):
#       self.val = x
#       self.left = None
#       self.right = None

class Solution:

    def _isSymmetric(self, A, B):

        if not A and not B:
            return True
        elif (not A and B) or (A and not B):
            return False

        if A.val == B.val:
            return self._isSymmetric(A.left, B.right) and self._isSymmetric(A.right, B.left)
        return False

    def _isSymetric2(self, r1, r2):
        # If boto trees are empty, then they are mirror(symetric)
        if not r1 and not r2:
            return True
        elif (not r1 and r2) or (r1 and not r2):
            return False

        # Mirror Trees have the following conditions:
        # 1. Their root nodes KEYs must be the same
        # 2. Left subtree of left tree and right subtree of right
        #    tree have to be mirror images.
        # 3. Right subtree of left tree and left subtree of right
        #    tree have to be mirror.

        if r1.val == r2.val:
            return self._isSymetric2(r1.left, r2.right) and self._isSymetric2(r1.right, r2.left)

        # If neither of the conditions above are True, then
        # R1 and R2 are not mirror images.


        return False


    # @param A : root node of tree
    # @return an integer
    def isSymmetric(self, A):
        if not A:
            return 1

        return int(self._isSymetric2(A, A))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == '__main__':
    #r1 = TreeNode(int(sys.argv[1]))
    #for arg in range(2, len(sys.argv), 1):
    #    insertNode(r1, TreeNode(int(sys.argv[arg])))

    r1 = TreeNode(2)
    node1 = TreeNode(1)
    node2 = TreeNode(1)

    r1.left = node1
    r1.right = node2

    s = Solution()
    if s.isSymmetric(r1):
        print("Both trees are Identical Binary Trees")
    else:
        print("Both trees are not Identical Binary Trees")


