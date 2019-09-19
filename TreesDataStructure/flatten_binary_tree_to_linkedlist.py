#!/usr/bin/env python3
import sys
from BST import TreeNode
from BST import insertNode
from BST import inOrderTraversal
from BST import preOrderTraversal

# Flatten Binary Tree to Linked List
# https://www.interviewbit.com/problems/flatten-binary-tree-to-linked-list/
#
# Given a binary tree, flatten it to a linked list in-place.
#
# Example :
# Given
#
#
#          1
#         / \
#        2   5
#       / \   \
#      3   4   6
# The flattened tree should look like:
#
#    1
#     \
#      2
#       \
#        3
#         \
#          4
#           \
#            5
#             \
#              6
# Note that the left child of all nodes should be NULL.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def _concatenate(self, first, second):
        first.right = second
        first.left = None

    # This function, does not work!!!
    def _flatten(self, A):
        if not A:
            return None, None

        leftStart, leftEnd = self._flatten(A.left)
        rightStart, rightEnd = self._flatten(A.right)

        if leftStart:
            self._concatenate(A, leftStart)
            self._concatenate(leftEnd, rightStart)
        elif rightStart:
            self._concatenate(A, rightStart)
        return A, rightEnd if rightEnd else A

    # This function WORKS!!!
    def preorderTraversal(self, A):
        stack, ans = list(), list()
        root = None

        if A:
            stack.append(A)

        while stack:
            node = stack[-1]
            #ans.append(stack.pop().val)
            if root == None:
                root = node
                temp = root
            else:
                temp.right = node
                temp.left = None
                temp = temp.right
            stack.pop()


            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return root

    # @param A : root node of tree
    # @return the root node in the tree
    def flatten(self, A):
        #root, _ = self._flatten(A)
        root = self.preorderTraversal(A)
        return root

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


if __name__ == '__main__':

    r = TreeNode(int(sys.argv[1]))
    for arg in range(2, len(sys.argv), 1):
        insertNode(r, TreeNode(int(sys.argv[arg])))

    s = Solution()
    r2 = s.flatten(r)

    #preOrderTraversal(r2)
    #print()
    
    temp = r2
    while temp:
        print(temp.val, end=' ')
        temp = temp.right
    print()

    #47 42 41 40 44 43 45 46 52 50 49 48 51 64 63 55 53 54 58 56 57 60 59 61 62 77 75 69 68 66 65 67 73 72 71 70 74 76 88 81 79 78 80 87 85 84 83 82 86 94 92 89 90 91 93 100 96 95 99 98 97 102 101 [LEFT FOUND!] 
    #47 42 41 40 44 43 45 46 52 50 49 48 51 64 63 55 53 54 58 56 57 60 59 61 62 77 75 69 68 66 65 67 73 72 71 70 74 76 88 81 79 78 80 87 85 84 83 82 86 94 92 89 90 91 93 100 96 95 99 98 97 102 101 

