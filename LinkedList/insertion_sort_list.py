#!/usr/bin/env python3
import sys
from LinkedList import LinkedList
from LinkedList import Node

# Insertion Sort List
# https://www.interviewbit.com/problems/insertion-sort-list/
#
# Sort a linked list using insertion sort.
#
# We have explained Insertion Sort at Slide 7 of Arrays
#
# Insertion Sort Wiki has some details on Insertion Sort as well.
#
# Example :
#
# Input : 1 -> 3 -> 2
#
# Return 1 -> 2 -> 3
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def insert(self, node, head, end_node):

        tmp = head
        while tmp.next and tmp.next.data < node.data and tmp is not end_node:
            tmp = tmp.next

        node.next = tmp.next
        tmp.next = node

        return node if tmp is end_node else end_node


    # @param A : head node of linked list
    # @return the head node in the linked list
    def insertionSortList(self, A):

        fake_head = Node(None)
        fake_head.next = A

        prev, tmp = fake_head, A

        while tmp:
            prev.next = tmp.next
            prev = self.insert(tmp, fake_head, prev)
            tmp = prev.next

        return fake_head.next

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    LL = LinkedList()
    LL.push(2)
    LL.push(3)
    LL.push(1)
    LL.print_list()
    s.insertionSortList(LL.head)
    LL.print_list()
