#!/usr/bin/env python3
import sys

# Best Time to Buy and Sell Stocks II
# https://www.interviewbit.com/problems/best-time-to-buy-and-sell-stocks-ii/
#
# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many transactions as you
# like (ie, buy one and sell one share of the stock multiple times). However, you may not engage
# in multiple transactions at the same time (ie, you must sell the stock before you buy again).
#
# Example :
#
# Input 1:
#     A = [1, 2, 3]
#
# Output 1:
#     2
#
# Explanation 1:
#     => Buy a stock on day 0.
#     => Sell the stock on day 1. (Profit +1)
#     => Buy a stock on day 1.
#     => Sell the stock on day 2. (Profit +1)
#   
#     Overall profit = 2
#
# Input 2:
#     A = [5, 2, 10]
#
# Output 2:
#     8
#
# Explanation 2:
#     => Buy a stock on day 1.
#     => Sell the stock on on day 2. (Profit +8)
#    
#     Overall profit = 8
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    def maxProfit(self, A):
        sol = 0
        for i in range(1, len(A)):
            sol += max(0, A[i] - A[i - 1])
        return sol

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #