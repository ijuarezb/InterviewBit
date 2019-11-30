#!/usr/bin/env python3
import sys
from BST import TreeNode
from BST import insertNode

# Populate Next Right Pointers Tree
# https://www.interviewbit.com/problems/populate-next-right-pointers-tree/
#
# Given a binary tree
#
#     struct TreeLinkNode {
#       TreeLinkNode *left;
#       TreeLinkNode *right;
#       TreeLinkNode *next;
#     }
# Populate each next pointer to point to its next right node. If there is no next right node, 
# the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.
#
#  Note:
# You may only use constant extra space.
# Example :
#
# Given the following binary tree,
#
#          1
#        /  \
#       2    3
#      / \  / \
#     4  5  6  7
# After calling your function, the tree should look like:
#
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \  / \
#     4->5->6->7 -> NULL
#  Note 1: that using recursion has memory overhe
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for a  binary tree node
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, A):
        if not A:
            return

        from collections import deque, OrderedDict

        def insert(node, lvl, lst):
            if len(levels) == lvl:
                lst[lvl] = node
                lst[lvl].next = None
            else: 
            	lst[lvl].next = node
            	lst[lvl] = lst[lvl].next
            	lst[lvl].next = None


        queue, ans, levels = deque(), list(), OrderedDict()

        if A:
            queue.append((0, A))

        while len(queue) > 0:
            lvl, node = queue.popleft()
            insert(node, lvl, levels)

            for child in [node.left, node.right]:
                if child:
                    queue.append((lvl + 1, child))

        return levels

    def connect(self, root):
        if not root:
            return

        curr, first_in_row, prev = root, None, None

        while curr:
            while curr:
                if curr.left:
                    if not prev:
                        first_in_row = curr.left
                    else:
                        prev.next = curr.left
                    prev = curr.left

                if curr.right:
                    if not prev:
                        first_in_row = curr.right
                    else:
                        prev.next = curr.right
                    prev = curr.right

                curr = curr.next

            curr = first_in_row
            prev = first_in_row = None

    # Connects Nodes in the same level, to the RIGHT!!!
    # Successful according with LeeCode!!!
    # Comment: Good Speed and Memory Usage
    def connect(self, tree):
        """
        :type tree: Node
        :rtype: Node
        """
        if tree is None:
            return

        queue = []
        queue.append((tree, 0))
        levels = self.get_level(tree)
        level_next_ptr = [None for _ in range(levels)]
        next_ptrs = [None for _ in range(levels)]

        while len(queue) > 0:
            n = queue.pop(0)
            if n:

                n[0].next = None
                if level_next_ptr[n[1]]:
                    level_next_ptr[n[1]].next = n[0]
                else:
                    next_ptrs[n[1]] = n[0]
                level_next_ptr[n[1]] = n[0]

                if n[0].left: queue.append((n[0].left, n[1] + 1))
                if n[0].right: queue.append((n[0].right, n[1] + 1))

        return tree
    
    def get_level(self, head):
        if head == None:
            return 0
        else:
            return max(self.get_level(head.left), self.get_level(head.right)) + 1

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == '__main__':
	# Input DATA to practice: 11 2 9 13 57 25 17 1 90 3
    r = TreeNode(int(sys.argv[1]))
    for arg in range(2, len(sys.argv), 1):
    	insertNode(r, TreeNode(int(sys.argv[arg])))

    # Print inoder traversal of the BST 
    s = Solution()
    D = s.connect(r)
    for level, node in D.items():
        print(D[level].val, end=' ')
    print()
    for level, node in D.items():
        print(D[level].next, end=' ')
    print()

    # 43 621367 400139 986434 318453 562082 727076 -1 208016 340383 409269 -1 702531 983736 187691 -1 -1 387077 -1 534779 647033 719463 824451 -1 -1 -1 373900 -1 517606 -1 -1 -1 -1 720965 -1 834145 -1 -1 -1 -1 -1 -1 -1 -1
    # 387077 340383 562082 409269 517606 534779 986434 702531 720965 647033 727076 NULL 719463 983736 824451 834145 NULL NULL NULL NULL NULL 
    # 387077 340383 562082 409269 517606 534779 986434 702531 720965 647033 727076 NULL 719463 983736 824451 834145 NULL NULL NULL NULL NULL
    # 189 838142 79327 850082 78362 664467 -1 973809 56042 79117 326663 773985 899271 976568 40359 69725 -1 -1 134531 603123 760369 826902 862205 959993 -1 -1 32358 50782 66899 73260 114761 298159 545464 604554 678183 762219 780090 831066 -1 868662 951588 -1 9679 33090 -1 51208 -1 -1 -1 -1 103548 -1 255457 311604 357548 548587 603382 633869 671177 689824 -1 773186 776851 792094 -1 -1 -1 -1 -1 -1 9608 28853 -1 -1 -1 -1 87854 -1 196521 274844 -1 -1 344728 462110 -1 599430 -1 -1 619311 646060 667529 -1 681109 747257 -1 -1 -1 -1 784081 -1 -1 -1 16653 -1 -1 100198 187605 209762 -1 -1 -1 -1 379623 477976 585788 602218 616193 -1 -1 -1 -1 -1 -1 684882 -1 -1 -1 -1 15442 26527 -1 -1 180722 -1 -1 -1 377684 398392 468700 507966 -1 -1 -1 -1 610117 -1 -1 -1 -1 -1 23983 -1 161326 -1 -1 -1 -1 415961 -1 -1 491819 509566 -1 -1 -1 -1 -1 168956 411487 -1 -1 492019 -1 -1 -1 171862 -1 412294 -1 498100 -1 177068 -1 -1 -1 -1 172344 -1 -1 -1
    # 28853 33090 26527 100198 161326 180722 87854 50782 51208 69725 66899 103548 79117 73260 134531 114761 664467 326663 850082 196521 187605 255457 298159 603123 415961 411487 412294 NULL NULL 377684 209762 274844 379623 311604 344728 545464 357548 773985 462110 548587 398392 477976 468700 492019 498100 491819 599430 507966 585788 509566 NULL NULL 610117 NULL 604554 603382 602218 619311 616193 760369 633869 678183 NULL 684882 646060 671177 667529 973809 681109 689824 762219 747257 NULL 773186 784081 826902 780090 776851 899271 792094 831066 NULL NULL 862205 868662 NULL NULL 959993 951588 976568 NULL NULL NULL NULL 