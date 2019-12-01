#!/usr/bin/env python3
import sys
from BST import TreeNode
from BST import insertNode
from BST import inOrderTraversal

# BST Iterator
# https://www.interviewbit.com/problems/bst-iterator/
#
# Implement an iterator over a binary search tree (BST). Your iterator will be initialized
# with the root node of a BST.
#
# The first call to next() will return the smallest number in BST. Calling next() again will
# return the next smallest number in the BST, and so on.
#
#  Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h
# is the height of the tree.
# Try to optimize the additional space complexity apart from the amortized time complexity.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary s):earch tree's root node
    def __init__(self, root):
        self.stack = list()
        if root:
            self.stack.append(root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return len(self.stack) > 0

    # @return an integer, the next smallest number
    def next(self):
        ans = None
        while ans is None:
            node = self.stack[-1]
            if not node.left or hasattr(node.left, 'visited'):
                node.visited = True
                ans = self.stack.pop().val

                if node.right:
                    self.stack.append(node.right)
            else:
                self.stack.append(node.left)
        return ans

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Your BSTIterator will be called like this:
# i = BSTIterator(root)
# while i.hasNext(): print(i.next()),

if __name__ == '__main__':
    # A = [11 2 9 13 57 25 17 1 90 3]; B = 5; Answer = 11

    r = TreeNode(int(sys.argv[1]))
    for arg in range(2, len(sys.argv), 1):
        insertNode(r, TreeNode(int(sys.argv[arg])))

    i = BSTIterator(r)
    print(i.next())    # return 1
    print(i.next())    # return 2
    print(i.hasNext()) # return true
    print(i.next())    # return 3
    print(i.hasNext()) # return true
    print(i.next())    # return 9
    print(i.hasNext()) # return true
    print(i.next())    # return 11
    print(i.hasNext()) # return false
    print(i.next())    # return 13
    print(i.hasNext()) # return true
    print(i.next())    # return 17
    print(i.hasNext()) # return false
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #