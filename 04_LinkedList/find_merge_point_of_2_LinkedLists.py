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
    # @param B : head node of linked list
    # @return the head node in the linked list
    def getIntersectionNode(self, A, B):
        c1 = self.getLinkedListLenght(A)
        c2 = self.getLinkedListLenght(B)
        d = 0

        if c1 > c2:
            d = c1 - c2
            return self.getIntersectionNodeData(d, A, B)
        else:
            d = c2 - c1
            return self.getIntersectionNodeData(d, B, A)

    def getLinkedListLenght(self, head):
        count = 0
        temp = head

        while temp != None:
            count += 1
            temp = temp.next
        
        return count

    def getIntersectionNodeData(self, d, A, B):
        current1 = A
        current2 = B

        for i in range(d):
            current1 = current1.next

        while current1 != None and current2 != None:
            if current1 == current2:
                return current1
            current1 = current1.next
            current2 = current2.next

        return None

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    A = [4, 1, 1, 2, 1, 3]
    s = Solution()
    # LL = LinkedList()
    # LL.push(7)
    # LL.push(1)
    # LL.push(3)
    # LL.push(2)
    # LL.push(8)
    # LL.print_list()
    # print("the Lenght of LL is {}".format(LL.get_count()))
    # LL.delete_node_index(4)
    # print("the Lenght of LL is {}".format(LL.get_count()))
    # LL.print_list()

    L1 = LinkedList()
    L2 = LinkedList()
    L1.push(10)
    L2.push(3)
    L2.append(6)
    L2.append(9)
    new_node = Node(15)
    L1.head.next = new_node
    L2.head.next.next.next = new_node
    L1.append(30)
    L1.print_list()
    L2.print_list()

    print(s.getIntersectionNode(L1.head, L2.head).data)
