#!/usr/bin/env python3
import sys

class Solution:
    # @param A : string
    # @return a strings
    def reverseString(self, A):
        word = ''
        for c in A:
            word = c + word
        return word

    def isValid(self, A):
    	L = []
    	B = {'{':'}', '[':']', '(':')'}

    	for c in A:
    		if c in ['{', '[', '(']:
    			L.append(c)
    			#print(L)
    		elif c in ['}', ']', ')']:
    			if len(L) == 0:
    				return 0
    			else:
    				if B[L[-1]] == c:
    					L.pop()
    				else:
    					return 0

    	if len(L) > 0:
    		return 0

    	if c in ['{', '[', '(']:
            return 0

    	return 1

if __name__ == "__main__":
	word = "ana banana"
	s = Solution()
	print(s.reverseString(word))
	equation = '()[]\{\}'
	print(s.isValid(equation))