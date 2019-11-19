#!/usr/bin/env python3
import sys

# Remove Duplicates from Sorted Array
# https://www.interviewbit.com/problems/remove-duplicates-from-sorted-array/
#
# Remove duplicates from Sorted Array
# Given a sorted array, remove the duplicates in place such that each element appears only once and return the new length.
#
# Note that even though we want you to return the new length, make sure to change the original array as well in place
#
# Do not allocate extra space for another array, you must do this in place with constant memory.
#
#     Example:
#     Given input array A = [1,1,2],
#     Your function should return length = 2, and A is now [1,2].
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicatesI(self, A):
        i = 0
        while i < len(A) - 1:
            j = i + 1
            while j < len(A) and A[i] == A[j] :
                j += 1
            A[i + 1:j] = []
            i += 1
        return len(A)

    # @param A : list of integers
    # @return an integer
    def removeDuplicatesII(self, A):
        i = 0
        while i < len(A) - 1:
            j = i + 2
            while j < len(A) and A[i] == A[j] :
                j += 1
            A[i + 2:j] = []
            i += 1
        return len(A)

    def removeDuplicatesIJB(self, A):
    	i = 0
    	while i < len(A)-1:
    		j = i + 1
    		while j < len(A) and A[i] == A[j]:
    			del A[j]
    			print(A)
    		i = i + 1
    	return len(A)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
if __name__ == "__main__":
    s = Solution()
    A = [1, 1, 1, 2]
    A = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    #s.removeDuplicates(A)
    print(s.removeDuplicatesIJB(A))
    print(A)