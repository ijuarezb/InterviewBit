#!/usr/bin/env python3
import sys

# Gas Station
# https://www.interviewbit.com/problems/gas-station/
#
# There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
#
# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i
# to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.
#
# Return the minimum starting gas station’s index if you can travel around the circuit once, otherwise return -1.
#
# You can only travel in one direction. i to i+1, i+2, ... n-1, 0, 1, 2..
# Completing the circuit means starting at i and ending up at i again.
#
# Example :
#
# Input :
#       Gas :   [1, 2]
#       Cost :  [2, 1]
#
# Output : 1
#
# If you start from index 0, you can fill in gas[0] = 1 amount of gas. Now your tank has 1 unit of
# gas. But you need cost[0] = 2 gas to travel to station 1.
# If you start from index 1, you can fill in gas[1] = 2 amount of gas. Now your tank has 2 units of
# gas. You need cost[1] = 1 gas to get to station 0. So, you travel to station 0 and still have 1
# unit of gas left over. You fill in gas[0] = 1 unit of additional gas, making your current gas = 2.
# It costs you cost[0] = 2 to get to station 1, which you do and complete the circuit.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return an integer
    def canCompleteCircuit(self, A, B):
        fuel = sum = start = 0

        for i in range(len(A)):
            sum += A[i] - B[i]
            fuel += A[i] - B[i]
            if fuel < 0:
                fuel, start = 0, i + 1

        return start % len(A) if sum >= 0 else -1

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #