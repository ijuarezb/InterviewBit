#!/usr/bin/env python3
import sys

# Distinct Subsequences
# https://www.interviewbit.com/problems/distinct-subsequences/
#
# Given two sequences S, T, count number of unique ways in sequence S, to form a subsequence
# that is identical to the sequence T.
#
#  Subsequence : A subsequence of a string is a new string which is formed from the original
# string by deleting some (can be none ) of the characters without disturbing the relative
# positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
# Example :
#
# S = "rabbbit"
# T = "rabbit"
# Return 3. And the formations as follows:
#
# S1= "ra_bbit"
# S2= "rab_bit"
# S3="rabb_it"
# "_" marks the removed character.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def numDistinct(self, A, B):
        m, n = len(B), len(A)

        if m > n:
            return 0

        dp = [[1] * (n + 1)] + [[0] * (n + 1) for _ in range(m)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i][j - 1]
                # print(i, A[j-1], j, B[i-1])
                if B[i - 1] == A[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]

        return dp[-1][-1]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == '__main__':
    s = Solution()
    print(s.numDistinct('rabbbit', 'rabbit'))