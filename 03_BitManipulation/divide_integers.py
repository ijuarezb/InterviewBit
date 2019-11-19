#!/usr/bin/env python3
import sys

# Divide Integers
# https://www.interviewbit.com/problems/divide-integers/
#
# Divide two integers without using multiplication, division and mod operator.
#
# Return the floor of the result of the division.
#
# Example:
#
# 5 / 2 = 2
#
# Also, consider if there can be overflow cases. For overflow case, return INT_MAX.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer

	# Python 3 implementation to Divide two 
	# integers without using multiplication, 
	# division and mod operator 

	# Function to divide a by b and 
	# return floor value it 
	# def divideT(self, dividend, divisor): 

	# 	# Calculate sign of divisor i.e., 
	# 	# sign will be negative only iff 
	# 	# either one of them is negative 
	# 	# otherwise it will be positive 
	# 	sign = -1 if ((dividend < 0) ^ (divisor < 0)) else 1
		
	# 	# Update both divisor and 
	# 	# dividend positive 
	# 	dividend = abs(dividend) 
	# 	divisor = abs(divisor) 
		
	# 	# Initialize the quotient 
	# 	quotient = 0
	# 	while (dividend >= divisor): 
	# 		dividend -= divisor 
	# 		quotient += 1
		
	# 	return sign * quotient 

    # @param A : integer
    # @param B : integer
    # @return an integer
    def divide(self, A, B):
        sign = -1 if ((A < 0) ^ (B < 0)) else 1

        dividend, divisor = abs(A), abs(B)
        quotient = temp = 0

        for i in range(31, -1, -1):
            if temp + (divisor << i) <= dividend:
                temp += (divisor << i)
                quotient |= 1 << i

        return self._bound_result(sign * quotient)

    def _bound_result(self, res):
        if res > (1 << 31) - 1:
            return (1 << 31) - 1
        elif res < -(1 << 32):
            return -(1 << 32)
        else:
            return res

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.divide(1, 2))

    # Driver code 
    a = 10
    b = 3
    print(s.divide(a, b))
    a = 43
    b = -8
    print(s.divide(a, b)) 
