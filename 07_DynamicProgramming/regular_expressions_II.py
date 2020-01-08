#!/usr/bin/env python3
import sys

# Regular Expression II
# https://www.interviewbit.com/problems/regular-expression-ii/
#
# Good Reference:
# https://www.youtube.com/watch?v=l3hda49XcDE
#
# Implement regular expression matching with support for '.' and '*'.
#
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
#
# The matching should cover the entire input string (not partial).
#
# The function prototype should be:
#
# int isMatch(const char *s, const char *p)
#
# Some examples:
#
# isMatch("aa","a") → 0
# isMatch("aa","aa") → 1
# isMatch("aaa","aa") → 0
# isMatch("aa", "a*") → 1
# isMatch("aa", ".*") → 1
# isMatch("ab", ".*") → 1
# isMatch("aab", "c*a*b") → 1
#
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    # dp[i][j] does i chars of b match j chars of a
    def isMatch(self, A, B):
        m, n = len(A), len(B)

        dp = [[False] + [False] * m for _ in range(n + 1)]
        dp[0][0] = True

        for i in range(1, n + 1):
            if B[i - 1] == '.':
                for j in range(1, m + 1):
                    dp[i][j] = dp[i - 1][j - 1]
            elif B[i - 1] == '*':
                last = B[i - 2]
                for j in range(1, m + 1):
                    if dp[i - 2][j] or dp[i - 1][j]:
                        dp[i][j] = True
                    elif A[j - 1] == last or last == '.':
                        dp[i][j] = dp[i][j - 1]
            else:
                for j in range(1, m + 1):
                    dp[i][j] = dp[i - 1][j - 1] if A[j - 1] == B[i - 1] else False

        return int(dp[-1][-1])

    # @param A : string, text
    # @param B : string, pattern
    # @return an integer
    def regex_match(self, A, B):
        n, m = len(A), len(B)
        dp = [[1] + [0]*n] + [[0]*(n+1) for _ in range(m)]
        for i in range(1, m+1): # To support pattherns like a*b*
            if B[i-1] == '*':
                dp[i][0] = dp[i-2][0]

        for i in range (1, m+1):
            for j in range(1, n+1):
                if A[j-1] == B[i-1] or B[i-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif B[i-1] == '*':
                    dp[i][j] = dp[i-2][j]
                    if A[j-1] == B[i-2] or B[i-2] == '.':
                        dp[i][j] = 1 if dp[i][j] or dp[i][j-1] else 0
                else:
                    dp[i][j] = 0

        return dp[-1][-1]


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.isMatch('a', 'a'))
    print(s.isMatch("aa", "a"))
    print(s.isMatch("aa", "aa"))
    print(s.isMatch("aaa", "aa"))
    print(s.isMatch("aaa", "aa."))
    print(s.isMatch("aaa", "aa.."))
    print(s.isMatch("aa", "a*"))
    print(s.isMatch("aa", ".*"))
    print(s.isMatch("ab", ".*"))
    print(s.isMatch("abbbc", "ab*c"))
    print(s.isMatch("aab", "c*a*b")) #*** bad case ***#
    print(s.isMatch("ac", "ab*c"))

    print("regex_match:")

    print(s.regex_match('a', 'a'))
    print(s.regex_match("aa", "a"))
    print(s.regex_match("aa", "aa"))
    print(s.regex_match("aaa", "aa"))
    print(s.regex_match("aaa", "aa."))
    print(s.regex_match("aaa", "aa.."))
    print(s.regex_match("aa", "a*")) # *
    print(s.regex_match("aa", ".*")) # *
    print(s.regex_match("ab", ".*")) # *
    print(s.regex_match("abbbc", "ab*c"))
    print(s.regex_match("aab", "c*a*b"))
    print(s.regex_match("ac", "ab*c"))
