#!/usr/bin/env python3
import sys
# Longest Common Prefix
# https://www.interviewbit.com/problems/longest-common-prefix/
#
# Write a function to find the longest common prefix string amongst an array of strings.
#
# Longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1 and S2.
#
# As an example, longest common prefix of "abcdefgh" and "abcefgh" is "abc".
#
# Given the array of strings, you need to find the longest S which is the prefix of ALL the strings in the array.
#
# Example:
#
# Given the array as:
#
# [
#
#   "abcdefgh",
#
#   "aefghijk",
#
#   "abcefgh"
# ]
#
# The answer would be “a”.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution(object):
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        prefix = '' if not A else A[0]

        for word in A:
            i = 0
            while i < len(word) and i < len(prefix) and word[i] == prefix[i]:
                i = i + 1

            prefix = prefix[:i]

        return prefix

class SolutionI(object): 

    def commonPrefixUtil(self, str1, str2): 
        result = "" 
        n1, n2 = len(str1), len(str2) 
        i, j = 0, 0

        while i <= n1 - 1 and j <= n2 - 1: 
            if str1[i] != str2[j]: 
                break
            result += str1[i] 
            i, j = i + 1, j + 1
    
        return result 

    def commonPrefix(self, arr, low, high): 

        if low == high: 
            return arr[low] 

        if high > low: 
            mid = low + (high - low) // 2
            str1 = self.commonPrefix(arr, low, mid) 
            str2 = self.commonPrefix(arr, mid + 1, high) 

            return self.commonPrefixUtil(str1, str2)

    def longestCommonPrefix(self, strs):
        n = len(strs)

        if n == 0:
            return ""

        ans = self.commonPrefix(strs, 0, n - 1)
        return ans 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(['ana', 'anastasija', 'ananas', 'anarhija', 'an']))