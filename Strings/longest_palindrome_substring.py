#!/usr/bin/env python3
import sys

# Longest Palindromic Substring
# https://www.interviewbit.com/problems/longest-palindromic-substring/
#
# Given a string S, find the longest palindromic substring in S.
#
# Substring of string S:
#
# S[i...j] where 0 <= i <= j < len(S)
#
# Palindrome string:
#
# A string which reads the same backwards. More formally, S is palindrome if reverse(S) = S.
#
# Incase of conflict, return the substring which occurs first ( with the least starting index ).
#
# Example :
#
# Input : "aaaabaaa"
# Output : "aaabaaa"
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class SolutionK:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):
        n, start, max_len = len(A), 0, 1
        dp = [[False] * n for i in range(n)]

        # length 1
        for i in range(n):
            dp[i][i] = True

        # length 2
        for i in range(1, n):
            if A[i] == A[i - 1]:
                dp[i - 1][i] = True
                if max_len < 2:
                    max_len, start = 2, i - 1

        # length > 3
        for k in range(3, n + 1):
            for i in range(n + 1 - k):
                if dp[i + 1][i + k - 2] and A[i] == A[i + k - 1]:
                    dp[i][i + k - 1] = True
                    if k > max_len:
                        max_len, start = k, i

        return A[start:start + max_len]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):

    	PDP = [[False for j in range(len(A))] for i in range(len(A))]
    	i_max_pal = 0
    	max_pal_lenght = 1

    	# Lenght 1
    	for i in range(len(A)):
    		PDP[i][i] = True

    	# Lenght 2
    	for i in range(len(A)-1):
    		if A[i] == A[i+1]:
    			PDP[i][i+1] = True
    			i_max_pal = i
    			max_pal_lenght = 2

    	# Lenght 3 or more
    	current_lenght = 3
    	for current_lenght in range(3, len(A)+1):
    		for i in range(len(A) - current_lenght + 1):
    			j = i + current_lenght - 1
    			if A[i] == A[j] and PDP[i+1][j-1]:
    				PDP[i][j] = True
    				i_max_pal = i
    				max_pal_lenght = current_lenght

    	return A[i_max_pal : i_max_pal+max_pal_lenght]


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome('aa'))