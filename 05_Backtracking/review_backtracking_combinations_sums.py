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

# permutations.py
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	def permute(self, A):
		A.sort()
		return self._permute(A, [])

	def _permute(self, nums, tmp):
		if len(tmp) == len(nums): return [tmp[:]]
		ans = []

		for i in range(len(nums)):

			if nums[i] in tmp:
				continue
			
			tmp.append(nums[i])
			ans.extend(self._permute(nums, tmp))
			tmp.pop()

		return ans

# combination_sum.py
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	def combination_sum(self, A, B):
		A.sort()
		return self._combination_sum(A, B, [], 0)

	def _combination_sum(self, nums, B, tmp, left):
		if sum(tmp) == B: return [tmp[:]]
		if sum(tmp) > B or left >= len(nums): return []
		ans = []

		for i in range(left, len(nums)):
			
			tmp.append(nums[i])
			ans.extend(self._combination_sum(nums, B, tmp, i))
			tmp.pop()

		return ans

# combination_sum_II.py
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	def combination_sum_II(self, A, B):
		A.sort()
		return self._combination_sum_II(A, B, [], 0)

	def _combination_sum_II(self, nums, B, tmp, left):
		if sum(tmp) == B:
			return [tmp[:]]
		if sum(tmp) > B or left >= len(nums):
			return []

		ans = []
		for i in range(left, len(nums)):

			if nums[i] in tmp and nums[i] != nums[i-1]:
				continue

			if i > left and nums[i] == nums[i-1]:
				continue
			
			tmp.append(nums[i])
			ans.extend(self._combination_sum_II(nums, B, tmp, i+1))
			tmp.pop()

		return ans


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    # print(s.subsets([1, 2, 3]))
    # print(s.combine(4, 2))
    # print(s.permute([1, 2, 3]))
    # print(s.combination_sum([1,2,3], 4))
    # print(s.combination_sum([10,1,2,7,6,5], 8))
    print(s.combination_sum_II([10,1,2,7,6,1,5], 8))