#!/usr/bin/env python3
import sys


# Search for a Range
# https://www.interviewbit.com/problems/search-for-a-range/
#
# Given a sorted array of integers, find the starting and ending position of a given target value.
#
# Your algorithm’s runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# Example:
#
# Given [5, 7, 7, 8, 8, 10]
#
# and target value 8,
#
# return [3, 4].
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class solution(object):

	def binary_search_ocurrences(self, A, x, search_first):
		start = 0
		end = len(A)-1
		result = -1
	 
		while start <= end:

			mid = (start + end) // 2

			if A[mid] == x:
				result = mid
				if search_first:
					end = mid - 1 # searching towards the left (lower indices)
				else:
					start = mid + 1 # searching towards the right (higher indices)

			elif A[mid] < x:
				start = mid + 1
			else:
				end = mid - 1

		return result

	def searchRange(self, A, x):
		first_index = self.binary_search_ocurrences(A, x, True)
		if first_index > -1:
			last_index = self.binary_search_ocurrences(A, x, False)
			return [first_index, last_index]
			
		return [-1, -1]



if __name__ == "__main__":
	B = [1,1,3,3,5,5,5,5,5,9,9,11]
	sol = solution()
	print(sol.searchRange(B, 5))