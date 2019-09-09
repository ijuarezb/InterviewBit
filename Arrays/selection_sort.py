#!/usr/bin/env python3
import sys

class Sort(object):

	def __init__(self, Arr, arr_size):
		self.Arr = Arr
		self.arr_size = arr_size

	def find_min_index(self, index):
		min_index = index
		for i in range(index+1, self.arr_size):
			if self.Arr[i] < self.Arr[min_index]:
				min_index = i

		return min_index

	def selection_sort(self):
		for i in range(0, self.arr_size):
			min_index = self.find_min_index(i)
			if min_index != i:
				temp = self.Arr[i]
				self.Arr[i] = self.Arr[min_index]
				self.Arr[min_index] = temp

		return self.Arr

# Driver Code 
if __name__ == "__main__": 

	A = [10, 9, 8, 15, 0, 5, 67, 3]
	sol = Sort(A, len(A))
	print("Sorted Array: ", sol.selection_sort())
# This code is contributed by Rituraj Jain 