
#!/usr/bin/env python3
import sys

# Minimize the absolute difference
# https://www.interviewbit.com/problems/minimize-the-absolute-difference/
#
# Given three sorted arrays A, B and C of not necessarily same sizes.
#
# Calculate the minimum absolute difference between the maximum and minimum number from the triplet a, b, c
# such that a, b, c belongs arrays A, B, C respectively.
#
# i.e. minimize | max(a,b,c) - min(a,b,c) |.
#
# Example :
#
# Input:
#
# A : [ 1, 4, 5, 8, 10 ]
# B : [ 6, 9, 15 ]
# C : [ 2, 3, 6, 6 ]
#
# Output:
#
# 1
#
# Explanation: We get the minimum difference for a=5, b=6, c=6 as | max(a,b,c) - min(a,b,c) | = |6-5| = 1.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, k):
        n = len(A)
        B = []

        B = sorted(A)
        return B[k-1]
        


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    A = [ 1, 4, 5, 8, 10 ]
    B = [ 6, 9, 15 ]
    C = [ 2, 3, 6, 6 ]

    s = Solution()
    print(s.solve(A, B, C))