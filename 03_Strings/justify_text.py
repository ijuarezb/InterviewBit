#!/usr/bin/env python3
import sys

# Justified Text
# https://www.interviewbit.com/problems/justified-text/
#
# Given an array of words and a length L, format the text such that each line has exactly L 
# characters and is fully (left and right) justified.  You should pack your words in a greedy 
# approach; that is, pack as many words as you can in each line.
#
# Pad extra spaces ‘ ‘ when necessary so that each line has exactly L characters.
# Extra spaces between words should be distributed as evenly as possible.
# If the number of spaces on a line do not divide evenly between words, the empty slots on the 
# left will be assigned more spaces than the slots on the right. For the last line of text, 
# it should be left justified and no extra space is inserted between words.
#
# Your program should return a list of strings, where each string represents a single line.
#
# Example:
#
# words: ["This", "is", "an", "example", "of", "text", "justification."]
#
# L: 16.
#
# Return the formatted lines as:
#
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
#
#     Note: Each word is guaranteed not to exceed L in length.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    def _padding_line(self, padding, line, line_words):
    	spaces = padding // line_words if padding//line_words > 1 else 1
    	last_space = padding % line_words if padding%line_words > 0 else spaces
    	pad = ' ' * spaces
    	tmp = line.split()[:-2]
    	sentence = pad.join(line.split()[:-1])
    	sentence = sentence + ' ' * last_space + line.split()[-1]

    	return sentence


	# @param A : list of strings
    # @param B : integer
    # @return a list of strings
    def fullJustify(self, A, B):

    	result, line, line_words = [], A[0], 1

    	for word in A[1:]:

    		length = len(line) + 1 + len(word)

    		if length == B:
    			result.append(line + ' ' + word)
    			line, line_words = '', 0
    		elif length > B:
    			line = self._padding_line(B - len(line), line, line_words)
    			result.append(line.lstrip(' '))
    			line, line_words = word, 1
    		else:
    			line = line + ' ' + word
    			line_words += 1

    	if line:
    		result.append(line)

    	return result

    # @param A : list of strings
    # @param B : integer
    # @return a list of strings
    def fullJustify(self, A, B):
        result = []
        curr = 0
        tmp = []
        for word in A:
            if not word:
                continue
            if curr + len(word) <= B:
                curr += len(word) + 1
                tmp.append(word)
            else:
                result.append(self.splitWords(tmp, curr - 1, B))
                tmp = [word]
                curr = len(word) + 1
        if curr:
            result.append(' '.join(tmp) + ' ' * (B - curr + 1))
        return result

    def splitWords(self, words, curr, L):
        if len(words) == 1:
            return words[0] + " " * (L - curr)
        to_all = (L - curr) // (len(words) - 1)
        additional = (L - curr) % (len(words) - 1)
        res = words.pop(0)

        for word in words:
            res += " " * (to_all + 1)
            if additional > 0:
                res += " "
                additional -= 1
            res += word
        return res

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == '__main__':
	s = Solution()
	words = ["This", "is", "an", "example", "of", "text", "justification."]
	L = 16
	print(s.fullJustify(words, L))

	A = [ "What", "must", "be", "shall", "be." ]
	B = 12
	print(s.fullJustify(A, B))