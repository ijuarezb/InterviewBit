#!/usr/bin/env python3
import sys
from BST import TreeNode
from BST import insertNode

# Inorder Traversal
# https://www.interviewbit.com/problems/inorder-traversal/
#
# Given a binary tree, return the inorder traversal of its nodes’ values.
#
# Example :
# Given binary tree
#
#    1
#     \
#      2
#     /
#    3
# return [1,3,2].
#
# Using recursion is not allowed.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, A):
        stack, ans = list(), list()

        if A:
            stack.append(A)

        while stack:
            node = stack[-1]
            if not node.left or hasattr(node.left, 'visited'):
                node.visited = True
                ans.append(stack.pop().val)

                if node.right:
                    stack.append(node.right)
            else:
            	stack.append(node.left)

        return ans

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

    def postorderTraversal(self, A):
        stack, ans = list(), list()
        i = 0

        if A:
            stack.append(A)

        while stack:
            node = stack[-1]
            if not node.left or hasattr(node.left, 'visitedp'):
                if not node.right or hasattr(node.right, 'visitedp'):
                    ans.append(stack.pop().val)
                    node.visitedp = True
                else:
                    stack.append(node.right)
            else:
                stack.append(node.left)

        return ans

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == '__main__':
    # Input DATA to practice: 11 2 9 13 57 25 17 1 90 3
    r = TreeNode(int(sys.argv[1]))
    for arg in range(2, len(sys.argv), 1):
    	insertNode(r, TreeNode(int(sys.argv[arg])))

    s = Solution()
    L = s.inorderTraversal(r)
    print("In Order Traversal: {}".format(L))
    L = s.preorderTraversal(r)
    print("Pre Order Traversal: {}".format(L))
    L = s.postorderTraversal(r)
    print("Post Order Traversal: {}".format(L))
