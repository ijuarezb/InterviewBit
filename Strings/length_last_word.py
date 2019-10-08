#!/usr/bin/env python3
import sys

# Length of Last Word
# https://www.interviewbit.com/problems/length-of-last-word/
#
# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a character sequence consists of non-space characters only.
#
# Example:
#
# Given s = "Hello World",
#
# return 5 as length("World") = 5.
#
# Please make sure you try to solve this problem without using library functions. Make sure you only traverse the string once.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : string
    # @return an integer
    def lengthLastWord(self, A):
    	L = A.split()
    	return len(L[-1]) if len(L) > 0 else 0

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.lengthLastWord(""))
    print(s.lengthLastWord("one two three"))