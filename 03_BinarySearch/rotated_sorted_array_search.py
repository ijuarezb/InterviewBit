#!/usr/bin/env python3
import sys

# Rotated Sorted Array Search
# https://www.interviewbit.com/problems/rotated-sorted-array-search/
#
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2 ).
#
# You are given a target value to search. If found in the array, return its index,
# otherwise return -1.
#
# You may assume no duplicate exists in the array.
#
# Input : [4 5 6 7 0 1 2] and target = 4
# Output : 0
#
#         NOTE : Think about the case when there are duplicates. Does your current solution work?
#                How does the time complexity change?*
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class solution(object):

	def binary_search(self, A, x):
		start = 0
		end = len(A)-1
	 
		while start <= end:

			mid = (start + end) // 2

			if A[mid] == x:
				return mid
			elif A[mid] < x:
				start = mid + 1
			else:
				end = mid - 1

		return -1

	def find_rotation_count(self, A):
		start = 0
		end = len(A) - 1
		n = len(A)

		while start <= end:
			if A[start] <= A[end]:  # Case 1
				return start
			mid = (start + end) // 2
			next_pointer = (mid + 1) % n
			prev_pointer = (mid + n - 1) % n

			if A[mid] <= A[next_pointer] and A[mid] <= A[prev_pointer]: # Case 2
				return mid
			elif A[mid] <= A[end]: # Case 3
				end = mid - 1
			elif A[mid] >= A[start]: # Case 4
				start = mid + 1
			pass

		return -1

	def search(self, A, x):
		pivot = self.find_rotation_count(A)

		start = 0
		end = pivot - 1

		result = self.binary_search(A[start:end+1], x)

		if result == -1:
			result = self.binary_search(A[pivot:len(A)], x)
			if result != -1:
				return pivot + result

		return result

if __name__ == "__main__":
	A = [4,5,6,7,0,1,2]
	sol = solution()
	result = sol.search(A,4)
	print("{} was found in index {}".format(4,result))
