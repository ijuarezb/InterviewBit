#!/usr/bin/env python3
import sys


# Excel Column Title
# https://www.interviewbit.com/problems/excel-column-title/
#
# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
#
# For example:
#
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        res = 0
        for char in A:
            diff = ord(char) - ord('A') + 1
            res = res * 26 + diff

        return res

    def numberToTitle(self, A):
        title = ''

        c = (A-1) // 26
        r = (A-1) % 26
        d = chr(r + ord('A'))
        title = d + title

        while c > 0:
            r = (c-1) % 26
            c = (c-1) // 26
            d = chr(r + ord('A'))
            title = d + title

        return title

    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        ans = ''

        while A:
            ans = '{}{}'.format(chr(ord('A') + (A - 1) % 26), ans)
            A = (A - 1) // 26

        return ans


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

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    #print(s.titleToNumber('AA'))
    #print(s.titleToNumber('A'))
    print(s.numberToTitle(1))