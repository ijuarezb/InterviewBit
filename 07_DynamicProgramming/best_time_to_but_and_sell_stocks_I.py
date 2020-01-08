#!/usr/bin/env python3
import sys

# Best Time to Buy and Sell Stocks
# https://www.interviewbit.com/problems/best-time-to-buy-and-sell-stocks-i/
#
# Say you have an array for which the ith element is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction (ie, buy one and sell one
# share of the stock), design an algorithm to find the maximum profit.
#
# Example :
#
# Input 1: [1 2]
# Return 1:  1
# Explanation: Buy the stock on day 0, and sell it on day 1.
#
# Input 2: A = [1, 4, 5, 2, 4]
# Output 2:  4
# Explanation: Buy the stock on day 0, and sell it on day 2.
#
# Constraints:
# 1 <= len(A) <= 7e5
# 1 <= A[i] <= 1e7
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        minBuy = float('inf')  # minimun seen so far
        maxProf = 0
        for a in A:
            maxProf = max(maxProf, a - minBuy)
            minBuy = min(minBuy, a)
        return maxProf

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

