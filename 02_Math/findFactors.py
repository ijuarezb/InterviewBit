#!/usr/bin/env python3
import sys
import math

# Python implementation of Naive method 
# to print all divisors 
  
# method to print the divisors 
def printDivisors(n) : 
	i = 1
	L = []
	while i <= math.sqrt(n): 
		if (n % i==0):
			if (n/i == i):
				L.append(i)
			else:
				L.append(i)
				L.append(int(n/i)) 
		i = i + 1
	L.sort()
	return L

# A school method based Python3  
# program to check if a number 
# is prime 
  
def isPrime(n): 
    # Corner case 
    if n <= 1: 
        return False
  
    # Check from 2 to n-1 
    for i in range(2, n): 
        if n % i == 0: 
            return False; 
  
    return True

def isPrimeEfficient(n) : 
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


# Python program to print all primes smaller than or equal to 
# n using Sieve of Eratosthenes 
  
def SieveOfEratosthenes(n): 
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

def binaryRepresentation(A):

	r = A % 2
	c = A / 2
	
	b = '1' if r == 1 else '0'

	while c > 0:
		r = c % 2
		c = c // 2
		a = '1' if r == 1 else '0'
		b = a + b

	return b

  
# driver program 
if __name__=='__main__': 
    n = 16
    print("Following are the prime numbers smaller")
    print("than or equal to", n)
    print(len(SieveOfEratosthenes(16777214)))
    #print(binaryRepresentation(n))

# Driver method 
#print("The divisors of 100 are: ")
#print(printDivisors(100))