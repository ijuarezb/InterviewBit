#!/usr/bin/env python3
import sys

# Prime Sum
# https://www.interviewbit.com/problems/prime-sum/
#
# Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to given number.
#
# NOTE A solution will always exist. read Goldbach’s conjecture
#
# Example:
#
#
# Input : 4
# Output: 2 + 2 = 4
#
# If there are more than one solutions possible, return the lexicographically smaller solution.
#
# If [a, b] is one solution with a <= b,
# and [c, d] is another solution with c <= d, then
#
# [a, b] < [c, d]
#
# If a < c OR a==c AND b < d.
#
# This problem’s solution is straight forward.
# Generate prime numbers less than N, and hash them in a list. 
# Then iterate on the whole list, and for every prime P, check if N-P is also prime. If you find such a pair, you are done :)
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:

    def primesum(self, n):
        #for i in range(2, n):
        #    if self.is_prime(i) and self.is_prime(n - i):
        #        return i, n - i

        if n <= 2:
            return False

        L = self.SieveOfEratosthenes(100)
        for p in L:
            if self.isPrimeEfficient(n-p):
                return p, n-p

    def primesum(self, n):
        #for i in range(2, n):
        #    if self.is_prime(i) and self.is_prime(n - i):
        #        return i, n - i

        if n <= 2:
            return False

        for i in range(2, n):
            L = self.SieveOfEratosthenes(i)
            for p in L:
                if self.isPrimeEfficient(n-p):
                    return p, n-p


    def SieveOfEratosthenes(self,n): 
        # Create a boolean array "prime[0..n]" and initialize 
        #  all entries it as true. A value in prime[i] will 
        # finally be false if i is Not a prime, else true. 
        prime = [True for i in range(n+1)] 
        p = 2
        while (p * p <= n): 
              
            # If prime[p] is not changed, then it is a prime 
            if (prime[p] == True): 
                  
                # Update all multiples of p 
                for i in range(p * p, n+1, p): 
                    prime[i] = False
            p += 1
        L = []      
        # Print all prime numbers 
        for p in range(2, n): 
            if prime[p]: 
                L.append(p)
        return L

    def isPrimeEfficient(self, n): 
        # Corner cases 
        if (n <= 1) : 
            return False
        if (n <= 3) : 
            return True
      
        # This is checked so that we can skip  
        # middle five numbers in below loop 
        if (n % 2 == 0 or n % 3 == 0) : 
            return False
      
        i = 5
        while(i * i <= n) : 
            if (n % i == 0 or n % (i + 2) == 0) : 
                return False
            i = i + 6
      
        return True

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.primesum(4))
    #print(s.primesum(84))