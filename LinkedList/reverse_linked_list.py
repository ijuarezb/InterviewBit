#!/usr/bin/env python3
import sys
from LinkedList import LinkedList
from LinkedList import Node
  
# Remove Element from Array
# https://www.interviewbit.com/problems/remove-element-from-array/
#
# Remove Element
#
# Given an array and a value, remove all the instances of that value in the array.
# Also return the number of elements left in the array after the operation.
# It does not matter what is left beyond the expected length.
#
#     Example:
#     If array A is [4, 1, 1, 2, 1, 3]
#     and value elem is 1,
#     then new length is 3, and A is now [4, 2, 3]
#
# Try to do it in less than linear additional space complexity.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reverseList(self, A):
        current_node = A
        next_node = None
        prev_node = None

        while  current_node != None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        return prev_node

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    A = [4, 1, 1, 2, 1, 3]
    s = Solution()
    LL = LinkedList()
    LL.push(7)
    LL.push(1)
    LL.push(3)
    LL.push(2)
    LL.push(8)
    LL.print_list()
    print("the Lenght of LL is {}".format(LL.get_count()))
    LL.delete_node_index(4)
    print("the Lenght of LL is {}".format(LL.get_count()))
    LL.print_list()
    LL.head = s.reverseList(LL.head)
    LL.print_list()
