#!/usr/bin/env python3
import sys


# Roman To Integer
# https://www.interviewbit.com/problems/roman-to-integer/
#
# Given a roman numeral, convert it to an integer.
#
# Input is guaranteed to be within the range from 1 to 3999.
#
# Read more details about roman numerals at Roman Numeric System
#
# Example :
#
# Input : "XIV"
# Return : 14
#
# Input : "XX"
# Output : 20
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class SolutionK:
    def romanToInt(self, A):
        mapper = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        ans = 0

        for ara, rom in mapper:
            while A.startswith(rom):
                ans += ara
                A = A[len(rom):]
        return ans

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class Solution(object):

	def romanToInt(self, s):
		int_number = 0
		RD = {'M':1000, 'D': 500, 'C':100,
				'L':50, 'X':10, 'V':5, 'I':1}

		past_roman_digit = ''

		for r in s:
			int_number = int_number + RD[r]

			if past_roman_digit == 'I' and (r == 'V' or r == 'X'):
				int_number = int_number - 2
			elif past_roman_digit == 'X' and (r == 'L' or r == 'C'):
				int_number = int_number - 20
			elif past_roman_digit == 'C' and (r == 'D' or r == 'M'):
				int_number = int_number - 200

			past_roman_digit = r

		return int_number

	def intToRoman(self, s):
		rom_number = ''
		RD = {'M':1000, 'D': 500, 'C':100,
				'L':50, 'X':10, 'V':5, 'I':1}

		for rom, ara in RD.items():
			num = s // ara

			if num == 9 and rom == 'C':
				rom_number = rom_number + 'CM'
			elif num == 9 and rom == 'X':
				rom_number = rom_number + 'XC'
			elif num == 9 and rom == 'I':
				rom_number = rom_number + 'IX'
			elif num == 4 and rom == 'C':
				rom_number = rom_number + 'CD'
			elif num == 4 and rom == 'X':
				rom_number = rom_number + 'XL'
			elif num == 4 and rom == 'I':
				rom_number = rom_number + 'IV'
			else:
				rom_number = rom_number + rom*num

			s = s % ara

		return rom_number

if __name__ == '__main__':

	#num = '00000010100101000001111010011100'
	num = 'MMMCMXCIX'
	#num = 4294967293
	sol = Solution()
	print('roman number: {} integer number: {}'.format(num, sol.romanToInt(num)))
	#print('integer number: {} roman number: {}'.format(9, sol.intToRoman(9)))