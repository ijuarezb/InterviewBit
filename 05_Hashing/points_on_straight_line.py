#!/usr/bin/env python3
import sys

# Points on the Straight Line
# https://www.interviewbit.com/problems/points-on-the-straight-line/
#
# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
#
# Sample Input :
# (1, 1)
# (2, 2)
#
# Sample Output :
# 2
# You will be give 2 arrays X and Y. Each point is represented by (X[i], Y[i])
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    def _gcd(self, A, B):
        while B:
            A, B = B, A % B
        return A

    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def maxPoints(self, A, B):
        from collections import defaultdict

        if len(A) < 2:
            return len(A)

        maxP, dp = 0, defaultdict(lambda : 0)
        for i in range(len(A) - 1):
            currP = overlapP = verticalP = 0
            for j in range(i + 1, len(A)):
                if A[j] == A[i] and B[j] == B[i]:
                    overlapP += 1
                elif A[j] == A[i]:
                    verticalP += 1
                else:
                    diffX = A[j] - A[i]
                    diffY = B[j] - B[i]
                    g = self._gcd(diffX, diffY)

                    diffX, diffY = diffX // g, diffY // g

                    dp[(diffY, diffX)] += 1
                    currP = max(currP, dp[(diffY, diffX)])
                currP = max(currP, verticalP)
            maxP = max(maxP, currP + overlapP + 1)
            dp.clear()
        return maxP

    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def maxPoints2(self, A, B):
        from collections import defaultdict
        if len(A) < 2: return len(A)
        final_max = 0
        slopes = defaultdict(lambda : 0)
        
        for i in range(len(A)-1):
            slope_count = 0
            same_count = 0
            vertical_count = 0
            x1, y1 = A[i], B[i]
            for j in range(i+1, len(A)):
                if i != j:
                    x2, y2 = A[j], B[j]
                    if x1 == x2 and y1 == y2:
                    	same_count += 1
                    elif x1 == x2: 
                        vertical_count += 1
                        slope_count = max(slope_count, vertical_count)
                    else:
                        slope = ((y2-y1)*1.0/(x2-x1))
                        slopes[slope] += 1 
                        slope_count = max(slope_count, slopes[slope])
                        
            final_max = max(slope_count + same_count + 1 , final_max)
            slopes.clear()
            
        return final_max

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == '__main__':
	A = [1, 2, 1, 1, 1]
	B = [1, 2, 2, 3, 4]
	s = Solution()
	print(s.maxPoints2(A, B))
	print(s.maxPoints(A,B))