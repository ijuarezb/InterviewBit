#!/usr/bin/env python3
import sys
from BST import TreeNode

# Root to Leaf Paths With Sum
# https://www.interviewbit.com/problems/root-to-leaf-paths-with-sum/
#
# Given a binary tree and a sum, find all root-to-leaf paths where each path’s sum equals the given sum.
#
# For example:
# Given the below binary tree and sum = 22,
#
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# return
#
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
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
    def pathSum(self, A, B):
        stack, ans, path, total = list(), list(), list(), 0

        if A:
            stack.append(A)

        while stack:
            node = stack.pop()
            total += node.val
            path.append(node.val)

            if total == B:
            	ans = ans + [path[:]]
            	total -= path[-1]
            	path.pop()

            elif not node.left and not node.right:
            	total -= path[-1]
            	path.pop()

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)            


        return ans

    def _pathSum(self, node, tmp, tmp_sum, s):
        if node is None:
            return []

        tmp.append(node.val)
        tmp_sum += node.val

        if not node.left and not node.right:
            ans = [tmp[:]] if tmp_sum == s else []
        else:
            ans = self._pathSum(node.left, tmp, tmp_sum, s) + self._pathSum(node.right, tmp, tmp_sum, s)

        tmp.pop()
        tmp_sum -= node.val

        return ans

    # @param A : root node of tree
    # @param B : integer
    # @return a list of list of integers
    def pathSum(self, A, B):
        return self._pathSum(A, [], 0, B)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == '__main__':

	s = Soution()
	t = TreeNode(5)
	t.left = TreeNode(4)
	t.left.left = TreeNode(11)
	t.left.left.left = TreeNode(7)
	t.left.left.right = TreeNode(2)
	t.right = TreeNode(8)
	t.right.left = TreeNode(13)
	t.right.right = TreeNode(4)
	t.right.right.left = TreeNode(5)
	t.right.right.right = TreeNode(1)
	print(s.pathSum(t, 22))

#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1


	
