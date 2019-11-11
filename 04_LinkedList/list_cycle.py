#!/usr/bin/env python3
import sys
from LinkedList import LinkedList
from LinkedList import Node

# List Cycle
# https://www.interviewbit.com/problems/list-cycle/
#
# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
#
# Try solving it using constant additional space.
#
# Example :
#
# Input :
#
#                   ______
#                  |     |
#                  \/    |
#         1 -> 2 -> 3 -> 4
#
# Return the node corresponding to node 3.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        slow = fast = A

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                break
        else:
            return None

        slow = A
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return fast


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
if __name__ == "__main__":
    s = Solution()
    # Driver program for testing 
    llist = LinkedList() 
    llist.push(20) 
    llist.push(4) 
    llist.push(15) 
    llist.push(10) 

    # Create a loop for testing 
    llist.head.next.next.next.next = llist.head 
    print(s.detectCycle(llist.head))
  
# This code is contributed by Nikhil Kumar Singh(nickzuck_007)