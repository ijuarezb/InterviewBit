#!/usr/bin/env python3
import sys

# Edit Distance
# https://www.interviewbit.com/problems/edit-distance/
#
# Given two words A and B, find the minimum number of steps required to convert A to B.
# (each operation is counted as 1 step.)
#
# You have the following 3 operations permitted on a word:
#
# Insert a character
# Delete a character
# Replace a character
# Example :
# edit distance between
# "Anshuman" and "Antihuman" is 2.
#
# Operation 1: Replace s with t.
# Operation 2: Insert i.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    def _minDistance(self, A, B, n, m, dp):

        if dp[n][m] != -1:
            return dp[n][m]

        if not m:
            dp[n][0] = n
            return n

        if not n:
            dp[0][m] = m
            return m

        if A[n - 1] == B[m - 1]:
            dp[n][m] = self._minDistance(A, B, n - 1, m - 1, dp)
        else:
            dp[n][m] = 1 + min(
                self._minDistance(A, B, n, m - 1, dp),
                self._minDistance(A, B, n - 1, m, dp),
                self._minDistance(A, B, n - 1, m - 1, dp)
            )
        return dp[n][m]

    # @param A : string
    # @param B : string
    # @return an integer
    def minDistance(self, A, B):
        n, m = len(A), len(B)
        dp = [[-1] * (m + 1) for _ in range(n + 1)]

        return self._minDistance(A, B, len(A), len(B), dp)

    def min_distance(self, A, B):
        delete, insert, replace = 1, 1, 1
        n, m = len(A), len(B)
        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(n+1):
            dp[0][i] = i * delete
        for j in range(m+1):
            dp[j][0] = j * insert

        for i in range(1, m+1):
            for j in range(1, n+1):
                if A[j-1] == B[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1]+1, dp[i][j-1]+1, dp[i-1][j]+1)

        return dp[i][j]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.minDistance("sunday", "saturday"))
    print(s.min_distance("saturday", "sunday"))