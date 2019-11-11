#!/usr/bin/env python3
import sys

# MAXSPPROD
# https://www.interviewbit.com/problems/maxspprod/
#
# You are given an array A containing N integers. The special product of each ith integer in
# this array is defined as the product of the following:<ul>
#
# LeftSpecialValue: For an index i, it is defined as the index j such that A[j]>A[i] (i>j).
# If multiple A[j]’s are present in multiple positions, the LeftSpecialValue is the maximum value of j.
#
# RightSpecialValue: For an index i, it is defined as the index j such that A[j]>A[i] (j>i). If
# multiple A[j]s are present in multiple positions, the RightSpecialValue is the minimum value of j.
#
# Write a program to find the maximum special product of any integer in the array.
#
# Input: You will receive array of integers as argument to function.
#
# Return: Maximum special product of any integer in the array modulo 1000000007.
#
# Note: If j does not exist, the LeftSpecialValue and RightSpecialValue are considered to be 0.
#
# Constraints 1 <= N <= 10^5 1 <= A[i] <= 10^9
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:

    def _first_greater(self, A, prev=True):
        stack, ans = list(), [0] * len(A)

        it = range(len(A)) if prev else range(len(A)-1, -1, -1)

        for i in it:
            while stack and A[i] >= A[stack[-1]]:
                stack.pop()
            ans[i] = stack[-1] if stack else 0
            stack.append(i)

        print(stack)
        print(ans)
        return ans

    # @param A : list of integers
    # @return an integer
    def maxSpecialProduct(self, A):
        left = self._first_greater(A)
        right = self._first_greater(A, prev=False)
        maxx = -float('inf')

        for l, r in zip(left, right):
            maxx = max(l * r, maxx)

        return maxx % 1000000007

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	

#driver code
if __name__ == "__main__":
	#A = [1, 2, 0, 4, 1001, 65, 9]
	#A = [3, 30, 34, 5, 9]
	#A = [10, 10, 10, 10, 10]
	#A = [ 83564666, 2976674, 46591497, 24720696, 16376995, 63209921, 25486800, 49369261, 20465079, 64068560, 7453256, 14180682, 65396173, 45808477, 10172062, 28790225, 82942061, 88180229, 62446590, 77573854, 79342753, 2472968, 74250054, 17223599, 47790265, 24757250, 40512339, 24505824, 30067250, 82972321, 32482714, 76111054, 74399050, 65518880, 94248755, 76948016, 76621901, 46454881, 40376566, 13867770, 76060951, 71404732, 21608002, 26893621, 27370182, 35088766, 64827587, 67610608, 90182899, 66469061, 67277958, 92926221, 58156218, 44648845, 37817595, 46518269, 44972058, 27607545, 99404748, 39262620, 98825772, 89950732, 69937719, 78068362, 78924300, 91679939, 52530444, 71773429, 57678430, 75699274, 5835797, 74160501, 51193131, 47950620, 4572042, 85251576, 49493188, 77502342, 3244395, 51211050, 44229120, 2135351, 47258209, 77312779, 37416880, 59038338, 96069936, 20766025, 35497532, 67316276, 38312269, 38357645, 41600875, 58590177, 99257528, 99136750, 4796996, 84369137, 54237155, 64368327, 94789440, 40718847, 12226041, 80504660, 8177227, 85151842, 36165763, 72764013, 36326808, 80969323, 22947547, 76322099, 7536094, 18346503, 65759149, 45879388, 53114170, 92521723, 15492250, 42479923, 20668783, 64053151, 68778592, 3669297, 73903133, 28973293, 73195487, 64588362, 62227726, 17909010, 70683505, 86982984, 64191987, 71505285, 45949516, 28244755, 33863602, 18256044, 25110337, 23997763, 81020611, 10135495, 925679, 98158797, 73400633, 27282156, 45863518, 49288993, 52471826, 30553639, 76174500, 28828417, 41628693, 80019078, 64260962, 5577578, 50920883, 16864714, 54950300, 9267396, 56454292, 40872286, 33819401, 75369837, 6552946, 26963596, 22368984, 43723768, 39227673, 98188566, 1054037, 28292455, 18763814, 72776850, 47192134, 58393410, 14487674, 4852891, 44100801, 9755253, 37231060, 42836447, 38104756, 77865902, 67635663, 43494238, 76484257, 80555820, 8632145, 3925993, 81317956, 12645616, 23438120, 48241610, 20578077, 75133501, 46214776, 35621790, 15258257, 20145132, 32680983, 94521866, 43456056, 19341117, 29693292, 38935734, 62721977, 31340268, 91841822, 22303667, 96935307, 29160182, 61869130, 33436979, 32438444, 87945655, 43629909, 88918708, 85650550, 4201421, 11958347, 74203607, 37964292, 56174257, 20894491, 33858970, 45292153, 22249182, 77695201, 34240048, 36320401, 64890030, 81514017, 58983774, 88785054, 93832841, 12338671, 46297822, 26489779, 85959340 ]
	#A = [1, 1, 1, 1, 0, 1, 1, 1, 1, 1]
	#A = [5, 4, 3, 4, 5]
	A = [ 5, 9, 6, 8, 6, 4, 6, 9, 5, 4, 9 ]

	#A.sort(reverse=True)
	print("Array has lenght: ", len(A))
	print(A)
	print(A[0])
	print(A[-1])

	sol = Solution()
	#print("the max distance is: ", sol.maximumGap(A))
	print("the max distance is: ", sol.maxSpecialProduct(A))
	A.sort()
	print(A[0],A[len(A)-1])