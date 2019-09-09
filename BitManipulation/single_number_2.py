#!/usr/bin/env python3
import sys


# Single Number II
# https://www.interviewbit.com/problems/single-number-ii/
#
# Given an array of integers, every element appears thrice except for one which occurs once.
#
# Find that element which does not appear thrice.
#
# Note: Your algorithm should have a linear runtime complexity.
#
# Could you implement it without using extra memory?
#
# Example :
#
# Input : [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
# Output : 4
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        ones = twos = 0

        for a in A:
            twos |= ones & a
            ones = ones ^ a
            threes = ones & twos
            ones &= ~threes
            twos &= ~threes

        return ones

    def getSingle(self, arr) : 
      
	    # Initialize result 
	    result = 0
	    n = len(arr)
	      
	    # Iterate through every bit 
	    for i in range(0, 32) : 
	          
	        # Find sum of set bits  
	        # at ith position in all  
	        # array elements 
	        sm = 0
	        x = (1 << i) 
	        for j in range(0, n) : 
	            if (arr[j] & x) : 
	                sm = sm + 1
	                  
	        # The bits with sum not  
	        # multiple of 3, are the 
	        # bits of element with  
	        # single occurrence. 
	        if (sm % 3) : 
	            result = result | x 
	      
	    return result 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.singleNumber([1, 2, 4, 3, 3, 2, 2, 3, 1, 1]))
    print(s.getSingle([1, 2, 4, 3, 3, 2, 2, 3, 1, 1]))
