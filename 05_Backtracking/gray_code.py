#!/usr/bin/env python3
import sys

# Gray Code
# https://www.interviewbit.com/problems/gray-code/
#
# The gray code is a binary numeral system where two successive values differ in only one bit.
#
# Given a non-negative integer n representing the total number of bits in the code, print the 
# sequence of gray code. A gray code sequence must begin with 0.
#
# For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:
#
# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2
# There might be multiple gray code sequences possible for a given n.
# Return any such sequence.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:

	def _swap(self, L1):
		L = []
		for i in range(len(L1)-1, -1, -1):
			L.append(L1[i])
		return L

	def _add_bit(self, L1, L2):
		n = len(L1)
		for i in range(n):
			L1[i] = '0' + L1[i]
			L2[i] = '1' + L2[i]
		return L1, L2

	def _gray_code(self, n):
		if n == 1:
			return ['0', '1']
		elif n > 1:
			L1 = self._gray_code(n-1)
			L2 = self._swap(L1)
			L1, L2 = self._add_bit(L1, L2)
			return L1 + L2

	def _binary_to_integer(self, L):
		decimal_numbers = []
		for binary_number in L:
			decimal_numbers.append(int(binary_number, 2))
		return decimal_numbers

	def gray_code(self, n):
		L = self._gray_code(n)
		return self._binary_to_integer(L)

if __name__ == '__main__':
	s = Solution()
	if len(sys.argv) > 1:
		print(s.gray_code(int(sys.argv[1])))

