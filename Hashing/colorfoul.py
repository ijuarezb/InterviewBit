#!/usr/bin/env python2
import sys

# Colorfoul
# https://www.interviewbit.com/problems/colorful-number/
#
# For Given Number N find if its COLORFUL number or not
#
# Return 0/1
#
# COLORFUL number:
#
# A number can be broken into different contiguous sub-subsequence parts. 
# Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245. 
# And this number is a COLORFUL number, since product of every digit of a contiguous subsequence is different
# Example:
#
# N = 23
# 2 3 23
# 2 -> 2
# 3 -> 3
# 23 -> 6
# this number is a COLORFUL number since product of every digit of a sub-sequence are different. 
#
# Output : 1
#

class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        s = str(A)
        d = set()
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                x = reduce(lambda x,y : x*y, map(int, s[i:j])) 
                if x in d:
                    return 0
                else:
                    d.add(x)
                    
        return 1

if __name__ == '__main__':
	s = Solution()
	print(s.colorful(A=23))
	print(s.colorful(A=3245))