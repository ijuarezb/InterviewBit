#!/usr/bin/env python3
import sys

# Regular Expression Match
# https://www.interviewbit.com/problems/regular-expression-match/
#
# Good reference:
# https://www.youtube.com/watch?v=3ZDZ-N0EPV0
#
# Implement wildcard pattern matching with support for '?' and '*'.
#
# '?' : Matches any single character.
# '*' : Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).
#
# The function prototype should be:
#
# int isMatch(const char *s, const char *p)
# Examples :
#
# isMatch("aa","a") → 0
# isMatch("aa","aa") → 1
# isMatch("aaa","aa") → 0
# isMatch("aa", "*") → 1
# isMatch("aa", "a*") → 1
# isMatch("ab", "?*") → 1
# isMatch("aab", "c*a*b") → 0
# Return 1/0 for this problem.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def isMatch(self, A, B):
        if len(B) - B.count('*') > len(A):
            return 0
        dp = [True] + [False] * len(A)
        for c in B:
            if c == '*':
                for n in range(1, len(A) + 1):
                    dp[n] = dp[n - 1] or dp[n]
            else:
                for n in range(len(A) - 1, -1, -1):
                    dp[n + 1] = dp[n] and (c == A[n] or c == '?')
                dp[0] = dp[0] and c == '*'
        return 1 if dp[-1] else 0

    # @param A : string
    # @param B : string pattern
    # @return an integer
    def regex_match(self, A, B):
    	n, m = len(A), len(B)
    	dp = [[1] + [0]*n] + [[0]*(n+1) for _ in range(m)]

    	for i in range(1, m+1):
    		for j in range(1, n+1):
    			if A[j-1] == B[i-1] or B[i-1] == '?':
    				dp[i][j] = dp[i-1][j-1]
    			elif B[i-1] == '*':
    				dp[i][j] = 1 if dp[i-1][j] or dp[i][j-1] else 0
    			else:
    				dp[i][j] = 0

    	return dp[-1][-1]


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.isMatch('a', '?'))
    print(s.isMatch('cc', '?'))
    print(s.regex_match('a', '?'))
    print(s.regex_match('cc', '?'))

    A = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    B = "*b"
    print(s.isMatch(A,B))
    print(s.regex_match(A, B))