#!/usr/bin/env python3
import sys

# Diffk II
# https://www.interviewbit.com/problems/diffk-ii/
#
# Given an array A of integers and another non negative integer k, find if there exists 2 indices
# i and j such that A[i] - A[j] = k, i != j.
#
# Example :
#
# Input :
#
# A : [1 5 3]
# k : 2
# Output :
#
# 1
# as 3 - 1 = 2
#
# Return 0 / 1 for this problem.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        from collections import defaultdict
        dp = defaultdict(lambda: 0)
        for a in A:
            if dp[B + a] + dp[a - B] > 0:
                return 1
            dp[a] += 1
        return 0

    def twoDiff(self, A, B):
        dp = dict()

        for i, a in enumerate(A):
            if a in dp:
                print(a)
                return 1
            if B + a not in dp:
                dp[B + a] = i
        return 0

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == '__main__':
    s = Solution()
    print(s.diffPossible([11, 85, 100, 44, 3, 32, 96, 72, 93, 76, 67, 93, 63, 5, 10, 45, 99, 35, 13], 60))
    print(s.twoDiff([ 77, 28, 19, 21, 67, 15, 53, 25, 82, 52, 8, 94, 50, 30, 37, 39, 9, 43, 35, 48, 82, 53, 16, 20, 13, 95, 18, 67, 77, 12, 93, 0 ], 0))