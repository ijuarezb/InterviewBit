#!/usr/bin/env python3
import sys
from BST import TreeNode
from BST import insertNode
from BST import inOrderTraversal
from BST import preOrderTraversal

# Identical Binary Trees
# https://www.interviewbit.com/problems/identical-binary-trees/
#
# Given two binary trees, write a function to check if they are equal or not.
#
# Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
#
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem
#
# Example :
#
# Input :
#
#    1       1
#   / \     / \
#  2   3   2   3
#
# Output :
#   1 or True
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def _isSameTree(self, A, B):

        s = int(not A) + int(not B)
        if s == 2:
            return True
        elif s == 1:
            return False
        else:
            return self._isSameTree(A.left, B.left) and self._isSameTree(A.right, B.right) and A.val == B.val

    def _identicalTrees(self, a, b): 
          
        # 1. Both empty 
        if a is None and b is None: 
            return True 
      
        # 2. Both non-empty -> Compare them 
        if a is not None and b is not None: 
            return ((a.val == b.val) and 
                    self._identicalTrees(a.left, b.left)and
                    self._identicalTrees(a.right, b.right)) 
          
        # 3. one empty, one not -- false 
        return False

    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    def isSameTree(self, A, B):
        return int(self._identicalTrees(A, B))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == '__main__':
    r1 = TreeNode(int(sys.argv[1]))
    for arg in range(2, len(sys.argv), 1):
        insertNode(r1, TreeNode(int(sys.argv[arg])))

    r2 = TreeNode(int(sys.argv[1]))
    for arg in range(2, len(sys.argv), 1):
        insertNode(r2, TreeNode(int(sys.argv[arg])))

    s = Solution()
    if s.isSameTree(r1, r2):
        print("Both trees are Identical Binary Trees")
    else:
        print("Both trees are not Identical Binary Trees")

    #preOrderTraversal(r2)
    #print()

