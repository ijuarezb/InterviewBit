#!/usr/bin/env python3
import sys
#import LinkedList

# K reverse linked list
# https://www.interviewbit.com/problems/k-reverse-linked-list/
#
# Given a singly linked list and an integer K, reverses the nodes of the
#
# list K at a time and returns modified linked list.
#
#     NOTE : The length of the list is divisible by K
#
# Example :
#
# Given linked list 1 -> 2 -> 3 -> 4 -> 5 -> 6 and K=2,
#
# You should return 2 -> 1 -> 4 -> 3 -> 6 -> 5
#
# Try to solve the problem using constant extra space.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def reverseList(self, A, B):
    # swap the List >> in Groups << of B items

        head = last = None
        while A:
            start = A
            prev = A
            A = A.next
            for i in range(1, B):
                next = A.next
                A.next = prev
                prev = A
                A = next
            if last:
                last.next = prev
            last = start

            if not head:
                head = prev
        if last:
            last.next = None

        return head

    def print_list(self, head):
        temp = head
        while  temp:
            print(temp.val, end=' ')
            temp = temp.next
        print("")

    # swap K pairs
    def swapPairs(self, A, B):
        fake_head = ListNode(0)
        fake_head.next = A

        tmp, i = fake_head, 0
        while tmp and tmp.next and tmp.next.next and i < B:
            nxt = tmp.next
            tmp.next = tmp.next.next
            nxt.next = tmp.next.next
            tmp.next.next = nxt

            tmp = tmp.next.next
            i += 1

        return fake_head.next

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == '__main__':
    s = Solution()

    # Given linked list 1 -> 2 -> 3 -> 4 -> 5 -> 6 and K=2,
    # You should return 2 -> 1 -> 4 -> 3 -> 6 -> 5
    n = ListNode(1)
    n.next = ListNode(2)
    n.next.next = ListNode(3)
    n.next.next.next = ListNode(4)
    n.next.next.next.next = ListNode(5)
    n.next.next.next.next.next = ListNode(6)
    s.print_list(n)
    #h = s.swapPairs(n, 2)
    h = s.reverseList(n, 3)
    s.print_list(h)


