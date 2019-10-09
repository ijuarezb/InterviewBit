#!/usr/bin/env python3
import sys
import math
from BST import TreeNode
from BST import insertNode
from BST import inOrderTraversal
from BST import preOrderTraversal

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#   Serialize a tree from top to bottom, left to right to a list of values
#   Args: 
#     a Tree object, each node has an integer value, and optionally have a left and right children. 
#     The tree is not ordered or balanced, it's just a binary tree
#     example:
#         1
#        / \
#       2   3
#      / \ / \
#        4 2
#   Returns: 
#     a list of serialized values
#     example: [1,2,3,None,4,2,None]
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Get Level Order of the Tree.  It gets a list of lists 
# with each level of the Tree in a ROW.  Row 0 is the Root
# Row 1 would be [2, 3] from your example above.  Row 2
# would be [None 4 2 None]
def level_order(A):
    from collections import deque

    def insert(el, lvl, lst):
        if len(ans) == lvl:
            lst.append([])
        lst[lvl].append(el)


    queue, ans = deque(), list()
    max_level = get_level(A)
    items = pow(2, max_level) - 1

    if A:
        queue.append((0, A))

    while len(queue) > 0:
        lvl, node = queue.popleft()
        if node:
          insert(node.val, lvl, ans)
        else:
          insert(None, lvl, ans)

        if node:
          for child in [node.left, node.right]:
              if child:
                  queue.append((lvl + 1, child))
              else:
                  queue.append((lvl + 1, None))
        elif items > 0:
          queue.append((lvl + 1, None))
          queue.append((lvl + 1, None))

        items -= 1

    return ans[0:max_level]

# Helper function used to get the "number of levels" in a Tree
def get_level(head):
    if head == None:
      return 0
    else:
      return max(get_level(head.left), get_level(head.right)) + 1

# The two functions below were taken from Question 1 to
# flatten the List of list with the Level Order of the Binary Tree
def _flatten_list(nested_list):
    for x in nested_list:
      if isinstance(x, (list, tuple)):
        for y in _flatten_list(x):
          yield y
      else:
        yield x

def flatten_list(nested_list):
    if len(nested_list) < 1:
      return []

    result = _flatten_list(nested_list)
    return list(result)

# class Node:
#   def __init__(self, x):
#     self.val = x
#     self.left = None
#     self.right = None
def serialize_tree(tree):
    levels = level_order(tree)
    return flatten_list(levels)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == '__main__':
    # Input DATA to practice: 11 2 9 13 57 25 17 1 90 3
    #
    #          11
    #        /    \
    #       2      13
    #      / \       \
    #     1   9      57
    #        /      /  \
    #       3      25   90
    #             /
    #            17    

    r = TreeNode(int(sys.argv[1]))
    for arg in range(2, len(sys.argv), 1):
      insertNode(r, TreeNode(int(sys.argv[arg])))
    print(serialize_tree(r))