#!/usr/bin/env python3
import sys
import string
import re

# Palindrome String
# https://www.interviewbit.com/problems/palindrome-string/
#
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# Example:
#
# "A man, a plan, a canal: Panama" is a palindrome.
#
# "race a car" is not a palindrome.
#
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# class Solution:
#     # @param A : string
#     # @return an integer
#     def _clear_string(self, A):
#         return ''.join(c.lower() for c in A if c.isalnum())
#
#     def _is_palindrome(self, A):
#         for i in range(len(A) // 2):
#             if A[i] != A[len(A) - 1 - i]:
#                 return False
#         return True
#
#     def isPalindrome(self, A):
#         A = self._clear_string(A)
#         return 1 if self._is_palindrome(A) else 0

# class Solution:
#     # @param A : string
#     # @return an integer
#     def isPalindrome(self, A):
#         low, high = 0, len(A) - 1
#         while low < high:
#
#             while low < high and not A[low].isalnum():
#                 low += 1
#
#             while low < high and not A[high].isalnum():
#                 high -= 1
#
#             if A[low].lower() != A[high].lower():
#                 return 0
#
#             low, high = low + 1, high - 1
#
#         return 1


class SolutionK:
    # @param A : string
    # @return an integer
    def _clear_string(self, A):
        return ''.join(c.lower() for c in A if c.isalnum())

    def isPalindrome(self, A):
        A = self._clear_string(A)
        return int(A == A[::-1])

# NOTE: I got Runtime Error with message **division by zero or array index out of bounds** and I don't know why :/

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution(object):

	def isPalindrome(self, word):
		reverse_word = ''
		for i in range(len(word)):
			reverse_word = word[i] + reverse_word
		return word == reverse_word

	def isPalindromeString(self, A):
		import re
		pattern = re.compile('[\W_]+')
		A = pattern.sub('', A)
		return self.isPalindrome(A.lower())

    def isPalindrome(self, A):
        s = []
        
        if len(A) == 0: return 1
        
        for c in A:
            if 'A' <= c <= 'Z' or 'a' <= c <= 'z' or '0' <= c <= '9':
                if 'A' <= c <= 'Z':
                    s.append(c.lower())
                else:
                    s.append(c)
        
        st = ''.join(s)
        
        if len(st) <= 1:
            return 1
        if len(st) == 2 and st[0] == st[1]:
            return 1
            
        l = len(st) // 2
        for i in range(l):
            if st[i] != st[-1-i]:
                return 0
                
        return 1

if __name__ == '__main__':

	#num = '00000010100101000001111010011100'
	word = ''
	sentence = "A man, a plan, a canal: Panama\""
	#num = 4294967293
	sol = Solution()
	print('sentence: {} is palindrome? {}'.format(sentence, sol.isPalindromeString(sentence)))