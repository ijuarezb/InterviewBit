#!/usr/bin/env python3
import sys

# https://www.interviewbit.com/problems/verify-prime/
#
# Given a number N, verify if N is prime or not.
#
# Return 1 if N is prime, else return 0.
#
# Example :
# Input : 7
# Output : True
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : integer
    # @return an integer
    
    def isPrime(self, n):
    # Corner case 
        if n <= 1: 
            return 0
        if n <= 3:
            return 1
        
        if n % 2 == 0 or n % 3 == 0:
            return 0
  
        i = 5
        while i*i <= n: 
            if n % i == 0 or n % (i+2) == 0: 
                return 0
            i += 6
  
        return 1

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
