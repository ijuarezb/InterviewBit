#!/usr/bin/env python3
import sys

# Diffk
# https://www.interviewbit.com/problems/diffk/
#
# Given an array ‘A’ of sorted integers and another non negative integer k, find if there exists 2
# indices i and j such that A[i] - A[j] = k, i != j.
#
#     Example:
#
#     Input :
#
#     A : [1 3 5]
#     k : 4
#
#     Output : YES
#
#     as 5 - 1 = 4
#
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem
#
# Try doing this in less than linear space complexity.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        i, j = 0, 1

        while j < len(A):
            diff = A[j] - A[i]
            if diff == B:
                return 1
            elif diff > B:
                i += 1
                j += (i == j)
            else:
                j += 1
        return 0

    def diffk(self, A, B):
        k = len(A) - 1
        for i in range(len(A)):
            for j in range(k, i, -1):
                if i != j and A[j] - A[i] == B:
                    return 1
                if A[j] - A[i] < B:
                #    k = j
                    break
        return 0

# A : [ 0, 1, 9, 10, 13, 17, 17, 17, 23, 25, 29, 30, 37, 38, 39, 39, 40, 41, 42, 60, 64, 70, 70, 70, 72, 75, 85, 85, 90, 91, 91, 93, 95 ]
# B : 83

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    A = [ 0, 1, 9, 10, 13, 17, 17, 17, 23, 25, 29, 30, 37, 38, 39, 39, 40, 41, 42, 60, 64, 70, 70, 70, 72, 75, 85, 85, 90, 91, 91, 93, 95 ]
    s = Solution()
    print(s.diffPossible(A, 83))
    print(s.diffk(A, 83))