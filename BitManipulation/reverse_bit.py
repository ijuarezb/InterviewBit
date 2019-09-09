#!/usr/bin/env python3
import sys

# Reverse Bits
# https://www.interviewbit.com/problems/reverse-bits/
#
# Reverse bits of an 32 bit unsigned integer
#
# Example 1:
#
# x = 0,
#
#           00000000000000000000000000000000
# =>        00000000000000000000000000000000
#
# return 0
#
# Example 2:
#
# x = 3,
#
#           00000000000000000000000000000011
# =>        11000000000000000000000000000000
#
# return 3221225472
#
# Since java does not have unsigned int, use long
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        head, tail = 1 << 31, 1

        for i in range(16):
            not_same = int(A & head > 0) ^ int(A & tail > 0)

            if not_same:
                A = A ^ tail ^ head

            head >>= 1
            tail <<= 1
        return A

    def reverse_ivan(self, A):
    	tail = 1
    	head = 1 << 31
    	reversed_number = 0
    	for i in range(16):
    		reversed_number = reversed_number | (A & tail) << (31 - i*2)
    		reversed_number = reversed_number | (A & head) >> (31 - i*2)
    		tail <<= 1
    		head >>= 1

    	return reversed_number

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    #print(s.reverse(43261596))
    #print(s.reverse(32768))
    print(s.reverse(0))
    print(s.reverse(3))

    #print(s.reverse_ivan(43261596))
    #print(s.reverse_ivan(32768))
    print(s.reverse_ivan(0))
    print(s.reverse_ivan(3))