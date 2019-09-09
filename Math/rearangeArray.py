#!/usr/bin/env python3
import sys

class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference. 
    # You do not need to return anything in this case. 
    def arrange(self, arr):
    	# The function to rearrange an 
		# array in-place so that arr[i] 
		# becomes arr[arr[i]]. 
	    n = len(arr)
  
	    # First step: Increase all values 
	    # by (arr[arr[i]] % n) * n 
	    for i in range(0, n): 
	        arr[i] += (arr[arr[i]] % n) * n 
	  
	    # Second Step: Divide all values 
	    # by n 
	    for i in range(0, n): 
	        arr[i] = int(arr[i] / n) 

	    return arr


# driver program 
if __name__=='__main__': 
    A = [4, 0, 2, 1, 3]
    sol = Solution()
    print("Following are the prime numbers smaller")
    print("than or equal to", A)
    #print(SieveOfEratosthenes(n))
    print(sol.arrange(A))