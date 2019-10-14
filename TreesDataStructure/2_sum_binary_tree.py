#!/usr/bin/env python
import sys
from BST import TreeNode
from BST import insertNode

# 2-Sum Binary Tree
# https://www.interviewbit.com/problems/2sum-binary-tree/
#
# Given a binary search tree T, where each node contains a positive integer, and an integer K,
# you have to find whether or not there exist two different nodes A and B such that A.value + B.value = K.
#
# Return 1 to denote that two such nodes exist. Return 0, otherwise.
#
# Notes
#
# Your solution should run in linear time and not take memory more than O(height of T).
# TODO: IMPROVE MEMORY COMPLEXITY
# Assume all values in BST are distinct.
# Example :
#
# Input 1:
#
# T :       10
#          / \
#         9   20
#
# K = 19
#
# Return: 1
#
# Input 2:
#
# T:        10
#          / \
#         9   20
#
# K = 40
#
# Return: 0
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _findTarget(self, A, B, dp):
        if not A:
            return False

        if B - A.val in dp:
            return True

        dp[A.val] = True

        return self._findTarget(A.left, B, dp) or self._findTarget(A.right, B, dp)

    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def t2Sum(self, A, B):
        return int(self._findTarget(A, B, dict()))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == '__main__':
    # Input DATA to practice: 11 2 9 13 57 25 17 1 90 3
    r = TreeNode(int(sys.argv[1]))
    for arg in range(2, len(sys.argv), 1):
        insertNode(r, TreeNode(int(sys.argv[arg])))

    s = Solution()
    print(s.t2Sum(r, 1))