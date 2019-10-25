#!/usr/bin/env python3
import sys

# Max Sum Path in Binary Tree
# https://www.interviewbit.com/problems/max-sum-path-in-binary-tree/
#
# Given a binary tree, find the maximum path sum.
#
# The path may start and end at any node in the tree.
#
# Example :
# Given the below binary tree,
#        1
#       / \
#      2   3
# Return 6.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:

    def maxPathSum(self, node):
        if node is None:
            return -float('inf')

        max_sum_left = self.maxPathSum(node.left)
        max_sum_right = self.maxPathSum(node.right)

        sum_left = node.left and node.left.max_sum or 0
        sum_right = node.right and node.right.max_sum or 0
        print(sum_left, sum_right)

        node.max_sum = max(sum_left + node.val, sum_right + node.val, node.val)

        return max(max_sum_left, max_sum_right, sum_left + sum_right + node.val, node.max_sum)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Driver code
if __name__ == '__main__':
    s = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(s.maxPathSum(root))

    # Input DATA to practice: 1 2 3 4 2
	#    1
	#   / \
	#  2   3
	# / \ / \
	#   4 2
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(2)
    print(s.maxPathSum(root))

    # Input DATA to practice: 11 2 9 13 57 25 17 1 90 3
    #          11
    #        /    \
    #       2      13
    #      / \       \
    #     1   9      57
    #        /      /  \
    #       3      25   90
    #             /
    #            17  
    root = TreeNode(11)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(9)
    root.left.right.left = TreeNode(3)
    root.right = TreeNode(13)
    root.right.right = TreeNode(57)
    root.right.right.left = TreeNode(25)
    root.right.right.left.left = TreeNode(17)
    root.right.right.right = TreeNode(90)
    print(s.maxPathSum(root))
