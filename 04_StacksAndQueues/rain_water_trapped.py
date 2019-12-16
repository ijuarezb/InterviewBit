#!/usr/bin/env python3
import sys

# Rain Water Trapped
# https://www.interviewbit.com/problems/rain-water-trapped/
#
# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it is able to trap after raining.
#
# Example :
#
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
#
# Rain water trapped: Example 1
#
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
# In this case, 6 units of rain water (blue section) are being trapped.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        left, right, ans = [0], [0], 0

        for a, b in zip(A, reversed(A)):
            left.append(max(left[-1], a))
            right.append(max(right[-1], b))

        right = list(reversed(right))

        for i, e in enumerate(A):
            ans += max(0, min(left[i + 1], right[i + 1]) - e)

        return ans

    def trap_st(self, height):
        ans, current = 0, 0
        st = list()
        while current < len(height):
            while len(st) > 0 and height[current] > height[st[-1]]:
                top = st.pop()
                if len(st) == 0:
                    break
                distance = current - st[-1] - 1
                bounded_height = min(height[current], height[st[-1]]) - height[top]
                ans += distance * bounded_height

            st.append(current)
            current += 1
        return ans

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(s.trap_st([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))