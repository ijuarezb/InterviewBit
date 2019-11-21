#!/usr/bin/env python3
import sys

# Largest Rectangle in Histogram
# https://www.interviewbit.com/problems/largest-rectangle-in-histogram/
#
# Given n non-negative integers representing the histogram’s bar height where the width of each bar is 1,
# find the area of largest rectangle in the histogram.
#
# Largest Rectangle in Histogram: Example 1
#
# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
#
# Largest Rectangle in Histogram: Example 2
#
# The largest rectangle is shown in the shaded area, which has area = 10 unit.
#
# For example,
# Given height = [2,1,5,6,2,3],
# return 10.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    def largestRectangleArea(self, A):
        stack, max_area = list(), 0

        for i in range(len(A)):
            if not len(stack) or A[stack[-1]] <= A[i]:
                stack.append(i)
            else:
                while len(stack) and A[stack[-1]] >= A[i]:
                    idx = stack.pop()
                    area = (i - (stack[-1] + 1 if len(stack) else 0)) * A[idx]
                    max_area = max(max_area, area)
                stack.append(i)

        while len(stack):
            idx = stack.pop()
            area = (len(A) - (stack[-1] + 1 if len(stack) else 0)) * A[idx]
            max_area = max(max_area, area)

        return max_area

    def max_area_histogram(self, histogram): 
        stack = list() 
        max_area = 0
        index = 0

        while index < len(histogram): 
            if (not stack) or (histogram[stack[-1]] <= histogram[index]): 
                stack.append(index) 
                index += 1
            else: 
                top_of_stack = stack.pop() 
                area = (histogram[top_of_stack] * ((index - stack[-1] - 1) if stack else index)) 
                max_area = max(max_area, area) 

        while stack: 
            top_of_stack = stack.pop() 
            area = (histogram[top_of_stack] * ((index - stack[-1] - 1) if stack else index)) 
            max_area = max(max_area, area) 

        return max_area 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.largestRectangleArea([2, 1, 5, 6, 2, 3]))
    print(s.largestRectangleArea([2, 1, 2]))
    print(s.largestRectangleArea([4, 2, 0, 3, 2, 5]))

    hist = [6, 2, 5, 4, 5, 1, 6] 
    print("Maximum area is", s.max_area_histogram(hist)) 