#!/usr/bin/env python3
import sys

# Majority Element
# https://www.interviewbit.com/problems/majority-element/
#
# Given an array of size n, find the majority element. The majority element is the element
# that appears more than floor(n/2) times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.
#
# Example :
#
# Input : [2, 1, 2]
# Return  : 2 which occurs 2 times which is greater than 3/2.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        curr, currCnt = None, 0

        for a in A:
            if not currCnt:
                curr, currCnt = a, 1
            elif a == curr:
                currCnt += 1
            else:
                currCnt -= 1
        return curr

    # @param A : tuple of integers
    # @return an integer
    def majorityElement2(self, A):
        if len(A) == 1: return A[0]
        count = 1
        majority_index = 0
        for i in range(1,len(A)):
            if A[majority_index] != A[i]:
                count -= 1
                if count < 1:
                    majority_index = i
                    count = 1
            else:
                count += 1
        return A[majority_index]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #