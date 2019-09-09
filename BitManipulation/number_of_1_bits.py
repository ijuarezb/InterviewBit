#!/usr/bin/env python3
import sys

# Number of 1 Bits
# https://www.interviewbit.com/problems/number-of-1-bits/
#
# Write a function that takes an unsigned integer and returns the number of 1 bits it has.
#
# Example:
#
# The 32-bit integer 11 has binary representation
#
# 00000000000000000000000000001011
#
# so the function should return 3.
#
# Note that since Java does not have unsigned int, use long for Java
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        res = 0
        for i in range(32):
            res += A & 1
            A >>= 1
        return res

    def numOfOnes(self, A):
    	ones = 0

    	for b in range(32):
    		if A & (1 << b):
    			ones += 1

    	return ones

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.numSetBits(0))
    print(s.numSetBits(1))
    print(s.numSetBits(3))

    print(s.numOfOnes(0))
    print(s.numOfOnes(1))
    print(s.numOfOnes(3))
