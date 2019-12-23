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

	def combineLC(self, n: int, k: int) -> List[List[int]]:
	    def backtrack(first = 1, curr = []):
	        # if the combination is done
	        if len(curr) == k:  
	            output.append(curr[:])
	        for i in range(first, n + 1):
	            # add i into the current combination
	            curr.append(i)
	            # use next integers to complete the combination
	            backtrack(i + 1, curr)
	            # backtrack
	            curr.pop()
	    
	    output = []
	    backtrack()
	    return output

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


	def permuteLC(self, nums):
	    """
	    :type nums: List[int]
	    :rtype: List[List[int]]
	    """
	    def backtrack(first = 0):
	        # if all integers are used up
	        if first == n:  
	            output.append(nums[:])
	        for i in range(first, n):
	            # place i-th integer first 
	            # in the current permutation
	            nums[first], nums[i] = nums[i], nums[first]
	            # use next integers to complete the permutations
	            backtrack(first + 1)
	            # backtrack
	            nums[first], nums[i] = nums[i], nums[first]
	    
	    n = len(nums)
	    output = []
	    backtrack()
	    return output

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    #print(s.subsets([1, 2, 3]))
    print(s.combine(4, 2))
    print(s.permute([1, 2, 3]))