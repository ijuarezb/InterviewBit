#!/usr/bin/env python3
import sys

# https://www.interviewbit.com/problems/inversions/
#
# Given an array A, count the number of inversions in the array.
# Formally speaking, two elements A[i] and A[j] form an inversion if A[i] > A[j] and i < j
#
# Example:
# A : [2, 4, 1, 3, 5]
# Output : 3
# as the 3 inversions are (2, 1), (4, 1), (4, 3).
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : list of integers
    # @return an integer
    # >>> n^2 solution <<<
	def countInversions(self, A):
	    inversions, tmp = 0, 0
	    n = len(A)
	    if n == 2 and A[0] > A[1]:
	        return 1
	    
	    while i < n-1:
	        for j in range(i+1, n):
	            if A[i] > A[j]:
	                inversions += 1
	        i += 1
	        
	    return inversions


	# >>> nlog(n) solution <<<
    # Python 3 program to count inversions in an array 
	# Function to Use Inversion Count
	# This code is contributed by ankush_953  
	def mergeSort(self, A): 
		# A temp_arr is created to store 
		# sorted array in merge function
		n = len(A) 
		temp_arr = [0]*n 
		return self._mergeSort(A, temp_arr, 0, n-1) 

	# This Function will use MergeSort to count inversions 
	def _mergeSort(self, arr, temp_arr, left, right): 
		# A variable inv_count is used to store 
		# inversion counts in each recursive call 
		inv_count = 0

		# We will make a recursive call if and only if 
		# we have more than one elements 
		if left < right: 
			# mid is calculated to divide the array into two subarrays 
			# Floor division is must in case of python 
			mid = (left + right)//2

			# It will calculate inversion counts in the left subarray 
			inv_count = self._mergeSort(arr, temp_arr, left, mid) 

			# It will calculate inversion counts in right subarray 
			inv_count += self._mergeSort(arr, temp_arr, mid + 1, right) 

			# It will merge two subarrays in a sorted subarray 
			inv_count += self._merge(arr, temp_arr, left, mid, right) 
		return inv_count 

	# This function will merge two subarrays in a single sorted subarray 
	def _merge(self, arr, temp_arr, left, mid, right): 
		i = left	 # Starting index of left subarray 
		j = mid + 1 # Starting index of right subarray 
		k = left	 # Starting index of to be sorted subarray 
		inv_count = 0

		# Conditions are checked to make sure that i and j don't exceed their 
		# subarray limits. 
		while i <= mid and j <= right: 

			# There will be no inversion if arr[i] <= arr[j] 
			if arr[i] <= arr[j]: 
				temp_arr[k] = arr[i] 
				k += 1
				i += 1
			else: 
				# Inversion will occur. 
				temp_arr[k] = arr[j] 
				inv_count += (mid-i + 1) 
				k += 1
				j += 1

		# Copy the remaining elements of left subarray into temporary array 
		while i <= mid: 
			temp_arr[k] = arr[i] 
			k += 1
			i += 1

		# Copy the remaining elements of right subarray into temporary array 
		while j <= right: 
			temp_arr[k] = arr[j] 
			k += 1
			j += 1

		# Copy the sorted subarray into Original array 
		for loop_var in range(left, right + 1): 
			arr[loop_var] = temp_arr[loop_var] 
			
		return inv_count 


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
if __name__ == '__main__':
	s = Solution()
	A = [ 84, 2, 37, 3, 67, 82, 19, 97, 91, 63, 27, 6, 13, 90, 63, 89, 100, 60, 47, 96, 54, 26, 64, 50, 71, 16, 6, 40, 84, 93, 67, 85, 16, 22, 60 ]
	# expected output 290
	A = [ 84, 2, 37, 3, 67, 82, 19, 97, 91, 63, 27, 6, 13, 90, 63, 89, 100, 60, 47, 96, 54, 26, 64, 50, 71, 16, 6, 40, 84, 93, 67, 85, 16, 22, 60 ]

	arr = [1, 20, 6, 4, 5] 
	result = s.mergeSort(arr) 
	print("Number of inversions are", result)
	result = s.mergeSort(A) 
	print("Number of inversions are", result)

