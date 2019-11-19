#!/usr/bin/env python3
import sys

    
# Single Number
# https://www.interviewbit.com/problems/single-number/
#
# Given an array of integers, every element appears twice except for one. Find that single one.
#
# Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#
# Example :
#
# Input : [1 2 2 3 1]
# Output : 3
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        from functools import reduce
        return reduce((lambda x, y: x ^ y), A)

    def singleNumberIvan(self, A):
    	result = A[0]

    	for i in range(1, len(A)):
    		result = result ^ A[i]

    	return result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
if __name__ == "__main__":
    s = Solution()
    print(s.singleNumber([1, 2, 2, 3, 1]))
    print(s.singleNumberIvan([1, 2, 2, 3, 1]))