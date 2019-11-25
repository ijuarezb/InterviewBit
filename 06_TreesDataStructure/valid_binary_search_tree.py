#!/usr/bin/env python3
import sys

# https://www.interviewbit.com/problems/valid-binary-search-tree/
#
# Valid Binary Search Tree
# Asked in:  
# Amazon
# Facebook
# Bookmark Suggest Edit
# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node’s key.
# The right subtree of a node contains only nodes with keys greater than the node’s key.
# Both the left and right subtrees must also be binary search trees.
# Example :
#
# Input : 
#    1
#   /  \
#  2    3
#
# Output : 0 or False
#
#
# Input : 
#   2
#  / \
# 1   3
#
# Output : 1 or True 
#
# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isValidBST(self, A):
        
        stack, ans = list(), list()
        i = 0

        if A:
            stack.append(A)

        while stack:
            node = stack[-1]
            if not node.left or hasattr(node.left, 'visited'):
                node.visited = True
                ans.append(stack.pop().val)
                i += 1

                if node.right:
                    stack.append(node.right)
            else:
                stack.append(node.left)
                
            if len(ans) > 1:
                if ans[i-1] <= ans[i-2]:
                    return 0
                    
        n = len(ans)
        
        if n >= 2:
            for i in range(1, n):
                if ans[i] <= ans[i-1]:
                    return 0

        return 1