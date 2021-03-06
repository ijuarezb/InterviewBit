#!/usr/bin/env python3
import sys

# Longest Substring Without Repeat
# https://www.interviewbit.com/problems/longest-substring-without-repeat/
#
# Given a string, 
# find the length of the longest substring without repeating characters.
#
# Example:
#
# The longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.
#
# For "bbbbb" the longest substring is "b", with the length of 1.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class  Solution():
    # @param A : string
    # @return an integer
	def longestSubstringWithoutRepeat(self, st):

		if not st or len(st) == 0:
			return 0

		sub_string = set()
		i, j = 0, 0
		max_length = 0
		max_substr = ''

		while j < len(st) and i <= j:
			set_len = len(sub_string)
			sub_string.add(st[j])
			if len(sub_string) > set_len:
				j += 1
				max_length = max(max_length, len(sub_string))
				max_substr = st[i:j+1]
			else:
				sub_string.remove(st[i])
				i += 1

		return max_length

	Complexity Analysis

	# Time complexity : 
	# O(2n)=O(n). In the worst case each character will be visited twice by i and j.

	# Space complexity : 
	# O(min(m,n)). Same as the previous approach. We need O(k) space for the sliding window, 
	# where k is the size of the Set. The size of the Set is upper bounded by the size of the string 
	# n and the size of the charset/alphabet m. 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
if __name__ == '__main__':
	s = Solution()
	print(s.longestSubstringWithoutRepeat('pwwke'))
	print(s.longestSubstringWithoutRepeat('abcabcbb'))
	print(s.longestSubstringWithoutRepeat('bbbbb'))