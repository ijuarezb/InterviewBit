#!/usr/bin/env python3
import sys

class Solution:
    # @param A : integer
    # @return a list of strings
	def fizzBuzz(self, A):
		FB = []

		for i in range(1, A+1):
			if i % 15 == 0:
				FB.append("FizzBuzz")
			elif i % 3 == 0:
				FB.append("Fizz")
			elif i % 5 == 0:
				FB.append("Buzz")
			else:
				FB.append(i)

		return FB


# driver program 
if __name__=='__main__': 
    A = 15
    sol = Solution()
    print("Following are the prime numbers smaller")
    print("than or equal to", A)
    #print(SieveOfEratosthenes(n))
    print(sol.fizzBuzz(A))