#!/usr/bin/env python3
import sys

# Longest Consecutive Sequence
# https://www.interviewbit.com/problems/longest-consecutive-sequence/
#
# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
#
# Example: 
# Given [100, 4, 200, 1, 3, 2],
# The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
#
# Your algorithm should run in O(n) complexity.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        s = [] 
        ans=0
  
    # Hash all the array elements 
        for e in A: 
            s.append(e) 
  
    # check each possible sequence from the start 
    # then update optimal length 
        for i in range(len(A)): 
  
         # if current element is the starting 
        # element of a sequence 
            if (A[i]-1) not in s: 
  
            # Then check for next elements in the 
            # sequence 
                j=A[i] 
                while(j in s): 
                    j+=1
  
            # update  optimal length if this length 
            # is more 
                ans=max(ans, j-A[i]) 
        return ans

    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive2(self, A):
        if not A:
            return 0

        A = list(dict.fromkeys(A))
        A.sort()
        count = 1
        longest_streak = []

        for index, value in enumerate(A):
            if index + 1 >= len(A):
                break

            if A[index + 1] == value + 1:
                count += 1
                longest_streak.append(count)
            else:
                count = 1

        if not longest_streak:
            return count

        return max(longest_streak)