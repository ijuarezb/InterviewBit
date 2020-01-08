#!/usr/bin/env python3
import sys

# Max Product Subarray
# https://www.interviewbit.com/problems/max-product-subarray/
#
# Find the contiguous subarray within an array (containing at least one number) which has the largest product.
# Return an integer corresponding to the maximum product possible.
#
# Example :
#
# Input : [2, 3, -2, 4]
# Return : 6
#
# Possible with [2, 3]
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProduct(self, A):
        dp, ans = [(A[0], A[0])], A[0]

        for i in range(1, len(A)):
            if A[i] > 0:
                dp.append((
                    max(A[i], dp[i - 1][0] * A[i]),
                    min(A[i], dp[i - 1][1] * A[i]),
                ))
            else:
                dp.append((
                    max(A[i], dp[i - 1][1] * A[i]),
                    min(A[i], dp[i - 1][0] * A[i]),
                ))
            ans = max(ans, dp[i][0])

        return ans

    def maxProduct2(self, A):
        if not A:
            return 0
        premax, premin = A[0], A[0]
        res = A[0]
        for n in A[1:]:
            minhere = min(premax*n, premin*n, n)
            maxhere = max(premin*n, premax*n, n)
            #minhere = maxhere
            res = max(minhere, maxhere,res)
            premin = minhere
            premax = maxhere
            
        return res

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.maxProduct([2, 3, -2, 4]))
    print(s.maxProduct2([2, 3, -2, 4]))