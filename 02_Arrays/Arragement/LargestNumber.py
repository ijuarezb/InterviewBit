#!/usr/bin/env python3
import sys

class Solution:
    # @param A : tuple of integers
    # @return a strings

    def my_compare(self, a, b):
    	ab = str(a) + str(b)
    	ba = str(b) + str(a)
    	return ((int(ba) > int(ab)) - (int(ba) < int (ab)))

    def poly_compare(self, poly):

    	class K(object):
    		def __init__(self, obj, *args):
    			self.obj = obj
    		def __lt__(self, other):
    			return poly(self.obj, other.obj) < 0
    		def __gt__(self, other):
    			return poly(self.obj, other.obj) > 0
    		def __eq__(self, other):
    			return poly(self.obj, other.obj) == 0
    		def __le__(self, other):
    			return poly(self.obj, other.obj) <= 0
    		def __ge__(self, other):
    			return poly(self.obj, other.obj) >= 0
    		def __ne__(self, other):
    			return poly(self.obj, other.obj) != 0
    	return K

    def largestNumber(self, A):
    	B = []

    	for n in A:
    		B.append(str(n))
    	B.sort(reverse=True)
    	if B[0] == '0':
    		return '0'

    	B = sorted(A, key=self.poly_compare(self.my_compare))
    	number = "".join([str(i) for i in B])
    	return number

def num_to_str(A):
	B = []
	for i in range(len(A)):
		B.append(str(A[i]))
	return B

#driver code
if __name__ == "__main__":
	A = [1, 2, 3, 4, 1001, 65, 9]
	#A = [3, 30, 34, 5, 9]
	#A = [0, 0, 0]
	B = num_to_str(A)

	#A.sort(reverse=True)
	print(A)
	print(B)
	B.sort(reverse=True)
	print(B)
	sol = Solution()
	print("the largest number is: ", sol.largestNumber(A)) 