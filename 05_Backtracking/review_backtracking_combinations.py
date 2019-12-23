#!/usr/bin/env python3
import sys

# combinations.py
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
class Solution:
	def combine(self, A, B):
		nums = [i+1 for i in range(A)]
		return self._combine(nums, B, [])

	def _combine(self, nums, k, tmp):
		if not k: return [tmp[:]]
		ans = []

		for i in range(len(nums)):
			tmp.append(nums[i])
			ans.extend(self._combine(nums[i+1:], k-1, tmp))
			tmp.pop()

		return ans


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    #print(s.subsets([1, 2, 3]))
    print(s.combine(4, 2))