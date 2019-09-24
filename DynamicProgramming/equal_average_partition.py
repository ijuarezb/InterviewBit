#!/usr/bin/env python3
import sys

# Equal Average Partition
# https://www.interviewbit.com/problems/equal-average-partition/
#
# Given an array with non negative numbers, divide the array into two parts such that the
# average of both the parts is equal.
# Return both parts (If exist).
# If there is no solution. return an empty list.
#
# Example:
#
#
# Input:
# [1 7 15 29 11 9]
#
# Output:
# [9 15] [1 7 11 29]

# A : [ 47, 14, 30, 19, 30, 4, 32, 32, 15, 2, 6, 24 ]
# [4 19 30 32 ] [2 6 14 15 24 47 ] 
# vs [2 4 32 47 ] [6 14 15 19 24 30 30 32 ] 

# should return empty: 18 29 0 47 0 41 40 28 7 1
#
# The average of part is (15+9)/2 = 12,
# average of second part elements is (1 + 7 + 11 + 29) / 4 = 12
#
#     NOTE 1: If a solution exists, you should return a list of exactly 2 lists of integers A
# and B which follow the following condition :
#
#         numElements in A <= numElements in B
#         If numElements in A = numElements in B, then A is lexicographically smaller than B
# ( https://en.wikipedia.org/wiki/Lexicographical_order )
#
#     NOTE 2: If multiple solutions exist, return the solution where length(A) is minimum.
# If there is still a tie, return the one where A is lexicographically smallest.
#
#     NOTE 3: Array will contain only non negative numbers.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from functools import wraps
import fractions

def memo(f):
    cache = {}

    @wraps(f)
    def wrap(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return wrap


class Solution:
    # @param A : list of integers
    # @return a list of list of integers

    @memo
    def knapsack(self, i, num, tot):
        # Find num items in A that add up to tot
        if i > len(self.A) - 1 or num <= 0 or tot <= 0:
            return None
        elif num == 1 and self.A[i] == tot:
            return [self.A[i]]
        else:
            include = self.knapsack(i + 1, num - 1, tot - self.A[i])
            exclude = self.knapsack(i + 1, num, tot)

            if include:
                return [self.A[i]] + include
            elif exclude:
                return exclude

    def avgset(self, A):
        s, n = sum(A), len(A)
        gcd = fractions.gcd(s, n)
        num = n // gcd
        self.A = sorted(A)

        for i in range(num, n // 2 + 1, num):
            k = self.knapsack(0, i, s * i // n)
            if k is not None:
                temp = k[:]
                return [k, [i for i in self.A if not i in temp or temp.remove(i)]]
        return []


    def is_possible(self, A):
        possible = False
        m = len(A) //  2
        n = len(A)
        total = sum(A)

        for i in range(m):
            if total * i % n == 0: possible = True
        return possible

    def lexicographically_smaller(self, L1, L2):
        #if len(L1) != len(L2):
        #    return L1 if len(L1) < len(L2) else L2
        for c1, c2 in zip(L1, L2):
            if c1 < c2:
                return L1
            elif c2 < c1:
                return L2
        return L1

    def diff_of_lists(self, L1, L2):
        from collections import Counter
        #A1, A2 = L1, L2 if len(L1) >= len(L2) else L2, L1
        return list((Counter(L1) - Counter(L2)).elements()) 

    def avg_set(self, A):
        if not self.is_possible(A): return []
        n = len(A)
        m = n // 2
        dp = [{0:[]} for i in range(m+1)]
        #dp[0][0].append(0)
        total = sum(A)

        for num in A:
            for i in range(m, 0, -1):
                for t in dp[i-1]:
                    if not (t + num) in dp[i]:
                        dp[i][t+num] = dp[i-1][t] + [num]
                    else:
                        dp[i][t+num] = self.lexicographically_smaller(dp[i][t+num], dp[i-1][t]+[num])

        is_possible = False
        set1 = []
        for i in range(1, m):
            if total*i%n == 0 and int(total*i/n) in dp[i]:
                set1 = dp[i][int(total*i/n)]
                is_possible = True

        set2 = self.diff_of_lists(A, set1)

        if is_possible:
            return set1, set2

        return []

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == '__main__':
    
    s = Solution()
    A = []

    for i in range(1, len(sys.argv)):
        A.append(int(sys.argv[i]))

    A.sort()
    print(s.avg_set(A))
