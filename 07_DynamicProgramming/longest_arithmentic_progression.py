#!/usr/bin/env python3
import sys

# Longest Arithmetic Progression
# https://www.interviewbit.com/problems/longest-arithmetic-progression/
#
# Find longest Arithmetic Progression in an integer array and return its length. More
# formally, find longest sequence of indeces, 0 < i1 < i2 < … < ik < ArraySize(0-indexed)
# such that sequence A[i1], A[i2], …, A[ik] is an Arithmetic Progression. Arithmetic
# Progression is a sequence in which all the differences between consecutive pairs are the
# same, i.e sequence B[0], B[1], B[2], …, B[m - 1] of length m is an Arithmetic Progression if
# and only if B[1] - B[0] == B[2] - B[1] == B[3] - B[2] == … == B[m - 1] - B[m - 2].
# Examples
# 1) 1, 2, 3(All differences are equal to 1)
# 2) 7, 7, 7(All differences are equal to 0)
# 3) 8, 5, 2(Yes, difference can be negative too)
#
# Samples
# 1) Input: 3, 6, 9, 12
# Output: 4
#
# 2) Input: 9, 4, 7, 2, 10
# Output: 3(If we choose elements in positions 1, 2 and 4(0-indexed))
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def solve(self, A):
        dp = {}
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                if (i, A[j] - A[i]) in dp:
                    dp[(j, A[j] - A[i])]  = 1 + dp[(i, A[j] - A[i])]
                    del dp[(i, A[j] - A[i])]
                else: dp[(j, A[j] - A[i])] = 1
        ## we now find the maximum count
        return max(dp.values()) + 1 if dp.values() else 1


    def solvI(self, A):
    	dp, lap = {}, 0
    	for i in range(len(A)):
    		for j in range(i+1, len(A)):
    			if (i, A[i] - A[j]) in dp:
    				dp[(j, A[i] - A[j])] = dp[(i, A[i] - A[j])] + 1
    			else:
    				dp[(j, A[i] - A[j])] = 1
    			lap = max(lap, dp[(j, A[i]-A[j])])

    	return lap+1 #max(dp.values()) + 1

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == '__main__':
	s = Solution()
	print(s.solvI([9, 4, 7, 2, 10]))
	print(s.solvI([3, 6, 9, 12]))
	print(s.solvI([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))