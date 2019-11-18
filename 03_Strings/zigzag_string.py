#!/usr/bin/env python3
import sys

# Zigzag String
# https://www.interviewbit.com/problems/zigzag-string/
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like 
# this: (you may want to display this pattern in a fixed font for better legibility)
#
# P.......A........H.......N
# ..A..P....L....S....I...I....G
# ....Y.........I........R
#
# And then read line by line: PAHNAPLSIIGYIR
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR"
#
# **Example 2 : **
# ABCD, 2 can be written as
#
# A....C
# ...B....D
#
# and hence the answer would be ACBD.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def convert(self, A, B):
    	if B == 1: return A

    	rows = [''] * B
    	direction, j = 1, 0

    	for i, c in enumerate(A):
    		rows[j] += c
    		j = j + direction
    		if j == 0 or j == B-1: direction = direction *  -1

    	return ''.join(rows)

    # @param A : string
    # @param B : integer
    # @return a strings
    def convertSK(self, A, B):
        res = [''] * B

        if B == 1:
            return A

        direction, i = True, 0

        for a in A:
            res[i] += a

            if direction and i == B - 1:
                direction = False
            elif not direction and i == 0:
                direction = True

            i = i + (1 if direction else -1)

        return ''.join(res)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
if __name__ == '__main__':
	s = Solution()
	print(s.convert("PAYPALISHIRING", 3))
	print(s.convert("ABCD", 2))
	A = "kHAlbLzY8Dr4zR0eeLwvoRFg9r23Y3hEujEqdio0ctLh4jZ1izwLh70R7SAkFsXlZ8UlghCL95yezo5hBxQJ1Td6qFb3jpFrMj8pdvP6M6k7IaXkq21XhpmGNwl7tBe86eZasMW2BGhnqF6gPb1YjCTexgCurS"
	B = 1
	print(s.convert(A, B))
