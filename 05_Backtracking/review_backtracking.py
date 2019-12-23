#!/usr/bin/env python3
import sys

# subset.py
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
class Solution:
	def _subsets(self, A, tmp, index):
		ans = [tmp[:]]
		for i in range(index, len(A)):
			tmp.append(A[i])
			ans.extend(self._subsets(A, tmp, i+1))
			#ans += self._subsets(A, tmp, i+1)
			tmp.pop()

		return ans

	def subsets(self, A):
		A.sort()
		return self._subsets(A, [], 0)

# def subsetsWithDup(self, A):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	def _subsetsWithDup(self, A, tmp, index):
		ans = [tmp[:]]
		for i in range(index, len(A)):

			if i > index and A[i] == A[i-1]:
				continue

			tmp.append(A[i])
			ans.extend(self._subsetsWithDup(A, tmp, i+1))
			tmp.pop()

		return ans

	def subsetsWithDup(self, A):
		A.sort()
		return self._subsetsWithDup(A, [], 0)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    #print(s.subsets([1, 2, 3]))
    print(s.subsetsWithDup([1, 2, 2]))