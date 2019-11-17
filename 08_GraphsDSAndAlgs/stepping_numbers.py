#!/usr/bin/env python3
import sys

# Stepping Numbers
# https://www.interviewbit.com/problems/stepping-numbers/
#
# Given N and M find all stepping numbers in range N to M
#
# The stepping number:
#
# A number is called as a stepping number if the adjacent digits have a difference of 1.
# e.g 123 is stepping number, but 358 is not a stepping number
#
# Example:
#
# N = 10, M = 20
# all stepping numbers are 10 , 12
# Return the numbers in sorted order.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : integer
    # @param B : integer
    # @return a list of integers
    def stepnum(self, A, B):
        from collections import deque
        queue, ans = deque(), list()

        for i in range(10):
            queue.append(i)

        while queue:
            curr = queue.popleft()
            if A <= curr <= B:
                ans.append(curr)

            if curr and curr < B:
                if curr % 10:
                    queue.append(curr * 10 + curr % 10 - 1)
                if curr % 10 < 9:
                    queue.append(curr * 10 + curr % 10 + 1)

        return ans

    # @param A : integer
    # @param B : integer
    # @return a list of integers
    def stepnum2(self, A, B):
        def nextNums(val):
            n = []
            if val - 1 >= 0:
                n.append(val-1)
            if val + 1 <= 9:
                n.append(val+1)
            return n
        graph = [i for i in range(10)]
        level = set(graph)
        res = set()
        while level:
            new_level = set()
            for num in level:
                if A <= num <= B:
                    res.add(num)
                val = num % 10
                for n in nextNums(val):
                    new_num = num*10 + n
                    if new_num <= B:
                        new_level.add(new_num)
            level = new_level
    
        return sorted(list(res))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.stepnum(0, 21))
    print(s.stepnum(10, 20))