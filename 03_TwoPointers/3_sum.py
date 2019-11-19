#!/usr/bin/env python3
import sys

# 3 Sum
# https://www.interviewbit.com/problems/3-sum/
#
# Given an array S of n integers, find three integers in S such that the sum is closest to a 
# given number, target. Return the sum of the three integers.
#
# Assume that there will only be one solution
#
# Example:
# given array S = {-1 2 1 -4},
# and target = 1.
#
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        A.sort()
        minn = float('INF')
        res = -1
        for i in range(0, len(A) - 2):
            a = A[i]
            start, end = i + 1, len(A) - 1
            while start < end:
                b, c = A[start], A[end]
                print(a, b, c)

                if abs(B - (a + b + c)) < minn:
                    minn = abs(B - (a + b + c))
                    res = a + b + c

                if a + b + c == B:
                    return B
                elif a + b + c > B:
                    end = end - 1
                else:
                    start = start + 1
        return res

    def three_sum_closest(self, nums, target):
        ls = len(nums)
        if(ls < 3):
            return []

        nums = sorted(nums)

        resus = sum(nums[0:3])

        for i in range(ls - 2):
            j = i + 1
            m = ls - 1

            while(j < m):
                tem = nums[i] + nums[j] + nums[m]
                v = tem - target

                if(abs(v) < abs(resus - target)):
                    resus = tem

                if(v == 0):
                    return target
                elif(v > 0):
                    m -= 1
                else:
                    j += 1

        return resus

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    A = [-1, 2, 1, -4]
    print(s.threeSumClosest(A, 1))
    print(s.three_sum_closest(A, 1))