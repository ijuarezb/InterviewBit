#!/usr/bin/env python3
import sys

#
# https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/
#
# Find a triplet that sum to a given value
#
# Given an array and a value, find if there is a triplet in array whose sum is equal 
# to the given value. If there is such a triplet present in array, then print the triplet and 
# return true. Else return false. For example, if the given array is {12, 3, 4, 1, 6, 9} 
# and given sum is 24, then there is a triplet (12, 3 and 9) present in array whose sum is 24.


# Python3 program to find a triplet using Hashing 
# returns true if there is triplet with sum equal 
# to 'sum' present in A[]. Also, prints the triplet 
def find3Numbers(A, sum): 
	for i in range(len(A)-1): 
		# Find pair in subarray A[i + 1..n-1] 
		# with sum equal to sum - A[i] 
		s = set() 
		curr_sum = sum - A[i] 
		for j in range(i + 1, len(A)): 
			if (curr_sum - A[j]) in s: 
				print("Triplet is", A[i], 
						", ", A[j], ", ", curr_sum-A[j]) 
				return True
			s.add(A[j]) 
	
	return False

# Driver program to test above function 
if __name__ == '__main__':
	A = [1, 4, 45, 6, 10, 8] 
	sum = 22
	find3Numbers(A, sum) 



