#!/usr/bin/env python3
import sys
from LinkedList import LinkedList
from LinkedList import Node

# Merge K Sorted Lists
# https://www.interviewbit.com/problems/merge-k-sorted-lists/
#
# Merge k sorted linked lists and return it as one sorted list.
#
# Example :
#
# 1 -> 10 -> 20
# 4 -> 11 -> 13
# 3 -> 8 -> 9
# will result in
#
# 1 -> 3 -> 4 -> 8 -> 9 -> 10 -> 11 -> 13 -> 20
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        from heapq import heappop, heappush

        heap = list()
        head = tail = None

        # Initilize HEAP (min heap) with first elements of each Linked List in A
        for i in range(len(A)):
            if A[i]:
                heappush(heap, (A[i].val, i))
                #print(heap)
        # End of Initialize HEAP

        # Creates LinkedList with all LinkedList elements from A.
        # POP current smallest from HEAP
        # PUSH current smallest to final LinkedList TAIL
        while heap:
            # POP current smallest element from MIN HEAP
            # Creates NODE to load element
            a, row = heappop(heap)
            node = Node(a)

            # PUSH NODE to new consolidated sorted LinkedList (TAIL)
            if not head:
                head  = tail = node
            else:
                tail.next = node
                tail = node

            # GET an element from one (ROW) of LinkedList in A
            # PUSH element to MIN HEAP
            A[row] = A[row].next
            if A[row]:
                heappush(heap, (A[row].val, row))
                #print(heap)
        # END Creates LinkedList

        return head

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    L1 = LinkedList()
    L1.push(20)
    L1.push(10)
    L1.push(1)
    L2 = LinkedList()
    L2.push(13)
    L2.push(11)
    L2.push(4)
    L3 = LinkedList()
    L3.push(9)
    L3.push(8)
    L3.push(3)
    A = [L1.head, L2.head, L3.head]
    LL = LinkedList()
    LL.head = s.mergeKLists(A)
    LL.print_list()
