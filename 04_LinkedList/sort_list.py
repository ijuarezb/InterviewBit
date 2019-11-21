#!/usr/bin/env python3
import sys

# Sort List
# https://www.interviewbit.com/problems/sort-list/
#
# Sort a linked list in O(n log n) time using constant space complexity.
#
# Example :
#
# Input : 1 -> 5 -> 4 -> 3
#
# Returned list : 1 -> 3 -> 4 -> 5
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    # split list, return mid pointer
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

    # find the min of two items
    def min(self, A, B):
        if A is None:
            return B
        elif B is None:
            return A
        else:
            return A.val < B.val and A or B

    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the two linked list merged
    def mergeTwoLists(self, A, B):

        head = tmp = self.min(A, B)

        if head == None:
            return None

        A = A.next if tmp is A else A
        B = B.next if tmp is B else B

        while A or B:
            minn = self.min(A, B)
            tmp.next = minn
            tmp = minn

            A = A.next if tmp is A else A
            B = B.next if tmp is B else B
        return head

    # Merge Sort: sorting algorithm
    def merge_sort(self, A):
        B = self.divide(A)

        if B is None:
            return A

        first = self.merge_sort(A)
        second = self.merge_sort(B)

        return self.mergeTwoLists(first, second)

    # @param A : head node of linked list
    # @return the head node in the linked list
    def sortList(self, A):
        return self.merge_sort(A)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
if __name__ == '__main__':
	main()