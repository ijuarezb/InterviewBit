#!/usr/bin/env python3
import sys

# Fraction
# https://www.interviewbit.com/problems/fraction/
#
# Given two integers representing the numerator and denominator of a fraction, 
# return the fraction in string format.
#
# If the fractional part is repeating, enclose the repeating part in parentheses.
#
# Example 1:
# Input: numerator = 1, denominator = 2
# Output: "0.5"
#
# Example 2:
# Input: numerator = 2, denominator = 1
# Output: "2"
#
# Example 3:
# Input: numerator = 2, denominator = 3
# Output: "0.(6)"
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param numerator : integer
    # @param denominator : integer
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        if denominator == 0:
            return "NaN"
            
        if numerator * denominator >= 0:
            positive = True
        else:
            positive = False
        
        num = abs(numerator)
        den = abs(denominator)
        result = str(num//den)
        rem = num % den
        if not rem: return result
        
        d = {}
        result += '.'
        
        i = len(result)
        while rem:
            #print(rem, result, d)
            num = rem * 10
            digit = str(num//den)
            
            if rem in d:
                result = result[:d[rem]] + "(" + result[d[rem]:] + ")"
                break
            else:
                result += digit
                d[rem] = i
            
            rem = num % den
            i += 1
        
        return result if positive else "-" + result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == '__main__':
	s = Solution()
	# print(s.fractionToDecimal(10,3))
	# print(s.fractionToDecimal(1,2))
	print(s.fractionToDecimal(-2,1))
	# print(s.fractionToDecimal(2,3))
	# print(s.fractionToDecimal(4,9))
	print(s.fractionToDecimal(4,333))
	print(s.fractionToDecimal(4,9))
	# print(s.fractionToDecimal(7,-6))



