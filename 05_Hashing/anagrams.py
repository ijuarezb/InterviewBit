#!/usr/bin/env python3
import sys

# Anagrams
# https://www.interviewbit.com/problems/anagrams/
#
# Given an array of strings, return all groups of strings that are anagrams. Represent a group by a 
# list of integers representing the index in the original list. Look at the sample case for clarification.
#
# Anagram : a word, phrase, or name formed by rearranging the letters of another, such as 'spar', formed from 'rasp' 
# Note: All inputs will be in lower-case. 
# Example :
#
# Input : cat dog god tca
# Output : [[1, 4], [2, 3]]
# cat and tca are anagrams which correspond to index 1 and 4. 
# dog and god are another set of anagrams which correspond to index 2 and 3.
# The indices are 1 based ( the first element has index 1 instead of index 0).
#
# Ordering of the result : You should not change the relative ordering of the words / phrases within the group. 
# Within a group containing A[i] and A[j], A[i] comes before A[j] if i < j.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        if A == None: return A
        d = {}
        list_of_groups = []
        group_number = 0
        for i in range(len(A)):
            sorted_A_i = ''.join(sorted(A[i]))
            if sorted_A_i not in d:
                list_of_groups.append([i+1])
                d[sorted_A_i] = group_number
                group_number += 1
            else:
                list_of_groups[d[sorted_A_i]].append(i+1)
        
        return  list_of_groups

    def anagramsIJB(self, A):
    	if len(A) == 0: return []
    	Anagrams = {}

    	for i, word in enumerate(A):
    		k = ''.join(sorted(word))
    		if k in Anagrams:
    			Anagrams[k].append(i+1)
    		else:
    			Anagrams[k] = [i+1]

    	return list(Anagrams.values())

if __name__ == '__main__':
	s = Solution()
	A = ['cat', 'dog', 'god', 'tca']
	print(s.anagrams(A))
	print(s.anagramsIJB(A))