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

    def subtract(self, A):
    	S = [] #Stack
    	temp = middle_node = self.find_mid(A)

    	if middle_node == None:
            return A

    	S.append(middle_node.data)
    	while temp.next != None:
    		temp = temp.next
    		S.append(temp.data)

    	temp = A
    	while len(S) > 0:
    		temp.data = S.pop() - temp.data
    		temp = temp.next

    	return

    # Function to middle node of list. 
    def find_mid(self, head):
    	temp = slow = fast = head

    	while(fast and fast.next):
    		# Advance 'fast' two nodes, and  
    		# advance 'slow' one node
    		slow = slow.next
    		fast = fast.next.next

    	# If number of nodes are odd then update slow 
    	# by slow->next;
    	if fast:
    		slow = slow.next

    	return slow

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
if __name__ == "__main__":
    s = Solution()
    # Driver program for testing 
    llist = LinkedList() 
    llist.push(5) 
    llist.push(4) 
    llist.push(3) 
    llist.push(2)
    llist.push(1)
    llist.print_list() 

    s.subtract(llist.head)
    llist.print_list()