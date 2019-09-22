#!/usr/bin/env python3
import sys

# Highest Product
# https://www.interviewbit.com/problems/highest-product/
#
# Given an array of integers, return the highest product possible by multiplying 3 numbers from the array
#
# Input:
#
# array of integers e.g {1, 2, 3}
#  NOTE: Solution will fit in a 32-bit signed integer
# Example:
#
# [0, -1, 3, 100, 70, 50]
#
# => 70*50*100 = 350000
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxp3(self, A):
        A.sort()

        return max(
            A[0] * A[1] * A[-1],
            A[-1] * A[-2] * A[-3]
        )

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #