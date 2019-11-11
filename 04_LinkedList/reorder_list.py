#!/usr/bin/env python3
import sys
from LinkedList import LinkedList
from LinkedList import Node

# Reorder List
# https://www.interviewbit.com/problems/reorder-list/
#
# Given a singly linked list
#
#     L: L0 → L1 → … → Ln-1 → Ln,
#
# reorder it to:
#
#     L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …
#
# You must do this in-place without altering the nodes’ values.
#
# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def divide(self, A):
        slow = fast = A
        while slow and fast and fast.next:
            fast = fast.next.next
            if fast is None:
                slow.next, slow = None, slow.next
            else:
                slow = slow.next
        else:
            if fast and not fast.next:
                slow.next, slow = None, slow.next

        return slow

    def reverseList(self, A):
        tmp, prev = A, None
        while tmp:
            nxt = tmp.next
            tmp.next = prev
            prev = tmp
            tmp = nxt

        return prev

    # @param A : head node of linked list
    # @return the head node in the linked list
    def reorderList(self, A):

        mid = self.divide(A)
        left, right, i = A, self.reverseList(mid), 1

        while right:
            if i % 2:
                next_left = left.next
                left.next = right
                left = next_left
            else:
                next_right = right.next
                right.next = left
                right = next_right
            i ^= 1
        return A

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
if __name__ == "__main__":
    s = Solution()
    # Driver program for testing 
    L1 = LinkedList() 
    L1.push(1) 
    L1.push(2) 
    L1.push(3)
    L1.push(4)
    L1.push(5)
    L1.push(6)
    L1.print_list()

    r = s.reorderList(L1.head)
    temp = r
    while  temp:
        print(temp.data, end=' ')
        temp = temp.next
    print("")