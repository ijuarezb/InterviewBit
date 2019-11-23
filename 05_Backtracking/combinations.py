#!/usr/bin/env python3
import sys

# Combinations
# https://www.interviewbit.com/problems/combinations/
#
# Given two integers n and k, return all possible combinations of k numbers out of 1 2 3 ... n.
#
# Make sure the combinations are sorted.
#
# To elaborate,
#
# Within every entry, elements should be sorted. [1, 4] is a valid entry while [4, 1] is not.
# Entries should be sorted within themselves.
# Example :
# If n = 4 and k = 2, a solution is:
#
# [
#   [1,2],
#   [1,3],
#   [1,4],
#   [2,3],
#   [2,4],
#   [3,4],
# ]
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : integer
    # @param B : integer
    # @return a list of list of integers
    def combine(self, A, B):
    	arr = [i+1 for i in range(A)]
    	# return self._combinations1(arr, [], 0, B)
    	return self._combinations(arr, [], B)

    def _combinations1(self, A, tmp, left, k):
    	if not k: return [tmp[:]]

    	result= []
    	for i in range(left, len(A)):
    		tmp.append(A[i])
    		result.extend(self._combinations1(A, tmp, i+1, k-1))
    		tmp.pop()

    	return result

    def _combinations(self, A, tmp, k):
    	if not k: return [tmp[:]]

    	result= []
    	for i in range(len(A)):
    		tmp.append(A[i])
    		result.extend(self._combinations(A[i+1:], tmp, k-1))
    		tmp.pop()

    	return result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    result = s.combine(5, 3)
    print(result)