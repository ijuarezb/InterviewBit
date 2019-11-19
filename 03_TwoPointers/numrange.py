#!/usr/bin/env python3
import sys

# NUMRANGE
# https://www.interviewbit.com/problems/numrange/
#
#Given an array of non negative integers A, and a range (B, C), 
#find the number of continuous subsequences in the array which have sum S in the range [B, C] or B <= S <= C
#
# Continuous subsequence is defined as all the numbers A[i], A[i + 1], .... A[j]
# where 0 <= i <= j < size(A)
#
# Example :
#
# A : [10, 5, 1, 0, 2]
# (B, C) : (6, 8)
# ans = 3 
# as [5, 1], [5, 1, 0], [5, 1, 0, 2] are the only 3 continuous subsequence with their sum in the range [6, 8]
#
# NOTE : The answer is guranteed to fit in a 32 bit signed integer. 
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def numRange(self, A, B, C):
        p, q = 0, 0
        result = 0

        for p in range(len(A)):
            for q in range(len(A)-1, p-1, -1):
                temp = sum(A[p:q+1])
                #print(A[p:q+1], p, q, temp)
                if B <= temp and temp <= C:
                    #print(A[p:q+1], p, q, temp)
                    result += 1
        return result

###########################################################

    # Function to find number 
    # of subarrays having sum 
    # less than or equal to x. 
    def countSub(self, arr, n, x): 
        
        # Starting index of 
        # sliding window. 
        st = 0

        # Ending index of 
        # sliding window. 
        end = 0

        # Sum of elements currently 
        # present in sliding window. 
        sum = 0

        # To store required 
        # number of subarrays. 
        cnt = 0

        # Increment ending index 
        # of sliding window one 
        # step at a time. 
        while end < n : 
            
            # Update sum of sliding 
            # window on adding a 
            # new element. 
            sum += arr[end] 

            # Increment starting index 
            # of sliding window until 
            # sum is greater than x. 
            while (st <= end and sum > x) : 
                sum -= arr[st] 
                st += 1

            # Update count of 
            # number of subarrays. 
            cnt += (end - st + 1)
            print(cnt, end)
            end += 1


        return cnt 

    # Function to find number 
    # of subarrays having sum 
    # in the range L to R. 
    def findSubSumLtoR(self, arr, n, L, R): 
        
        # Number of subarrays 
        # having sum less 
        # than or equal to R. 
        Rcnt = self.countSub(arr, n, R) 

        # Number of subarrays 
        # having sum less than 
        # or equal to L-1. 
        Lcnt = self.countSub(arr, n, L - 1) 

        return Rcnt - Lcnt 

#########################################################

    def anotherSolution(self, A, B, C):
        p, q = 0, len(A)-1
        result = 0

        while p <= q and q < len(A):
            temp = sum(A[p:q+1])
            if B <= temp <= C:
                #print(A[p:q+1], temp)
                result += 1
                p += 1
            elif temp < B:
                q += 1
            else:
                p -= 1

        return result

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    #A = [10, 5, 1, 0, 2]
    #B = 6
    #C = 8

    A = [ 80, 97, 78, 45, 23, 38, 38, 93, 83, 16, 91, 69, 18, 82, 60, 50, 61, 70, 15, 6, 52, 90 ]
    B = 99
    C = 269

    # A = [ 76, 22, 81, 77, 95, 23, 27, 35, 24, 38, 15, 90, 19, 46, 53, 6, 77, 96, 100, 85, 43, 16, 73, 18, 7, 66 ]
    # B = 98
    # C = 290

    s = Solution()
    #print(s.numRange(A, B, C))
    #print(s.anotherSolution(A, B, C))

    # Driver code 
    #arr = [ 1, 4, 6 ] 
    #n = len(arr) 
    #L = 3
    #R = 8

    arr = [ 80, 97, 78, 45, 23, 38, 38, 93, 83, 16, 91, 69, 18, 82, 60, 50, 61, 70, 15, 6, 52, 90 ]
    L = 99
    R = 269
    print(s.findSubSumLtoR(arr, len(arr), L, R)) 

    # This code is contributed 
    # by ChitraNayal 