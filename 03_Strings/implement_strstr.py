#!/usr/bin/env python3
import sys

# Implement StrStr
# https://www.interviewbit.com/problems/implement-strstr/
#
# Please Note:
#
# Another question which belongs to the category of questions which are intentionally stated vaguely.
# Expectation is that you will ask for correct clarification or you will state your assumptions before you start coding.
#
# Implement strStr().
#
#     strstr - locate a substring ( needle ) in a string ( haystack ).
#
# Try not to use standard library string functions for this question.
#
# Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
#     NOTE:
#
#     Good clarification questions:
#
#         What should be the return value if the needle is empty?
#
#         What if both haystack and needle are empty?
#
#     For the purpose of this problem, assume that the return value should be -1 in both cases.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    def strStr(self, A, B):
        import re
        a = re.search(B, A)
        return a.start() if a else -1

    def strstr_ivan(self, A, B):
    	return A.find(B)

    def strstr_lowlevel(self, A, B):
    	i=0

    	if len(A) == 0 or len(B) == 0:
    		return -1

    	while i < len(A) and i+len(B) <= len(A):
    		#print(A[i:len(B)+i])
    		if A[i:len(B)+i] == B:
    			return i
    		i = i + 1

    	return -1



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.strStr('hello', 'll'))
    print(s.strstr_ivan('hello', 'wes'))
    print(s.strstr_lowlevel('b', 'b'))
