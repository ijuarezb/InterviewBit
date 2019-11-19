#!/usr/bin/env python3
import sys

    
# Remove Element from Array
# https://www.interviewbit.com/problems/remove-element-from-array/
#
# Remove Element
#
# Given an array and a value, remove all the instances of that value in the array.
# Also return the number of elements left in the array after the operation.
# It does not matter what is left beyond the expected length.
#
#     Example:
#     If array A is [4, 1, 1, 2, 1, 3]
#     and value elem is 1,
#     then new length is 3, and A is now [4, 2, 3]
#
# Try to do it in less than linear additional space complexity.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):
        i = 0
        for a in A:
            if a != B:
                A[i], i = a, i + 1
        return i

    def removeElementIJB(self, A, B):
    	i = 0
    	for e in A:
    		if e != B:
    			A[i], i = e, i + 1
    	return i

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    A = [4, 1, 1, 2, 1, 3]
    s = Solution()
    print(s.removeElementIJB(A, 1))
    print(A)