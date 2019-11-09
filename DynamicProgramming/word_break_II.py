#!/usr/bin/env python3
import sys

# Word Break II
# https://www.interviewbit.com/problems/word-break-ii/
#
# Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where
# each word is a valid dictionary word.
#
# Return all such possible sentences.
#
# For example, given
#
# s = "catsanddog",
# dict = ["cat", "cats", "and", "sand", "dog"].
#
# A solution is
#
# [
#   "cat sand dog",
#   "cats and dog"
# ]
#
# Input 2:
#     A = "b"
#     B = ["aabbb"]
#
# Output 1:
#     []
#
# Make sure the strings are sorted in your result.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    class TrieNode:
        def __init__(self):
            self.chars = dict()
            self.marker = False

        def markWord(self):
            self.marker = True

        def insertWord(self, word):
            current = self
            for char in word:
                if char not in current.chars:
                    current.chars[char] = Solution.TrieNode()
                current = current.chars[char]
            current.markWord()

    def reconstruct(self, index, dp, sol):
        #print(sol)
        if index == 0:
            return [sol[1:]]
        result = list()
        for idx in dp[index]:
            result.extend(
                self.reconstruct(idx, dp, '{} {}'.format(
                    sol[:idx],
                    sol[idx:]
                )))
        return result

    # @param A : string
    # @param B : list of strings
    # @return a list of strings
    def wordBreak(self, A, B):

        n, trie = len(A), Solution.TrieNode()
        for word in B:
            trie.insertWord(word)

        dp = [list() for i in range(n + 1)]
        dp[0].append(-1)

        for i in range(n):
            if dp[i]:
                current, j = trie, i
                while j < n and A[j] in current.chars:
                    if current.chars[A[j]].marker:
                        dp[j + 1].append(i)
                    current, j = current.chars[A[j]], j + 1

        return sorted(self.reconstruct(-1, dp, A))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
if __name__ == '__main__':
    A = "catsanddog"
    B = ["cat", "cats", "and", "sand", "dog"]
    s = Solution()
    print(s.wordBreak(A, B))