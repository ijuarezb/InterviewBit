#!/usr/bin/env python3
import sys

# Add Binary Strings
# https://www.interviewbit.com/problems/add-binary-strings/
#
# Given two binary strings, return their sum (also a binary string).
#
# Example:
#
# a = "100"
#
# b = "11"
#
# Return a + b = “111”.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
        ia, ib = len(A) - 1, len(B) - 1
        ans, ext = '', 0


        while ia >= 0 or ib >= 0:
            pa = 0 if ia < 0 else ord(A[ia]) - ord('0')
            pb = 0 if ib < 0 else ord(B[ib]) - ord('0')

            ans = "{}{}".format((pa + pb + ext) % 2, ans)
            ext = (pa + pb + ext) // 2

            ia, ib = ia - 1, ib - 1

        return "{}{}".format('1' if ext else '', ans)

    def addBinaryString(self, A, B):
        ia = len(A) - 1
        ib = len(B) - 1
        car = 0
        result = ''

        while ia >= 0 or ib >= 0:
            ba = 0 if ia < 0 else ord(A[ia]) - ord('0')
            bb = 0 if ib < 0 else ord(B[ib]) - ord('0')

            result = "{}{}".format((ba + bb + car) % 2, result)
            car = (ba + bb + car) // 2

            ia = ia - 1
            ib = ib - 1
        
        return "{}{}".format('1' if car else '', result)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.addBinaryString("1", "1111101"))